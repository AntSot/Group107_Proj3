import pytesseract
from PIL import Image
from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20160420T200137Z.602d58f64d6ac2cf.d8e7eca404d946f979b434e59caa856c178eb095')
"""
print('Languages: ', translate.langs)
print('Translate directions: ',translate.directions)
print('Detect language: ', translate.detect('hola'))
"""
print(pytesseract.image_to_string(Image.open('wifi.png')))

text = pytesseract.image_to_string(Image.open('wifi.png'))

print('Translate: ', translate.translate(text, 'en-es'))
