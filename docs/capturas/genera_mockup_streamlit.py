from PIL import Image, ImageDraw, ImageFont

# Crear imagen base
img = Image.new('RGB', (800, 500), color=(245, 245, 245))
draw = ImageDraw.Draw(img)

# Fuentes
try:
    font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 32)
    font_menu = ImageFont.truetype("DejaVuSans.ttf", 22)
    font_text = ImageFont.truetype("DejaVuSans.ttf", 18)
except:
    font_title = font_menu = font_text = None

# Título principal
draw.rectangle([0,0,800,60], fill=(33,150,243))
draw.text((20,15), "Secadores Solares - App Multipágina", fill=(255,255,255), font=font_title)

# Menú lateral
draw.rectangle([0,60,180,500], fill=(220,220,220))
draw.text((20,80), "Área de Colector\nMasa de Aire y Producto\nEficiencia y Rendimiento", fill=(33,150,243), font=font_menu)

# Ejemplo de página
x0, y0 = 200, 80
draw.text((x0, y0), "Área de Colector Solar", fill=(33,150,243), font=font_title)
draw.text((x0, y0+50), "Q = A · I · η · t · 3600", fill=(0,0,0), font=font_text)
draw.text((x0, y0+90), "Área necesaria del colector: 3.47 m²", fill=(0,0,0), font=font_text)

img.save("docs/capturas/ejemplo.png")
print("Mockup guardado en docs/capturas/ejemplo.png")
