# FaceMaskDetection
# 😷 Face Mask Detection using CNN

 Direct Link: https://facemaskdetection-cqgc3avc6hnnuja9x4accu.streamlit.app/

## 📌 Overview

This project is a deep learning-based application that detects whether a person is wearing a face mask or not using a Convolutional Neural Network (CNN). The model is trained on image data and deployed using Streamlit for an interactive web interface.

---

## 🚀 Features

* Image-based face mask detection (Mask / No Mask)
* Deep learning model using CNN
* User-friendly interface built with Streamlit
* Real-time prediction on uploaded images

---

## 🧰 Tech Stack

* Python
* TensorFlow (CNN Model)
* OpenCV (Image processing)
* Streamlit (Web deployment)

---

## 📂 Dataset

* Face Mask Dataset from Kaggle
* Contains images categorized into:

  * `with_mask`
  * `without_mask`

⚠️ Dataset is not included in this repository due to size limitations.

---

## ⚙️ How It Works

1. Images are preprocessed (resized, normalized)
2. CNN model is trained on labeled data
3. Model is saved as `mask_detector.h5`
4. Streamlit app loads the model
5. User uploads image → prediction shown

---

## ▶️ How to Run the Project

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd FaceMaskDetection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

## 📊 Results

* Achieved high accuracy on validation dataset
* Successfully classifies images as:

  * 😷 Mask
  * ❌ No Mask

---

## 📁 Project Structure

```
FaceMaskDetection/
 ├── app.py
 ├── train.py
 ├── mask_detector.h5
 ├── requirements.txt
 └── README.md
```

---

## 📌 Future Improvements

* Add real-time webcam detection
* Improve model accuracy with larger dataset
* Deploy using cloud platforms

---

## 🌐 Deployment

This project can be deployed using Streamlit Community Cloud.

---

## 👨‍💻 Author

Komal Saini
