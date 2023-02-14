import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = "./bill1.jpg"

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

rect_kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

dialation = cv2.dilate(thresh1, rect_kernal, iterations= 1)

# find countours
countours, hierarchy = cv2.findContours(dialation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

duplicate_image = image.copy()

with open('data.txt', "w+") as f:
    f.write("")
    f.close()

for i in countours:
    x, y, w, h = cv2.boundingRect(i)

    rect = cv2.rectangle(duplicate_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    croppedimage = duplicate_image[y:y + h, x:x + w]

    with open('data.txt', "a") as f:
        text = pytesseract.image_to_string(croppedimage)
        if text:
            f.write(text)
            f.write('\n')
            f.close()
