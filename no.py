import pyautogui
import pyscreenshot
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

while(True):
    pic = pyscreenshot.grab(bbox=(1330,140,1500,210))

    text = pytesseract.image_to_string(pic)
    print(text)

    number = text.partition('\n')[0]
    number = number.replace(" ", "")
    number = number.replace("a", "0")
    number = number.replace("e", "0")
    try:
        if(int(number[0:len(number) - 1]) < 30000 and number[len(number) - 1: len(number)].lower() == "p"):
            pyautogui.dragTo(1800, 170)
            pyautogui.click(1800, 170)
            pyautogui.dragTo(880, 590)
    except:
        print("error")

    pyautogui.dragTo(1835, 120)
    pyautogui.click(1835, 120)

    time.sleep(1)
