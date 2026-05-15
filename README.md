# Quantum-Enhanced Swin Transformer for Multi-Class Retinal Disease Classification Using OCT Images

This project presents a deep learning-based system for multi-class retinal disease classification using Optical Coherence Tomography (OCT) images. The goal is to assist in early and accurate diagnosis of retinal diseases using Swin Transformer and Quantum-enhanced deep learning techniques.

## 🧠 Overview

Retinal diseases can cause severe vision impairment if not diagnosed early. OCT imaging provides high-resolution retinal scans that help detect abnormalities effectively. This project focuses on:

- Classifying multiple retinal diseases using OCT images.
- Extracting deep image features using Swin Transformer architecture.
- Applying Quantum-enhanced learning techniques for improved performance.
- Building a Flask web application for real-time retinal disease prediction.
- Providing an automated and efficient diagnosis support system.

## 📁 Dataset

Dataset Link: https://www.kaggle.com/datasets/obulisainaren/retinal-oct-c8

The dataset contains OCT retinal images categorized into multiple retinal disease classes.

### Disease Classes Include:

- AMD — Age-related Macular Degeneration  
- CNV — Choroidal Neovascularization  
- CSR — Central Serous Retinopathy  
- DME — Diabetic Macular Edema  
- DR — Diabetic Retinopathy  
- DRUSEN — Yellow deposits under the retina  
- MH — Macular Hole  
- NORMAL — Healthy eyes with no abnormalities  

## 🛠️ Tools & Libraries

- Python
- Flask
- TensorFlow / Keras
- PyTorch
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Swin Transformer
- Scikit-learn

## 🔍 Image Processing & Feature Extraction

The project performs:

- OCT image preprocessing
- Image resizing and normalization
- Data augmentation
- Deep feature extraction using Swin Transformer
- Quantum-enhanced feature optimization

## 🧪 Model Training

### Models Used:
- Baseline Swin Transformer
- Quantum-Enhanced Swin Transformer

### Training Techniques:
- Transfer Learning
- Data Augmentation
- Multi-class Classification
- Hyperparameter Optimization

### Performance Metrics:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 📈 Results

- Quantum-enhanced model achieved improved classification performance compared to baseline models.
- Better feature representation and classification accuracy on OCT retinal images.
- Efficient multi-class retinal disease prediction.

## 🌐 Web Interface (Flask App)

The Flask web application allows users to:

- Upload OCT retinal images
- Perform real-time disease prediction
- Display predicted retinal disease category
- Provide a simple and user-friendly interface for diagnosis support

## 🚀 Future Enhancements

- Cloud deployment integration
- Real-time hospital diagnosis support
- Explainable AI visualization
- Mobile application integration
- Advanced quantum optimization techniques

## 📂 Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── static/
├── templates/
└── README.md
```

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/KothaTeja/Quantum-Enhanced-Swin-Transformer-for-Multi-Class-Retinal-Disease-Classification-Using-OCT-Images.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
python app.py
```
