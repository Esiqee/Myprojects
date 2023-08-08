import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith((".png", ".jpg", ".jpeg")):
    sys.exit("Invalid input")
elif not sys.argv[2].lower().endswith((".png", ".jpg", ".jpeg")):
    sys.exit("Invalid output")
elif not sys.argv[1][-4:] == sys.argv[2][-4:]:
    sys.exit("Input and output have different extensions")


try:
    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    output = ImageOps.fit(image, size)
    output.paste(shirt, shirt)
    output.save(sys.argv[2])

except FileNotFoundError:
    sys.exit(f"Input does not exist")


