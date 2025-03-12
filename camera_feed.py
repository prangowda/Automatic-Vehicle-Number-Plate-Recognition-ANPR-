import cv2
import pytesseract

plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

def detect_and_extract_text(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        plate_img = gray[y:y+h, x:x+w]
        plate_text = pytesseract.image_to_string(plate_img, config='--psm 7')
        print(f"Detected Number Plate: {plate_text.strip()}")

    return frame

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detect_and_extract_text(frame)
        cv2.imshow("Vehicle Number Plate Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
