import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    center_x = width // 2
    center_y = height // 2

    half_size = 100
    x1 = center_x - half_size
    x2 = center_x + half_size
    y1 = center_y - half_size
    y2 = center_y + half_size

    roi = frame[y1:y2, x1:x2]

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    gray_roi_bgr = cv2.cvtColor(gray_roi, cv2.COLOR_GRAY2BGR)

    frame[y1:y2, x1:x2] = gray_roi_bgr

    cv2.imshow("ROI Grayscale", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()