# YOLO26 Exploration

Exploring YOLO-based object detection as an alternative to classical OpenCV 
contour detection in the context of a medical imaging ML pipeline (MASA).

Focused on learning and experimenting with the Ultralytics YOLO pipeline — 
inference, visualization, and dataset preparation for potential custom training.

---

## Objectives
- Understand how YOLO performs detection on real images
- Compare learned detection (YOLO) vs classical OpenCV contour approaches
- Experiment with inference, bounding box visualization, and model outputs
- Build a foundation for future MASA-related computer vision work

---

## Setup
```bash
pip install ultralytics opencv-python
```

---

## Usage
Run all scripts from the project root:
```bash
python scripts/boundingbox_test.py
python scripts/webcam_test.py
```

---

## Models
Place model weights in `models/`. Not committed to git.
- `yolo26n.pt` / `yolo26m.pt` — download from [Ultralytics](https://github.com/ultralytics/ultralytics)

---

## License
Licensed under AGPL-3.0 in compliance with the [Ultralytics YOLO license](https://github.com/ultralytics/ultralytics/blob/main/LICENSE).