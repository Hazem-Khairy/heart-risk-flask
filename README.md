#  Heart Risk Prediction App

A machine learning web application that predicts heart disease risk levels using a **LightGBM (LGBM)** model, deployed with **Flask** and containerized with **Docker**. CI/CD is handled via **Jenkins**, and the app is live on **Hugging Face Spaces**.

---

## 🚀 Live Demo

👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/Hazem-Khairy74/Heart-risk-app)

---

## 📌 Project Overview

This project predicts whether a person is at **low, medium, or high risk** of heart disease based on clinical and lifestyle features. The model achieves a **Recall of 0.98**, making it highly sensitive to detecting at-risk individuals — which is critical in a medical context.

---

## 🧠 Machine Learning

| Detail | Info |
|--------|------|
| Algorithm | LightGBM (LGBM) |
| Target | Heart Risk Level (Low / Medium / High) |
| Key Metric | Recall = **0.98** |
| Dataset | Custom synthetic dataset (generated) |
| Preprocessing | RobustScaler + OneHotEncoder |

- 📓 **Kaggle Notebook:** [Heart Risk Level — Recall 0.98](https://www.kaggle.com/code/hazemkhairy10/heart-risk-level-recall-0-98)
- 📊 **Dataset:** [Heart Risk Dataset on Kaggle](https://www.kaggle.com/datasets/hazemkhairy10/heart-risk-dataset)

---

## 🗂️ Project Structure

```
heart-risk-flask/
│
├── templates/
│   └── index.html          # Frontend UI
│
├── app.py                  # Flask application
├── lgbm_heart_model.pkl    # Trained LGBM model
├── onehot_encoder.pkl      # OneHot encoder for categorical features
├── robust_scaler.pkl       # RobustScaler for numerical features
├── heart_risk_dataset_v2.csv  # Dataset used for training
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker container config
└── Jenkinsfile             # CI/CD pipeline config
```

---

## ⚙️ Tech Stack

- **Machine Learning:** LightGBM, Scikit-learn, Pandas, NumPy
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Containerization:** Docker
- **CI/CD:** Jenkins
- **Deployment:** Hugging Face Spaces

---

## 🐳 Run with Docker

```bash
# Pull or build the image
docker build -t heart-risk-flask .

# Run the container
docker run -p 5000:5000 heart-risk-flask
```

Then open your browser at `http://localhost:5000`

---

## 🔧 Run Locally (without Docker)

```bash
# Clone the repository
git clone https://github.com/Hazem-Khairy/heart-risk-flask.git
cd heart-risk-flask

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

---

## 📈 CI/CD Pipeline (Jenkins)

The project uses a **Jenkinsfile** to automate:
1. Code checkout
2. Docker image build
3. Deployment

---

## 📬 Contact

**Hazem Khairy**
- GitHub: [@Hazem-Khairy](https://github.com/Hazem-Khairy)
- Kaggle: [@hazemkhairy10](https://www.kaggle.com/hazemkhairy10)

---

> ⭐ If you find this project useful, please consider giving it a star!
