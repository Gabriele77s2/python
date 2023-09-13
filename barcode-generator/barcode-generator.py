import barcode
from barcode import generate
from barcode.writer import ImageWriter

text = input("Enter text to encode: ")
code = barcode.get_barcode_class("code128")
code_image = generate("code128", text, writer=ImageWriter(), output="barcode")
print("Barcode generated and saved as 'barcode.png'")
