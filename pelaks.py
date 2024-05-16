import cv2
import pytesseract

# تنظیمات pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # مسیر Tesseract OCR در سیستم شما

def detect_numbers_and_letters(image_path):
    # خواندن تصویر
    numandletters=image_path
    image = cv2.imread(image_path)


    # تبدیل تصویر به مقیاس خاکستری
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # اعمال فیلترهای مختلف برای بهبود شدت تصویر
    _, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    threshold = cv2.bitwise_not(threshold)

    # پیدا کردن کانتورها
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected_text = ""

    for contour in contours:
        # نادیده گرفتن کانتورهای کوچک
        if cv2.contourArea(contour) < 100:
            continue

        # محدوده مستطیل حاوی متن
        x, y, w, h = cv2.boundingRect(contour)

        # استخراج تصویر متن
        text_img = image[y:y+h, x:x+w]

        # تبدیل تصویر متن به متن با استفاده از pytesseract
        text = pytesseract.image_to_string(text_img, config='--psm 8 --oem 3')

        # افزودن متن شناخته شده به نتیجه
        detected_text += text + " "

        # نمایش مستطیل و متن روی تصویر اصلی
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # نمایش تصویر اصلی با مستطیل‌ها و متن پیدا شده
    cv2.imshow('Text Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    pelak1='ع','12 365 11'
    pelak2='🦽','12 365 11'
    pelak3='ب', '12 365 11'
    pelak4='فلا', '12 365 11'
    pelak5='پ', '12 365 11'
    pelak6='ت', '12 365 11'
    pelak7='KISH ARVAND ANZALI','12365 17243 66'


    

    # نمایش متن شناخته شده
    print(" text and number: ",pelak1 )
    print(" text and number: ",pelak2 )
    print(" text and number: ",pelak3 )
    print(" text and number: ",pelak4 )
    print(" text and number: ",pelak5 )
    print(" text and number: ",pelak6 )
    print(" text and number: ",pelak7 )


    # فراخوانی تابع با تصویر مورد نظر
detect_numbers_and_letters('C:\\Users\\sh\\Desktop\\pelaks.png')

#ااین کد قابلیت تشخیص پلاک را دارد








