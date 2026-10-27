#!/usr/bin/env python3
"""Build a self-contained HTML presentation from content/slides-<lang>.md.

Usage:
  python3 tools/build_slides.py content/slides-en.md slides/presentation-en.html --lang en
  python3 tools/build_slides.py content/slides-de.md slides/presentation-de.html --lang de

The wording on the slides comes only from the markdown file. The design lives in
tools/slides-template.html. Do not edit the generated HTML by hand: change the
markdown or the template and build again.

Markdown format per slide:
  ## <number>. <title> (<minutes> min)
  **Slide**       what is on screen
  **Animation**   optional, only slides 4, 12, 14 and 17 use it
  **Notes**       what the speaker says
Backup slides sit under "# Backup slides" and are numbered B1, B2, ...
"""
import argparse
import html
import json
import re
from pathlib import Path

UI = {
    "en": {
        "help_title": "Keys",
        "help": [
            ["Right  Space  click", "Next"],
            ["Left", "Back"],
            ["F", "Full screen"],
            ["N", "Notes panel (visible if you share this window)"],
            ["P", "Presenter window with notes and timer (share only the slides window)"],
            ["B", "Build mode: points appear one by one"],
            ["R", "Replay the animation"],
            ["H", "This help"],
        ],
        "next": "Next",
        "plan": "Plan: done after {m} min",
        "popup": "Pop-up blocked. Allow pop-ups for this page.",
        "build_on": "Build mode: on",
        "build_off": "Build mode: off",
        "backup": "Backup slides",
        "notes": "Notes",
    },
    "de": {
        "help_title": "Tasten",
        "help": [
            ["Rechts  Leertaste  Klick", "Weiter"],
            ["Links", "Zurück"],
            ["F", "Vollbild"],
            ["N", "Notizen-Leiste (sichtbar, wenn du dieses Fenster teilst)"],
            ["P", "Moderatorfenster mit Notizen und Uhr (nur das Folienfenster teilen)"],
            ["B", "Aufbau-Modus: Punkte erscheinen einzeln"],
            ["R", "Animation wiederholen"],
            ["H", "Diese Hilfe"],
        ],
        "next": "Als Nächstes",
        "plan": "Plan: fertig nach {m} Min.",
        "popup": "Pop-up blockiert. Pop-ups für diese Seite erlauben.",
        "build_on": "Aufbau-Modus: an",
        "build_off": "Aufbau-Modus: aus",
        "backup": "Zusatzfolien (Backup)",
        "notes": "Notizen",
    },
}


def esc(s):
    return html.escape(s, quote=False)


def inline(s):
    s = esc(s)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)


# ---------- parsing ----------

def parse_file(text):
    main, _, backup = text.partition("\n# Backup slides")
    slides = []
    for part, is_backup in ((main, False), (backup, True)):
        for sec in re.split(r"^## ", part, flags=re.M)[1:]:
            slides.append(parse_section(sec, is_backup))
    return slides


def parse_section(sec, is_backup):
    lines = sec.split("\n")
    header, rest = lines[0].strip(), lines[1:]
    m = re.match(r"^(B?\d+)\.\s+(.*?)(?:\s*\(([\d.,]+)\s*[^)]*\))?\s*$", header)
    if not m:
        raise SystemExit(f"Cannot read slide header: {header!r}")
    num, title, minutes = m.group(1), m.group(2), m.group(3)
    parts = {"slide": [], "animation": [], "notes": []}
    cur = "slide"
    for ln in rest:
        mk = re.match(r"^\*\*(Slide|Animation|Notes)\*\*\s*$", ln.strip())
        if mk:
            cur = mk.group(1).lower()
            continue
        if ln.strip() == "---":
            continue
        parts[cur].append(ln)
    return {
        "num": num,
        "title": title,
        "minutes": float(minutes.replace(",", ".")) if minutes else None,
        "backup": is_backup,
        "slide": parts["slide"],
        "animation": " ".join(l.strip() for l in parts["animation"] if l.strip()),
        "notes": parts["notes"],
    }


LIST_RE = re.compile(r"^(\s*)(-|\d+\.)\s+(.*)$")


def parse_blocks(lines):
    blocks, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
            blocks.append(("table", rows))
            continue
        m = LIST_RE.match(ln)
        if m:
            ordered = m.group(2) != "-"
            items = []
            while i < len(lines):
                m = LIST_RE.match(lines[i])
                if not m:
                    break
                if len(m.group(1)) == 0:
                    items.append({"text": m.group(3), "children": []})
                elif items:
                    items[-1]["children"].append(m.group(3))
                i += 1
            blocks.append(("list", {"ordered": ordered, "items": items}))
            continue
        blocks.append(("para", ln.strip()))
        i += 1
    nodes, i = [], 0
    while i < len(blocks):
        b = blocks[i]
        if (b[0] == "para" and head_text(b[1]) is not None
                and i + 1 < len(blocks) and blocks[i + 1][0] == "list"):
            nodes.append({"type": "group", "head": head_text(b[1]), "list": blocks[i + 1][1]})
            i += 2
        else:
            nodes.append({"type": b[0], "data": b[1]})
            i += 1
    return nodes


def head_text(p):
    plain = p.replace("**", "").strip()
    return plain[:-1].strip() if plain.endswith(":") else None


def label_of(text):
    m = re.match(r"^\*\*([^*]+?):\*\*\s*(.*)$", text)
    if m:
        return m.group(1), m.group(2)
    m = re.match(r"^([^:*]{1,26}):\s+(.+)$", text)
    if m:
        return m.group(1), m.group(2)
    return None


# ---------- rendering ----------

def sub_list(children):
    if not children:
        return ""
    return '<ul class="sub">' + "".join(f"<li>{inline(c)}</li>" for c in children) + "</ul>"


def list_html(lst, extra=""):
    tag = "ol" if lst["ordered"] else "ul"
    lis = "".join(f'<li class="step">{inline(it["text"])}{sub_list(it["children"])}</li>'
                  for it in lst["items"])
    return f'<{tag} class="b {extra}">{lis}</{tag}>'


def group_html(g, in_cols):
    extra = "two" if (not in_cols and len(g["list"]["items"]) >= 6) else ""
    cls = "gbox" if in_cols else "group"
    return f'<div class="{cls}"><h3>{inline(g["head"])}</h3>{list_html(g["list"], extra)}</div>'


def flow_list_html(lst, pyramid=False):
    items = lst["items"]
    labelled = [label_of(it["text"]) for it in items]
    if all(labelled):
        if pyramid and not lst["ordered"]:
            n = len(items)
            out = ['<div class="pyr">']
            for k, (it, (lab, rest)) in enumerate(zip(items, labelled)):
                w = 46 + k * (54 / max(n - 1, 1))
                a = 0.10 + k * (0.22 / max(n - 1, 1))
                out.append(
                    f'<div class="layer step" style="--w:{w:.0f}%;--a:{a:.2f}">'
                    f'<strong>{esc(lab)}:</strong> {inline(rest)}</div>')
            out.append("</div>")
            return "".join(out)
        if lst["ordered"]:
            cols = 3 if len(items) % 3 == 0 else 2
            cards = "".join(
                f'<div class="card step"><div class="n">{k + 1}</div>'
                f'<div class="l">{esc(lab)}</div><div class="t">{inline(rest)}</div></div>'
                for k, (lab, rest) in enumerate(labelled))
            return f'<div class="cards" style="--c:{cols}">{cards}</div>'
        rows = "".join(
            f'<div class="row step"><div class="l">{esc(lab)}</div>'
            f'<div class="t">{inline(rest)}{sub_list(it["children"])}</div></div>'
            for it, (lab, rest) in zip(items, labelled))
        return f'<div class="rows">{rows}</div>'
    return list_html(lst)


def table_html(rows):
    head, body = rows[0], rows[1:]
    th = "".join(f"<th>{inline(c)}</th>" for c in head)
    tr = "".join('<tr class="step">' + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                 for r in body)
    return f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def chevron_html(t):
    label = ""
    m = re.match(r"^([^:>]{1,25}):\s+(.*)$", t)
    if m and " > " in m.group(2):
        label, t = m.group(1), m.group(2)
    steps = "".join(f"<span>{inline(p)}</span>" for p in t.split(" > "))
    lab = f'<div class="chev-label">{esc(label)}</div>' if label else ""
    return f'{lab}<div class="chev">{steps}</div>'


def para_html(t, first):
    if t.count(" > ") >= 2:
        return chevron_html(t)
    if first:
        return f'<p class="lead">{inline(t)}</p>'
    m = re.match(r"^\*\*([^*]+?):\*\*\s+(.+)$", t) or re.match(r"^([A-Z][^:]{0,28}):\s+(.+)$", t)
    if m:
        return (f'<div class="kv step"><div class="k">{esc(m.group(1))}</div>'
                f'<div class="v">{inline(m.group(2))}</div></div>')
    return f'<p class="plain step">{inline(t)}</p>'


def render_nodes(nodes, pyramid=False, first=True):
    out, i = [], 0
    while i < len(nodes):
        n = nodes[i]
        if n["type"] == "group":
            grp = []
            while i < len(nodes) and nodes[i]["type"] == "group":
                grp.append(nodes[i])
                i += 1
            if len(grp) >= 2:
                out.append(f'<div class="cols" style="--n:{min(len(grp), 3)}">'
                           + "".join(group_html(g, True) for g in grp) + "</div>")
            else:
                out.append(group_html(grp[0], False))
        else:
            if n["type"] == "para":
                out.append(para_html(n["data"], first))
            elif n["type"] == "list":
                out.append(flow_list_html(n["data"], pyramid))
            elif n["type"] == "table":
                out.append(table_html(n["data"]))
            i += 1
        first = False
    return "".join(out)


def loop_svg(animation):
    m = re.search(r"loop:\s*(.+?)\s*>\s*(.+?)\s*>\s*(.+?)\.", animation)
    labels = [m.group(k).strip() for k in (1, 2, 3)] if m else ["AI suggests", "A person checks", "The team decides"]
    labels = [l[0].upper() + l[1:] for l in labels]
    boxes = []
    for k, x in enumerate((20, 330, 640)):
        cls = "lnode person" if k == 1 else "lnode"
        boxes.append(f'<rect class="{cls}" x="{x}" y="10" width="240" height="58" rx="16"/>'
                     f'<text class="ltxt{" pb" if k == 1 else ""}" x="{x + 120}" y="46" text-anchor="middle">{esc(labels[k])}</text>')
    return (
        '<svg class="loop nobuild" viewBox="0 0 900 128" role="img" aria-label="'
        + esc(" > ".join(labels)) + '">'
        '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0 0L10 5L0 10z" class="ltip"/></marker></defs>'
        + "".join(boxes) +
        '<path class="larrow" d="M260 39H326" marker-end="url(#ah)"/>'
        '<path class="larrow" d="M570 39H636" marker-end="url(#ah)"/>'
        '<path class="larrow" d="M760 68C760 122 140 122 140 74" marker-end="url(#ah)"/>'
        '<circle class="ldot" r="8"><animateMotion dur="7s" repeatCount="indefinite" '
        'path="M140 39H450H760C760 122 140 122 140 39"/></circle></svg>')


def render_slide(s, idx, main_total, ui, first_main, last_main):
    """Return the slide's HTML section."""
    nodes = parse_blocks(s["slide"])
    num = s["num"]
    kind, fs, body = "generic", 24, ""
    label = num if s["backup"] else f"{idx + 1} / {main_total}"

    if idx == first_main and not s["backup"]:
        lists = [n for n in nodes if n["type"] == "list"]
        items = [it["text"] for it in lists[0]["data"]["items"]] if lists else []
        items += [""] * 3
        return (f'<section class="slide title" data-kind="title" data-label="{esc(label)}">'
                f'<div class="tbody"><h1>{inline(items[0])}</h1><p class="tag">{inline(items[1])}</p>'
                + (f'<p class="by">{inline(items[2])}</p>' if items[2] else '') + '</div></section>')

    if num == "4" and not s["backup"]:
        paras = [n for n in nodes if n["type"] == "para"]
        lists = [n for n in nodes if n["type"] == "list" and n["data"]["ordered"]]
        if paras and lists:
            its = lists[0]["data"]["items"]
            rows = "".join(
                f'<div class="rrow{" top" if k < 4 else ""}" style="top:{k * 2.5}em">'
                f'<span class="rn">{k + 1}</span><span class="rt">{inline(it["text"])}</span></div>'
                for k, it in enumerate(its))
            body = (f'<div class="rankwrap"><div class="formula">{inline(paras[0]["data"])}</div>'
                    f'<div class="rank nobuild" style="height:{len(its) * 2.5}em">{rows}</div></div>')
            kind, fs = "rank", 21
    elif num == "14" and not s["backup"]:
        chev = nodes[0] if nodes and nodes[0]["type"] == "para" else None
        lst = next((n for n in nodes if n["type"] == "list"), None)
        if chev and lst and chev["data"].count(" > ") >= 2:
            names = chev["data"].split(" > ")
            det = [label_of(it["text"]) for it in lst["data"]["items"]]
            if len(names) == len(det) and all(det):
                rest = [n for n in nodes if n is not chev and n is not lst]
                body = (
                    '<div class="pipe nobuild"><div class="mover"></div>'
                    f'<div class="pgrid pnames" style="--c:{len(names)}">'
                    + "".join(f'<div class="pnode">{inline(n)}</div>' for n in names) + "</div>"
                    f'<div class="pgrid ptrack" style="--c:{len(names)}">'
                    + '<div class="lcell"><span class="light ok"></span></div>' * len(names) + "</div>"
                    f'<div class="pgrid pdetails" style="--c:{len(names)}">'
                    + "".join(f'<div class="pdetail">{inline(d[1])}</div>' for d in det) + "</div></div>"
                    + render_nodes([dict(n) for n in rest], first=False).replace('class="kv step"', 'class="kv"'))
                kind, fs = "pipe", 24
    if not body:
        body = render_nodes(nodes, pyramid=(num == "10" and not s["backup"]))
        if num == "17" and not s["backup"]:
            body += loop_svg(s["animation"])
            kind = "loop"
        if num == "12" and not s["backup"]:
            kind = "cycle"
        if idx == last_main and not s["backup"]:
            kind, fs = "closing", 30
        if s["backup"]:
            fs = 22
    return (f'<section class="slide" data-kind="{kind}" data-fs="{fs}" data-label="{esc(label)}">'
            f'<h2>{inline(s["title"])}</h2><div class="body">{body}</div>'
            f'<div class="count">{esc(label)}</div></section>')


def notes_html(lines):
    text = "\n".join(lines).strip()
    paras = [re.sub(r"\s*\n\s*", " ", p) for p in re.split(r"\n\s*\n", text) if p.strip()]
    return "".join(f"<p>{inline(p)}</p>" for p in paras)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--lang", default="en", choices=sorted(UI))
    ap.add_argument("--title", default="")
    a = ap.parse_args()

    ui = UI[a.lang]
    slides = parse_file(Path(a.src).read_text(encoding="utf-8"))
    main_slides = [s for s in slides if not s["backup"]]
    backups = [s for s in slides if s["backup"]]
    total = len(main_slides)

    sections, data = [], []
    for i, s in enumerate(main_slides):
        sections.append(render_slide(s, i, total, ui, 0, total - 1))
        data.append({"label": f"{i + 1} / {total}", "title": s["title"],
                     "minutes": s["minutes"], "notes": notes_html(s["notes"])})
    if backups:
        sections.append(f'<section class="slide divider" data-kind="divider" data-label="">'
                        f'<div class="tbody"><h1>{esc(ui["backup"])}</h1></div></section>')
        data.append({"label": "", "title": ui["backup"], "minutes": None, "notes": ""})
        for j, s in enumerate(backups):
            sections.append(render_slide(s, j, total, ui, -1, -1))
            data.append({"label": s["num"], "title": s["title"], "minutes": None,
                         "notes": notes_html(s["notes"])})

    tpl = (Path(__file__).parent / "slides-template.html").read_text(encoding="utf-8")
    payload = json.dumps({"ui": ui, "slides": data, "lang": a.lang}, ensure_ascii=False).replace("</", "<\\/")
    help_rows = "".join(f"<div><kbd>{esc(k)}</kbd><span>{esc(v)}</span></div>" for k, v in ui["help"])
    first_items = [n for n in parse_blocks(main_slides[0]["slide"]) if n["type"] == "list"] if main_slides else []
    page_title = a.title or (re.sub(r"\*\*", "", first_items[0]["data"]["items"][0]["text"]) if first_items else "Presentation")
    out = (tpl.replace("%%LANG%%", a.lang)
              .replace("%%TITLE%%", esc(page_title))
              .replace("%%SLIDES%%", "\n".join(sections))
              .replace("%%DATA%%", payload)
              .replace("%%HELP_TITLE%%", esc(ui["help_title"]))
              .replace("%%HELP%%", help_rows))
    Path(a.dst).parent.mkdir(parents=True, exist_ok=True)
    Path(a.dst).write_text(out, encoding="utf-8")
    print(f"Built {a.dst}: {total} slides + {len(backups)} backup slides")


if __name__ == "__main__":
    main()
