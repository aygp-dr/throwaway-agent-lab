from PIL import Image, ImageDraw, ImageFilter

# Create a blank image
img = Image.new('RGB', (200, 200), color = 'red')
d = ImageDraw.Draw(img)
d.text((20,20), "Hello World", fill=(255,255,0))

# Apply filter
blurred = img.filter(ImageFilter.GaussianBlur(5))

blurred.save("/output/blurred.png")
