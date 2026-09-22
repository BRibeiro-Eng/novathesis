import fitz
from PIL import Image
d = fitz.open('template.pdf')
toc = d.get_toc()
caps = [(t, p) for lvl, t, p in toc if lvl == 1 and p > 20][:8]
print([(t[:28], p) for t, p in caps])
ims = []
for t, p in caps[4:8]:
    px = d[p - 1].get_pixmap(dpi=80)
    ims.append(Image.frombytes('RGB', [px.width, px.height], px.samples))
w, h = ims[0].size
sh = Image.new('RGB', (2 * w, 2 * h), 'white')
for k, im in enumerate(ims):
    sh.paste(im, ((k % 2) * w, (k // 2) * h))
sh.save('.rev-ind.png')
print('ok', sh.size)
