import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow("Kontrol Paneli")

def nothing(x):
    pass

cv2.createTrackbar("H Min", "Kontrol Paneli", 0, 179, nothing)
cv2.createTrackbar("H Max", "Kontrol Paneli", 179, 179, nothing)
cv2.createTrackbar("S Min", "Kontrol Paneli", 0, 255, nothing)
cv2.createTrackbar("S Max", "Kontrol Paneli", 255, 255, nothing)
cv2.createTrackbar("V Min", "Kontrol Paneli", 0, 255, nothing)
cv2.createTrackbar("V Max", "Kontrol Paneli", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("H Min", "Kontrol Paneli")
    h_max = cv2.getTrackbarPos("H Max", "Kontrol Paneli")
    s_min = cv2.getTrackbarPos("S Min", "Kontrol Paneli")
    s_max = cv2.getTrackbarPos("S Max", "Kontrol Paneli")
    v_min = cv2.getTrackbarPos("V Min", "Kontrol Paneli")
    v_max = cv2.getTrackbarPos("V Max", "Kontrol Paneli")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Orijinal Goruntu", frame)
    cv2.imshow("Maske", mask)
    cv2.imshow("Renk Takibi", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()