from ultralytics import solutions

# Launch Ultralytics' built-in Streamlit inference interface,
# pre-loaded with MASA's fine-tuned YOLO26m weights.
inf = solutions.Inference(model="weights/best.pt")
inf.inference()

# Run this file with:
#   streamlit run scripts/streamlit_app.py
# NOT with plain `python`.
