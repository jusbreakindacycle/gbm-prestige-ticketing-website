from PIL import Image, ImageDraw, ImageFilter

out = 'public/images/hero-travel-main.jpg'
W, H = 1600, 1200
img = Image.new('RGB', (W, H), '#f7efe4')
draw = ImageDraw.Draw(img)

for y in range(H):
    t = y / H
    r = int(250 - 40 * t)
    g = int(244 - 10 * t)
    b = int(244 - 20 * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

sun = (1300, 220)
for radius in range(220, 420, 24):
    draw.ellipse((sun[0] - radius, sun[1] - radius, sun[0] + radius, sun[1] + radius), outline=(255, 215, 135, 80))
draw.ellipse((sun[0] - 90, sun[1] - 90, sun[0] + 90, sun[1] + 90), fill=(255, 213, 128))

water = Image.new('RGBA', (W, H), (0, 0, 0, 0))
wd = ImageDraw.Draw(water)
wd.pieslice((0, 320, W, H + 200), 0, 180, fill=(24, 90, 146, 255))
wd.pieslice((0, 390, W, H + 220), 0, 180, fill=(47, 125, 174, 255))
wd.pieslice((0, 460, W, H + 260), 0, 180, fill=(80, 156, 196, 255))
wd.polygon([
    (0, 560), (120, 520), (220, 548), (330, 510), (430, 534), (570, 492), (720, 510),
    (840, 482), (960, 504), (1080, 470), (1220, 500), (1400, 460), (1600, 500),
    (1600, 1200), (0, 1200)
], fill=(23, 113, 78, 255))
wd.ellipse((0, 500, W, H + 80), fill=(44, 126, 92, 140))
for y in range(620, 900, 40):
    wd.line([(0, y), (W, y)], fill=(255, 255, 255, 70))

img = Image.alpha_composite(img.convert('RGBA'), water).convert('RGB')

for y in range(560, 760):
    alpha = int(20 * (1 - abs(y - 660) / 220))
    draw.line([(0, y), (W, y)], fill=(255, 255, 255, alpha))

island = Image.new('RGBA', (W, H), (0, 0, 0, 0))
idraw2 = ImageDraw.Draw(island)
for x0, x1, y0, y1, color in [
    (0, 240, 620, 760, (14, 79, 53)),
    (220, 500, 640, 780, (20, 96, 64)),
    (520, 820, 620, 770, (16, 84, 58)),
    (1000, 1320, 640, 780, (22, 99, 66)),
    (1280, 1600, 620, 790, (16, 81, 56)),
]:
    idraw2.ellipse((x0, y0, x1, y1), fill=color)
for x in [280, 390, 540, 720, 950, 1100, 1320]:
    idraw2.rectangle((x - 4, 700, x + 4, 760), fill=(26, 96, 68))
    idraw2.polygon([(x - 18, 700), (x, 650), (x + 18, 700)], fill=(34, 120, 80))
    idraw2.polygon([(x - 12, 690), (x, 640), (x + 12, 690)], fill=(44, 141, 96))
img = Image.alpha_composite(img.convert('RGBA'), island).convert('RGB')

vignette = Image.new('RGBA', (W, H), (0, 0, 0, 0))
vd = ImageDraw.Draw(vignette)
for i in range(80):
    alpha = int(18 * i / 80)
    vd.rectangle((i, i, W - i - 1, H - i - 1), outline=(0, 0, 0, alpha))
img = Image.alpha_composite(img.convert('RGBA'), vignette).convert('RGB')
img = img.filter(ImageFilter.GaussianBlur(0.6))
img.save(out, quality=92, optimize=True)
print(out, 'created')
