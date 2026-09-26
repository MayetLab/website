#!/usr/bin/env python3
"""Fabrique public/assets/og.jpg — l'image d'aperçu des liens partagés.

1200 × 630 : le logo allumé en blanc sur la nuit de l'atelier, les
collines de la Montagne Bourbonnaise en bas, la devise à la craie.
Tout est lu dans public/ : logo, police Caveat, couleurs de site.css.

Usage : python3 tools/make-og.py   (nécessite Pillow)
"""
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

RACINE = Path(__file__).resolve().parent.parent / "public"
W, H = 1200, 630


def couleur(nom: str) -> tuple[int, int, int]:
    css = (RACINE / "assets/site.css").read_text(encoding="utf-8")
    hexa = re.search(rf"--{nom}:\s*#([0-9A-Fa-f]{{6}})", css).group(1)
    return tuple(int(hexa[i:i + 2], 16) for i in (0, 2, 4))


def colline(d: ImageDraw.ImageDraw, base: float, amp: float, phase: float, fill) -> None:
    import math
    pts = [(x, H * base - amp * math.sin(x / W * 2.6 * math.pi + phase)
            - amp * .45 * math.sin(x / W * 5.3 * math.pi + phase * 2))
           for x in range(0, W + 10, 10)]
    d.polygon(pts + [(W, H), (0, H)], fill=fill)


def main() -> None:
    img = Image.new("RGB", (W, H), couleur("nuit"))
    d = ImageDraw.Draw(img)
    colline(d, .76, 24, 0.4, couleur("sapin"))
    colline(d, .84, 20, 1.7, couleur("foret"))
    colline(d, .92, 16, 3.1, couleur("prairie"))

    logo = Image.open(RACINE / "assets/logo.png").convert("RGBA")
    logo.thumbnail((620, 310), Image.LANCZOS)
    alpha = logo.split()[3]
    blanc = Image.new("RGBA", logo.size, (255, 253, 246, 255))
    blanc.putalpha(alpha)
    img.paste(blanc, ((W - logo.width) // 2, 70), blanc)

    police = next((RACINE / "fonts").glob("caveat-*-latin.woff2"))
    try:
        f = ImageFont.truetype(str(police), 64)
        f.set_variation_by_axes([700])
    except Exception:
        f = ImageFont.load_default(64)
    texte = "Un tiers-lieu pour la Montagne Bourbonnaise"
    l = d.textlength(texte, font=f)
    d.text(((W - l) / 2, 70 + logo.height + 24), texte, font=f, fill=couleur("lampe"))

    img.save(RACINE / "assets/og.jpg", quality=86, optimize=True, progressive=True)
    print("public/assets/og.jpg écrit.")


if __name__ == "__main__":
    main()
