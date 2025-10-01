# 🚨 Network Intrusion Detection System (NIDS)

This project implements a **Network Intrusion Detection System** using **Machine Learning** techniques.  
It is designed to classify network traffic as **normal** or **malicious** based on extracted features, helping in early detection of cyber threats.

The project is built and tested in **Jupyter Notebook (`Network_Intrusion_Detection.ipynb`)** and can be extended into production-ready applications.

---

## 📂 Project Structure

├── Network_Intrusion_Detection.ipynb # Main Jupyter Notebook with code

├── dataset/ # Network intrusion dataset (Train_)

├── models/ # Trained ML models (pickle files)

├── requirements.txt # Required dependencies

└── README.md # Project documentation


---

## ⚙️ Features

- Data preprocessing & feature selection
- Handling categorical and numerical features
- Training multiple ML models:
  - Logistic Regression  
  - Decision Tree  
  - Random Forest  
  - Gradient Boosting  
  - XGBoost, LightGBM, CatBoost  
  - SVM, KNN, Naive Bayes  
  - Ensemble methods (Voting, Bagging, Stacking, AdaBoost)
- Model evaluation with:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix
- Export trained models as `.pkl` using `pickle`
- (Optional) Streamlit-based GUI for real-time detection

---

## 📊 Dataset

The dataset contains **network traffic records** with features such as:

- `protocol_type`  
- `service`  
- `flag`  
- `src_bytes`  
- `dst_bytes`  
- `count`, `srv_count`  
- ... and many more  

The target variable is:
- `normal` → Safe traffic  
- `attack` → Malicious activity  

*(You can use NSL-KDD, CICIDS2017, or any other intrusion dataset.)*

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```bash


https://github.com/Amanpandit87/Network_intrusion_Detection
