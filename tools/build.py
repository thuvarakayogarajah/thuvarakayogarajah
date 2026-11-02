"""
Generates all profile graphics (light + dark) into assets/.
Edit the CONTENT section, then run:  python tools/build.py
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"

# ───────────────────────── CONTENT ─────────────────────────
NAME = "Thuvaraka"
NICK = "Thuki"
ROLE = "Junior Software Developer @ Hamilton Medical"
STUDY = "BSc Computational & Data Science @ FH Graubünden"
PLACE = "Switzerland"

NOW = "Now: writing my bachelor thesis, sharpening algorithms and learning more DevOps."

ABOUT = [
    ("01", "Backend developer", "Building services with Java, Spring Boot, MongoDB and REST APIs at Hamilton Medical since 2023."),
    ("02", "Data scientist in training", "Studying Computational & Data Science at FH Graubünden, turning raw data into decisions."),
    ("03", "From law to code", "Studied law at HSG first, started in tech support, and found my way into software."),
]

PROJECTS = [
    ("Hackathon 2026", "Hitsch Fan Quest", "Fan-experience prototype for the Spengler Cup, built with Team 1 at the Thinksport Datahack Challenge."),
    ("Bachelor thesis", "Thesis project", "Data science thesis together with an industry partner. Details coming soon."),
    ("Next up", "Coming soon", " Building something amazing."),
]

STACK = {
    "Backend": [("Java", "Jv", "#E76F00"), ("Spring Boot", "Sb", "#6DB33F"),
                ("REST APIs", "{}", "#0E7490"), ("Maven", "Mv", "#C71A36"),
                ("JUnit", "Ju", "#25A162"), ("Gradle", "Gr", "#209BC4")],
    "Databases": [("MongoDB", "Mg", "#47A248"), ("PostgreSQL", "Pg", "#336791"),
                  ("MySQL", "My", "#00758F"), ("SQLite", "Sl", "#0F80CC"),
                  ("SQL", "Sq", "#64748B"), ("Redis", "Rd", "#DC382D")],
    "Data Science": [("Python", "Py", "#3776AB"), ("Pandas", "Pd", "#6B46C1"),
                     ("NumPy", "Np", "#4DABCF"), ("Matplotlib", "Mp", "#11557C"),
                     ("Seaborn", "Sn", "#4C72B0"), ("Jupyter", "Jp", "#F37626")],
    "Machine Learning": [("scikit-learn", "Sk", "#F7931E"), ("PyTorch", "Pt", "#EE4C2C"),
                         ("TensorFlow", "Tf", "#FF8F00"), ("Keras", "Ks", "#D00000"),
                         ("Hugging Face", "HF", "#E0A100"), ("R", "R", "#276DC3")],
    "DevOps": [("Docker", "Dk", "#2496ED"), ("Kubernetes", "K8", "#326CE5"),
               ("GitHub Actions", "GA", "#2088FF"), ("Linux", "Lx", "#3F3F46"),
               ("Bash", "Sh", "#4EAA25"), ("Azure", "Az", "#0078D4")],
    "Tools": [("Git", "Gt", "#F05032"), ("GitHub", "Gh", "#3F3F46"),
              ("IntelliJ IDEA", "IJ", "#FE315D"), ("VS Code", "VS", "#007ACC"),
              ("Postman", "Pm", "#FF6C37"), ("Notion", "N", "#52525B"),
              ("Jira", "Ji", "#0052CC")],
}

LINKS = ["LinkedIn", "Email", "GitHub"]

SECTIONS = {"s01": "About me", "s02": "Featured projects", "s03": "Tools I work with",
            "s04": "On repeat", "s05": "Building in public"}

CTA_TITLE = "Let's build something together."
CTA_SUB = "Open to chats about backend, data science and sports analytics."

# ───────────────────────── THEMES ─────────────────────────
THEMES = {
    "light": dict(bg="#FBFAF8", card="#FFFFFF", ink="#16161D", muted="#6B6B78",
                  line="#E7E5EE", chip="#F2F0F8", a1="#6A11CB", a2="#2575FC",
                  k="#A626A4", s="#2E8B57", t="#C2410C"),
    "dark": dict(bg="#0D1117", card="#161B22", ink="#E6EDF3", muted="#8B949E",
                 line="#30363D", chip="#1F2630", a1="#A78BFA", a2="#60A5FA",
                 k="#F472B6", s="#86EFAC", t="#FDBA74"),
}
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "'SF Mono', 'Cascadia Code', Consolas, 'Liberation Mono', monospace"

def e(s):
    return escape(s, quote=True)

def wrap(text, n):
    lines, cur = [], ""
    for w in text.split():
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    return lines + ([cur] if cur else [])

def svg(w, h, body, c):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{c["a1"]}"/><stop offset="1" stop-color="{c["a2"]}"/></linearGradient>'
            f'<style>.sans{{font-family:{SANS}}}.mono{{font-family:{MONO}}}</style></defs>{body}</svg>')

# ───────────────────────── GRAPHICS ─────────────────────────
def hero(c):
    W, H = 1280, 440
    code = [
        [("@RestController", c["t"])],
        [("public class ", c["k"]), (NICK, c["ink"]), (" {", c["muted"])],
        [("  String ", c["k"]), ("role  ", c["ink"]), ("= ", c["muted"]), ('"Backend Dev"', c["s"]), (";", c["muted"])],
        [("  String ", c["k"]), ("study ", c["ink"]), ("= ", c["muted"]), ('"Data Science"', c["s"]), (";", c["muted"])],
        [("  String ", c["k"]), ("base  ", c["ink"]), ("= ", c["muted"]), ('" Switzerland"', c["s"]), (";", c["muted"])],
        [("  int ", c["k"]), ("languages ", c["ink"]), ("= ", c["muted"]), ("4", c["t"]), (";", c["muted"])],
        [("}", c["muted"])],
    ]
    code_svg = ""
    for i, line in enumerate(code):
        spans = "".join(f'<tspan fill="{col}">{e(t)}</tspan>' for t, col in line)
        code_svg += f'<text x="790" y="{180 + i*30}" class="mono" font-size="17" xml:space="preserve">{spans}</text>'
    body = f'''
<style>
@keyframes f1{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(40px,25px)}}}}
@keyframes f2{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-35px,-20px)}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes up{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
.o1{{animation:f1 9s ease-in-out infinite}}.o2{{animation:f2 11s ease-in-out infinite}}
.cur{{animation:blink 1.1s step-end infinite}}
.u1{{animation:up .8s ease-out both}}.u2{{animation:up .8s .15s ease-out both}}.u3{{animation:up .8s .3s ease-out both}}
</style>
<clipPath id="clip"><rect width="{W}" height="{H}" rx="28"/></clipPath>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>
  <circle class="o1" cx="1120" cy="60" r="220" fill="{c["a2"]}" opacity=".16"/>
  <circle class="o2" cx="640" cy="440" r="200" fill="{c["a1"]}" opacity=".13"/>
  <g opacity=".5" stroke="{c["line"]}">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(0, W, 64))}</g>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="28" fill="none" stroke="{c["line"]}"/>
<g class="u1"><text x="72" y="112" class="mono" font-size="18" fill="{c["a2"]}">// hello, world</text></g>
<g class="u2"><text x="68" y="190" class="sans" font-size="60" font-weight="700" fill="{c["ink"]}">Hi, I'm <tspan fill="url(#g)">{e(NAME)}</tspan></text></g>
<g class="u3">
  <text x="72" y="252" class="sans" font-size="23" fill="{c["ink"]}">{e(ROLE)}</text>
  <text x="72" y="288" class="sans" font-size="21" fill="{c["muted"]}">{e(STUDY)}</text>
  <rect x="72" y="326" width="{len(PLACE)*10 + 56}" height="40" rx="20" fill="{c["chip"]}" stroke="{c["line"]}"/>
  <circle cx="96" cy="346" r="6" fill="url(#g)"/>
  <text x="112" y="352" class="sans" font-size="16" fill="{c["ink"]}">{e(PLACE)}</text>
</g>
<rect x="760" y="96" width="452" height="290" rx="18" fill="{c["card"]}" stroke="{c["line"]}"/>
<circle cx="788" cy="124" r="6" fill="#FF5F57"/><circle cx="808" cy="124" r="6" fill="#FEBC2E"/><circle cx="828" cy="124" r="6" fill="#28C840"/>
<text x="1184" y="129" text-anchor="end" class="mono" font-size="13" fill="{c["muted"]}">{e(NICK)}.java</text>
<line x1="760" y1="146" x2="1212" y2="146" stroke="{c["line"]}"/>
{code_svg}
<rect class="cur" x="806" y="362" width="10" height="20" fill="{c["a2"]}"/>
'''
    return svg(W, H, body, c)

def section(title, num, c):
    W, H = 1280, 96
    body = f'''<text x="4" y="62" class="mono" font-size="18" fill="{c["a2"]}">{num}</text>
<text x="52" y="64" class="sans" font-size="34" font-weight="700" fill="{c["ink"]}">{e(title)}</text>
<rect x="4" y="84" width="1272" height="1" fill="{c["line"]}"/><rect x="4" y="83" width="120" height="3" rx="1.5" fill="url(#g)"/>'''
    return svg(W, H, body, c)

def card(kicker, title, text, c, big=False):
    W, H = 412, 300
    lines = wrap(text, 38)
    desc = "".join(f'<text x="32" y="{176 + i*28}" class="sans" font-size="18" fill="{c["muted"]}">{e(l)}</text>' for i, l in enumerate(lines))
    body = f'''<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="22" fill="{c["card"]}" stroke="{c["line"]}"/>
<rect x="32" y="36" width="{len(kicker)*9 + 28}" height="30" rx="15" fill="{c["chip"]}"/>
<text x="46" y="56" class="mono" font-size="14" fill="{c["a2"]}">{e(kicker)}</text>
<text x="32" y="128" class="sans" font-size="{30 if big else 26}" font-weight="700" fill="{c["ink"]}">{e(title)}</text>
<rect x="32" y="146" width="44" height="3" rx="1.5" fill="url(#g)"/>{desc}'''
    return svg(W, H, body, c)

def now(c):
    W, H = 1280, 96
    body = f'''<style>@keyframes p{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}.p{{animation:p 1.6s ease-in-out infinite}}</style>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="20" fill="{c["card"]}" stroke="{c["line"]}"/>
<circle class="p" cx="44" cy="48" r="8" fill="#22C55E"/>
<text x="68" y="55" class="sans" font-size="21" fill="{c["ink"]}">{e(NOW)}</text>'''
    return svg(W, H, body, c)

def stack(c):
    W, gap, cols = 1280, 22, 3
    cw = (W - (cols - 1) * gap) // cols
    groups = list(STACK.items())
    out, y0 = "", 0
    for r in range(0, len(groups), cols):
        row = groups[r:r + cols]
        H = 104 + max(len(t) for _, t in row) * 64 + 24
        for i, (group, tools) in enumerate(row):
            x, n = i * (cw + gap), r + i + 1
            out += (f'<rect x="{x+.5}" y="{y0+.5}" width="{cw-1}" height="{H-1}" rx="22" fill="{c["card"]}" stroke="{c["line"]}"/>'
                    f'<text x="{x+30}" y="{y0+52}" class="mono" font-size="14" fill="{c["a2"]}">{n:02d}</text>'
                    f'<text x="{x+62}" y="{y0+53}" class="sans" font-size="22" font-weight="700" fill="{c["ink"]}">{e(group)}</text>'
                    f'<rect x="{x+30}" y="{y0+70}" width="44" height="3" rx="1.5" fill="url(#g)"/>')
            for j, (name, mono, col) in enumerate(tools):
                y = y0 + 98 + j * 64
                out += (f'<rect x="{x+30}" y="{y}" width="44" height="44" rx="12" fill="{col}"/>'
                        f'<text x="{x+52}" y="{y+28}" text-anchor="middle" class="mono" font-size="16" font-weight="700" fill="#FFFFFF">{e(mono)}</text>'
                        f'<text x="{x+92}" y="{y+29}" class="sans" font-size="19" fill="{c["ink"]}">{e(name)}</text>')
                if j < len(tools) - 1:
                    out += f'<rect x="{x+92}" y="{y+54}" width="{cw-122}" height="1" fill="{c["line"]}"/>'
        y0 += H + gap
    return svg(W, y0 - gap, out, c)

def pill(label, c):
    W, H = len(label) * 10 + 48, 40
    body = f'''<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="20" fill="{c["card"]}" stroke="{c["line"]}"/>
<text x="{W/2}" y="26" text-anchor="middle" class="sans" font-size="16" font-weight="600" fill="{c["ink"]}">{e(label)}</text>'''
    return svg(W, H, body, c)

def cta(c):
    W, H = 1280, 200
    body = f'''<linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6A11CB"/><stop offset="1" stop-color="#2575FC"/></linearGradient>
<rect width="{W}" height="{H}" rx="28" fill="url(#cg)"/>
<circle cx="1180" cy="20" r="120" fill="#fff" opacity=".08"/><circle cx="1060" cy="210" r="90" fill="#fff" opacity=".08"/>
<text x="64" y="96" class="sans" font-size="40" font-weight="700" fill="#fff">{e(CTA_TITLE)}</text>
<text x="64" y="140" class="sans" font-size="21" fill="#fff" opacity=".85">{e(CTA_SUB)}</text>'''
    return svg(W, H, body, c)

# ───────────────────────── BUILD ─────────────────────────
def main():
    for theme, c in THEMES.items():
        d = OUT / theme
        d.mkdir(parents=True, exist_ok=True)
        files = {"hero.svg": hero(c), "now.svg": now(c), "stack.svg": stack(c), "cta.svg": cta(c)}
        for i, (k, t) in enumerate(SECTIONS.items(), 1):
            files[f"{k}.svg"] = section(t, f"{i:02d}", c)
        for i, (n, t, x) in enumerate(ABOUT, 1):
            files[f"a{i}.svg"] = card(n, t, x, c)
        for i, (k, t, x) in enumerate(PROJECTS, 1):
            files[f"p{i}.svg"] = card(k, t, x, c, big=True)
        for l in LINKS:
            files[f"l-{l.lower()}.svg"] = pill(l, c)
        for name, content in files.items():
            (d / name).write_text(content, encoding="utf-8")
    print(f"Built graphics into {OUT}")

if __name__ == "__main__":
    main()