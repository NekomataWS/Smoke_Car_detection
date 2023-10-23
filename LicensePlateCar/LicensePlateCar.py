from PIL import Image
import pytesseract

image_path = 'LicensePlateCar/ThaiLicense1.jpg'
image = Image.open(image_path)

# Perform OCR and specify the language ('tha' for Thai)
text = pytesseract.image_to_string(image, lang='tha')
print(text)
