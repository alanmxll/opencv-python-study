import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# cap.set(4, 1208)
# cap.set(5, 720)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f'Width: {cap.get(4)} Height: {cap.get(5)}'
        datet = str(datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break

cap.release()
cv2.destroyAllWindows()
