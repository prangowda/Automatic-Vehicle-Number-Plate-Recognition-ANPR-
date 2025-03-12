import cv2

# Load pre-trained Haar cascade for number plate detection
plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

def detect_number_plate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in plates:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        plate = gray[y:y + h, x:x + w]
        return plate
    
    return None

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)  # Open webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        plate_img = detect_number_plate(frame)
        cv2.imshow("Vehicle Number Plate Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
