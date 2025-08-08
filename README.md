
# 🩺 Diabetes Predictor AI Web App

An end-to-end machine learning web application that predicts the risk of diabetes based on health metrics. Built using Python, Flask, and scikit-learn.

![App Screenshot]<img width="1037" height="645" alt="Screenshot 2025-08-08 203321" src="https://github.com/user-attachments/assets/935ec60c-696c-414e-a31d-d78712d230a9" />


---

## 🚀 Live Demo

🔗 Comming Soon

---

## 📌 Features

- Predicts diabetes risk (High / Low)
- Built using GradientBoostingClassifier with hyperparameter tuning
- Clean and modern Bootstrap UI
- Input validation (both frontend and backend)
- Trained on the PIMA Indian Diabetes dataset
- Feature scaling and data cleaning implemented
- Professional project folder structure

---

## 🧠 Tech Stack

- Python 3.7+
- Flask
- HTML/CSS (Bootstrap)
- scikit-learn
- XGBoost
- pandas, numpy, seaborn
- Render (for deployment)

---

## 📁 Folder Structure

```
diabetes_app/
├── app.py
├── model/
│   └── Diabetes_Model1.pkl
│   └── scaler.pkl
├── templates/
│   └── Diabetes_App.html
├── static/
│   └── styles.css (optional)
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation (Local)

```bash
git clone https://github.com/your-username/diabetes-predictor-app.git
cd diabetes_app
pip install -r requirements.txt
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## 📝 Model Training Summary

- Trained on PIMA Indians Diabetes Dataset (Kaggle)
- Handled zero-value outliers using imputation
- Applied StandardScaler for feature normalization
- Trained and tuned GradientBoosting and XGBoost
- Final model: GradientBoostingClassifier
- Accuracy: ~85% (depending on tuning)

---

## 👤 Author

**Sumit Bavaskar**  
📧 Contact: [LinkedIn](https://linkedin.com/in/sumitbavaskar)  
📂 Portfolio: Coming Soon

---

## 📜 License

Licensed under the Apache License 2.0.
