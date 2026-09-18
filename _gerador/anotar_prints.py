#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anota as capturas do dashboard para o corpo da tese (caixa F09).

    python3 _gerador/anotar_prints.py

Le as capturas ja recortadas ao canvas em ../manual-dashboard/5-figuras/prints
(1429x804, dashboard v22, dados ate 2026-07-29, captura de 2026-07-31) e
escreve PDF vetorial-com-raster em 5-Figures/cap5/.

As marcas sao numeros em circulo, e a legenda de cada numero vive na legenda
da figura em LaTeX: texto sobre a imagem seria ilegivel no tamanho impresso e
obrigaria a reanotar a imagem sempre que a redacao mudasse.
"""
import os
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(AQUI)
PRINTS = os.path.join(os.path.dirname(REPO), "manual-dashboard", "5-figuras", "prints")
DESTINO = os.path.join(REPO, "5-Figures", "cap5")
FONTE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
LARANJA = (255, 107, 53)

# (ficheiro, nome de saida, [(numero, x, y)]) em coordenadas da captura 1429x804
FIGURAS = [
    ("00.png", "dashboard-overview", [
        (1, 532, 60),    # seletores de metrica, janela e ano de referencia
        (2, 683, 278),   # matriz de semaforos unidade x vetor
        (3, 322, 268),   # ranking por desvio
        (4, 300, 586),   # pareto por par unidade-vetor
        (5, 1150, 566),  # qualidade das baselines do ano de referencia
    ]),
    ("29.png", "dashboard-baselines", [
        (1, 300, 200),   # dispersao consumo x carga com reta e banda
        (2, 850, 250),   # cartao de estatisticas
        (3, 1200, 200),  # painel das oito regras de sequencia
        (4, 300, 600),   # soma acumulada dos residuos
        (5, 1080, 600),  # residuos padronizados / consumo observado vs previsto
    ]),
]


def anota(origem, destino, marcas, raio=17):
    im = Image.open(origem).convert("RGB")
    d = ImageDraw.Draw(im)
    fonte = ImageFont.truetype(FONTE, 22)
    for n, x, y in marcas:
        # halo branco: garante contraste tanto sobre o fundo escuro como
        # sobre as barras claras dos visuais
        d.ellipse([x - raio - 2, y - raio - 2, x + raio + 2, y + raio + 2], fill="white")
        d.ellipse([x - raio, y - raio, x + raio, y + raio], fill=LARANJA)
        t = str(n)
        cx, cy, dx, dy = d.textbbox((0, 0), t, font=fonte)
        d.text((x - (dx - cx) / 2, y - (dy - cy) / 2 - 2), t, font=fonte, fill="white")
    im.save(destino, "PDF", resolution=200.0)
    return im.size


def main():
    os.makedirs(DESTINO, exist_ok=True)
    for f, nome, marcas in FIGURAS:
        o = os.path.join(PRINTS, f)
        if not os.path.exists(o):
            raise SystemExit("falta %s" % o)
        d = os.path.join(DESTINO, nome + ".pdf")
        print("%s -> %s %s" % (f, os.path.relpath(d, REPO), anota(o, d, marcas)))


if __name__ == "__main__":
    main()
