from PIL import Image
import pytesseract
import cv2

def captchaSolver():
    img = Image.open('uims_api/assets/ss.png')

    x = 406
    y = 400
    width = 60
    height = 32
    captcha = img.crop((x, y, x+width, y+height))
    captcha.save('uims_api/assets/captcha.png')

    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    captcha = cv2.imread("uims_api/assets/captcha.png")
    captcha = cv2.resize(captcha, (width*4, height*4))
    captcha = cv2.cvtColor(captcha, cv2.COLOR_BGR2RGB)
    captcha_pil = Image.fromarray(captcha)
    gray = captcha_pil.convert('L')
    gray.save('uims_api/assets/captcha_gray.png')
    bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
    bw.save('uims_api/assets/captcha_thresholded.png')
    captcha_text = pytesseract.image_to_string(
        bw, lang='eng')
    return captcha_text


