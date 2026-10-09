<div align="center">

# 🙂 Face Recognition Login System

**A desktop app that registers users by face and logs them in through the webcam.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-informational)
![face_recognition](https://img.shields.io/badge/face__recognition-dlib-orange)

</div>

---

## ✨ Features

- 🪟 **Tkinter GUI** with a live webcam preview and **Login** / **Register** buttons.
- ➕ **Register** - capture a face, enter a name and save it to the local `./db` folder.
- 🔓 **Login** - compares the current webcam frame with the registered faces using the [`face_recognition`](https://github.com/ageitgey/face_recognition) library and greets the matched user.
- 🧾 **Access log** - successful logins are appended to `log.txt`.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A webcam
- `face_recognition` requires `dlib` (CMake and a C++ compiler on most systems)

### Install & run

```bash
git clone https://github.com/Arashomranpour/face_recognition.git
cd face_recognition
pip install opencv-python pillow numpy face_recognition
python main.py
```

## 📁 Project Structure

```
.
├── main.py        # App window, webcam, register/login logic
└── utility.py     # Tkinter helpers (buttons, labels, message boxes)
```

> The `./db` folder (registered faces) and `log.txt` are created at runtime.

## 🛠️ Tech Stack

`Tkinter` · `OpenCV` · `face_recognition` · `Pillow` · `NumPy`
