# 🧠 Real-Time Face Recognition System
This is a real-time face recognition system using OpenCV, FaceNet, and SVM. It detects faces from a webcam, extracts embeddings, and classifies them using a trained model. The project is Dockerized for easy setup and is suitable for applications like security and attendance systems.

---

## 🚀 Features

* Real-time face detection using OpenCV
* Face embedding extraction via **FaceNet** (`keras-facenet`)
* Face classification using pre-trained **SVM**
* Pre-computed face embeddings for fast execution
* Cross-platform deployment using **Docker**

---

## 🛠️ Technologies Used

* Python 3.9
* OpenCV
* keras-facenet
* scikit-learn
* NumPy, Pillow
* Docker (for containerization)

---

## 📁 Project Structure

```
.
├── main.py                        # Main application script
├── haarcascade_frontalface_default.xml  # Face detector
├── faces_embeddings_done_4classes.npz   # Embeddings for 4 known classes
├── svm_model_160x160.pkl          # Pre-trained SVM classifier
├── requirements.txt               # Python dependencies
└── Dockerfile                     # Container setup
```

---

## 🧪 How It Works

1. Capture frame from webcam
2. Detect faces using Haar cascades
3. Extract 128-dimensional embedding using FaceNet
4. Classify identity with SVM model
5. Display the label over the detected face

---

## 🐳 Run with Docker

```bash
# Build the Docker image
docker build -t face-recognition-app .

# Run the app (Linux: ensure webcam is accessible)
docker run --rm -it --device=/dev/video0 face-recognition-app
```

> ⚠️ For Windows/macOS: use a virtual camera or adjust Docker settings for webcam access.

---

## 📝 Future Improvements

* Add support for dynamic face registration
* Improve UI (e.g., add web interface or GUI)
* Support face logging and unknown face detection
* Integrate alert systems or logging for security applications


