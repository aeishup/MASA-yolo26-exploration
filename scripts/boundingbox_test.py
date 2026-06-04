from ultralytics import YOLO
import cv2

model = YOLO("yolo26m.pt")  

results = model("https://ultralytics.com/images/bus.jpg", show=False)

for r in results:
    annotated = r.plot()  # returns BGR numpy array with boxes drawn
    cv2.imshow("YOLO Detection", annotated)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()