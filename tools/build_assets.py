"""Generate the profile README SVG assets (hero + project cards).

Run: python3 tools/build_assets.py
Outputs: assets/hero-dark.svg, assets/hero-light.svg, assets/cards/*.svg
Pure SVG, system fonts, no scripts or remote resources, so GitHub renders it reliably.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "panel": "#161b22",
        "border": "#30363d",
        "text": "#f0f6fc",
        "muted": "#9198a1",
        "accent": "#58a6ff",
        "artifact": "#ff9e64",
        "ok": "#3fb950",
        "grid": "#21262d",
    },
    "light": {
        "bg": "#ffffff",
        "panel": "#f6f8fa",
        "border": "#d1d9e0",
        "text": "#1f2328",
        "muted": "#59636e",
        "accent": "#0969da",
        "artifact": "#bc4c00",
        "ok": "#1a7f37",
        "grid": "#eaeef2",
    },
}


def hero(theme: str) -> str:
    c = THEMES[theme]
    stages = [
        ("fuente", "fijada + SHA-256"),
        ("contrato", "esquema validado"),
        ("tests", "pytest · CI"),
        ("artefacto", "versionado"),
    ]
    dots = "".join(
        f'<circle cx="{x}" cy="{y}" r="1.6" fill="{c["grid"]}"/>'
        for x in range(0)
        for y in range(40, 330, 22)
    )
    rail = []
    x0, y0, gap = 742, 114, 58
    for i, (name, note) in enumerate(stages):
        y = y0 + i * gap
        last = i == len(stages) - 1
        color = c["artifact"] if last else c["accent"]
        if i:
            rail.append(
                f'<line x1="{x0}" y1="{y - gap + 13}" x2="{x0}" y2="{y - 13}" '
                f'stroke="{c["border"]}" stroke-width="3"/>'
            )
        rail.append(
            f'<circle cx="{x0}" cy="{y}" r="11" fill="{c["panel"]}" stroke="{color}" stroke-width="4"/>'
        )
        if last:
            rail.append(f'<circle cx="{x0}" cy="{y}" r="5" fill="{color}"/>')
        else:
            rail.append(
                f'<path d="M{x0 - 5} {y} l3.5 3.5 l6.5 -7" fill="none" stroke="{c["ok"]}" '
                f'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
            )
        rail.append(
            f'<text x="{x0 + 30}" y="{y + 8}" font-family="{SANS}" font-size="24" '
            f'font-weight="600" fill="{c["text"]}">{escape(name)}</text>'
        )
        rail.append(
            f'<text x="{x0 + 190}" y="{y + 7}" font-family="{MONO}" font-size="18" '
            f'fill="{c["muted"]}">{escape(note)}</text>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="1200" height="360" role="img" aria-labelledby="t d">
  <title id="t">Eduardo Pacheco · Junior Python / Data Engineer</title>
  <desc id="d">Guayaquil, Ecuador. Pipelines de datos reproducibles: fuente, contrato, tests y artefacto.</desc>
  <rect width="1200" height="360" rx="24" fill="{c["bg"]}"/>
  <rect x="0.75" y="0.75" width="1198.5" height="358.5" rx="23.5" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>
  {dots}
  <rect x="696" y="44" width="456" height="272" rx="18" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5"/>
  <text x="726" y="72" font-family="{MONO}" font-size="16" letter-spacing="2" fill="{c["muted"]}">CÓMO CONSTRUYO</text>
  {"".join(rail)}
  <text x="64" y="96" font-family="{MONO}" font-size="18" letter-spacing="2.5" fill="{c["accent"]}">GUAYAQUIL · ECUADOR · 2.19°S 79.89°W</text>
  <text x="64" y="178" font-family="{SANS}" font-size="66" font-weight="800" fill="{c["text"]}">Eduardo Pacheco</text>
  <text x="64" y="232" font-family="{SANS}" font-size="32" font-weight="500" fill="{c["text"]}">Junior Python / Data Engineer</text>
  <text x="64" y="274" font-family="{SANS}" font-size="22" fill="{c["muted"]}">Ciencia de Datos e IA · ESPOL</text>
  <rect x="64" y="298" width="56" height="5" rx="2.5" fill="{c["accent"]}"/>
  <rect x="126" y="298" width="18" height="5" rx="2.5" fill="{c["artifact"]}"/>
</svg>
"""


CARDS = [
    {
        "slug": "newsroom",
        "eyebrow": "IA LOCAL · VIDEO",
        "title": "Video de noticias con IA",
        "lines": [
            "De la noticia al video: radar, guion con IA,",
            "voz, subtítulos y render, todo offline.",
        ],
        "chips": ["Python", "Node", "Ollama", "Whisper", "Remotion"],
        "accent": "#f778ba",
    },
    {
        "slug": "lakehouse",
        "eyebrow": "INGENIERÍA ANALÍTICA",
        "title": "Lakehouse de datos abiertos",
        "lines": [
            "Datos del SRI, INEC y BCE verificados con",
            "checksums y modelados con dbt en DuckDB.",
        ],
        "chips": ["dbt", "DuckDB", "Parquet", "Python"],
        "accent": "#6cb6ff",
    },
    {
        "slug": "mlops",
        "eyebrow": "MLOPS",
        "title": "Laboratorio MLOps",
        "lines": [
            "Validación, MLflow, registro de modelos,",
            "servicio con FastAPI y monitoreo de drift.",
        ],
        "chips": ["MLflow", "FastAPI", "scikit-learn", "Docker"],
        "accent": "#d2a8ff",
    },
    {
        "slug": "indicadores",
        "eyebrow": "APP DE ESCRITORIO",
        "title": "Indicadores Ecuador",
        "lines": [
            "Explora y compara indicadores del Banco",
            "Mundial sin conexión, en tu escritorio.",
        ],
        "chips": ["Tauri", "Rust", "React", "TypeScript"],
        "accent": "#f5c400",
    },
    {
        "slug": "agente-sql",
        "eyebrow": "IA LOCAL · TEXT-TO-SQL",
        "title": "Agente analista SQL local",
        "lines": [
            "Responde en español sobre compras públicas",
            "de Ecuador con SQL de solo lectura validado.",
        ],
        "chips": ["Python", "DuckDB", "Ollama", "FastAPI"],
        "accent": "#39c5cf",
    },
    {
        "slug": "sismos",
        "eyebrow": "STREAMING EN TIEMPO REAL",
        "title": "Sismos en tiempo real",
        "lines": [
            "Terremotos reales de USGS en streaming,",
            "con un solo comando en tu máquina.",
        ],
        "chips": ["Redpanda", "ClickHouse", "Grafana", "Python"],
        "accent": "#e5534b",
    },
    {
        "slug": "fallas-viales",
        "eyebrow": "VISIÓN POR COMPUTADORA",
        "title": "Detección de fallas viales",
        "lines": [
            "Grietas y baches en fotos y video con",
            "RT-DETRv2 e inferencia ONNX sin PyTorch.",
        ],
        "chips": ["RT-DETRv2", "ONNX", "PyTorch", "FastAPI"],
        "accent": "#ffa657",
    },
    {
        "slug": "clasificador",
        "eyebrow": "NLP · ESPAÑOL",
        "title": "Clasificador de texto LoRA",
        "lines": [
            "60 intenciones en español con MrBERT-es",
            "ajustado con LoRA y servido con ONNX.",
        ],
        "chips": ["Transformers", "LoRA", "ONNX", "FastAPI"],
        "accent": "#b083f0",
    },
    {
        "slug": "decision-platform",
        "eyebrow": "PLATAFORMA DE DATOS",
        "title": "Decision Intelligence Platform",
        "lines": [
            "Ingesta programada con FastAPI y SQLite,",
            "con estados de falla observables.",
        ],
        "chips": ["FastAPI", "SQLite", "Python", "pytest"],
        "accent": "#7ee787",
    },
    {
        "slug": "rag",
        "eyebrow": "RAG CON EVIDENCIA",
        "title": "Evidence-Grounded RAG",
        "lines": [
            "Recuperación híbrida, citas validadas y",
            "abstención cuando no hay evidencia.",
        ],
        "chips": ["Python", "Búsqueda híbrida", "Evaluación"],
        "accent": "#e3b341",
    },
]


def card(data: dict) -> str:
    c = THEMES["dark"]
    accent = data["accent"]
    chips, x = [], 40
    for chip in data["chips"]:
        width = int(len(chip) * 10.2 + 28)
        chips.append(
            f'<rect x="{x}" y="232" width="{width}" height="34" rx="17" fill="{c["bg"]}" stroke="{c["border"]}"/>'
            f'<text x="{x + width / 2}" y="255" text-anchor="middle" font-family="{MONO}" font-size="16" '
            f'fill="{c["text"]}">{escape(chip)}</text>'
        )
        x += width + 10
    lines = "".join(
        f'<text x="40" y="{168 + i * 30}" font-family="{SANS}" font-size="21" fill="{c["muted"]}">{escape(line)}</text>'
        for i, line in enumerate(data["lines"])
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="600" height="300" role="img" aria-labelledby="t">
  <title id="t">{escape(data["title"])}</title>
  <rect width="600" height="300" rx="20" fill="{c["panel"]}"/>
  <rect x="0.75" y="0.75" width="598.5" height="298.5" rx="19.25" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>
  <rect x="40" y="34" width="44" height="6" rx="3" fill="{accent}"/>
  <text x="40" y="74" font-family="{MONO}" font-size="16" letter-spacing="2" fill="{accent}">{escape(data["eyebrow"])}</text>
  <text x="40" y="118" font-family="{SANS}" font-size="32" font-weight="700" fill="{c["text"]}">{escape(data["title"])}</text>
  {lines}
  {"".join(chips)}
  <path d="M548 44 l12 12 l-12 12" fill="none" stroke="{c["muted"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


def main() -> None:
    (ASSETS / "cards").mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        (ASSETS / f"hero-{theme}.svg").write_text(hero(theme), encoding="utf-8")
    for data in CARDS:
        (ASSETS / "cards" / f"{data['slug']}.svg").write_text(card(data), encoding="utf-8")
    print(f"wrote {2 + len(CARDS)} SVG files under {ASSETS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
