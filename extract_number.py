import cv2
import pytesseract

# Configure path if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_plate(plate_image):
    text = pytesseract.image_to_string(plate_image, config='--psm 7')
    return text.strip()

if __name__ == "__main__":
    img = cv2.imread("sample_plate.jpg")  # Sample plate image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    extracted_text = extract_text_from_plate(gray)
    print("Extracted Number:", extracted_text)
