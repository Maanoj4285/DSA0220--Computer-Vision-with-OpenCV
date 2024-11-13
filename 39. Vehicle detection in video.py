import cv2

vehicle_cascade = cv2.CascadeClassifier('cars.xml')

video = cv2.VideoCapture('vehicle_video.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Vehicle Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
video.release()
cv2.destroyAllWindows()
