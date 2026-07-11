from PIL import Image, ImageDraw, ImageFilter

out = 'public/images/about-travel-support.jpg'
W, H = 1600, 1200
img = Image.new('RGB', (W, H), '#f3efe9')
draw = ImageDraw.Draw(img)

for y in range(H):
    t = y / H
    r = int(248 - 20 * t)
    g = int(244 - 8 * t)
    b = int(240 - 10 * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

sun = (1280, 220)
for radius in range(180, 340, 22):
    draw.ellipse((sun[0] - radius, sun[1] - radius, sun[0] + radius, sun[1] + radius), outline=(255, 214, 140, 45))
draw.ellipse((sun[0] - 95, sun[1] - 95, sun[0] + 95, sun[1] + 95), fill=(255, 214, 140))

water = Image.new('RGBA', (W, H), (0, 0, 0, 0))
wd = ImageDraw.Draw(water)
wd.rectangle((0, 560, W, H), fill=(24, 88, 129))
wd.rectangle((0, 600, W, H), fill=(34, 111, 156))
wd.rectangle((0, 660, W, H), fill=(59, 136, 177))
wd.polygon([(0, 560), (120, 520), (260, 540), (410, 500), (560, 525), (720, 490), (920, 515), (1120, 480), (1400, 500), (1600, 470), (1600, 1200), (0, 1200)], fill=(23, 107, 79, 255))
for y in range(580, 760):
    alpha = int(30 * (1 - abs(y - 670) / 140))
    wd.line([(0, y), (W, y)], fill=(255, 255, 255, alpha))
img = Image.alpha_composite(img.convert('RGBA'), water).convert('RGB')

panel = Image.new('RGBA', (W, H), (0, 0, 0, 0))
pd = ImageDraw.Draw(panel)
pd.rounded_rectangle((220, 260, 1380, 980), radius=34, fill=(255, 255, 255, 230))
pd.rounded_rectangle((240, 280, 1400, 1000), radius=34, outline=(16, 54, 90, 80))

pd.rounded_rectangle((320, 360, 540, 620), radius=22, fill=(250, 247, 240, 255))
pd.rounded_rectangle((334, 375, 526, 606), radius=18, fill=(255, 255, 255, 220))
pd.rectangle((348, 395, 512, 430), fill=(30, 90, 130))
pd.rectangle((348, 448, 512, 482), fill=(13, 69, 103))

pd.rounded_rectangle((620, 380, 860, 610), radius=20, fill=(244, 241, 234, 255))
pd.rectangle((648, 405, 832, 465), fill=(17, 70, 110))
pd.rectangle((648, 485, 832, 525), fill=(100, 142, 173))

pd.ellipse((1020, 420, 1240, 720), fill=(19, 78, 116))
pd.rectangle((1040, 430, 1220, 690), fill=(23, 95, 141))
pd.ellipse((1080, 430, 1180, 470), fill=(31, 117, 177))

pd.ellipse((1280, 405, 1340, 465), fill=(37, 129, 79))
pd.line((1290, 450, 1320, 500), fill=(37, 129, 79), width=8)
pd.line((1320, 500, 1360, 560), fill=(37, 129, 79), width=8)
pd.ellipse((1360, 530, 1420, 590), fill=(248, 172, 72))

pd.ellipse((300, 780, 430, 890), fill=(38, 122, 77, 50))
pd.ellipse((760, 760, 920, 920), fill=(44, 128, 176, 45))
pd.ellipse((1160, 760, 1320, 900), fill=(138, 176, 203, 45))
img = Image.alpha_composite(img.convert('RGBA'), panel).convert('RGB')
img = img.filter(ImageFilter.GaussianBlur(0.5))
img.save(out, quality=92, optimize=True)
print(out, 'created')
