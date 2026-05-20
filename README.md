# 🧠 End-to-End HR Analytics Platform

> A complete data science project that simulates a real-world HR intelligence system — from raw messy data to a live machine learning web application.

---

## 📌 Project Overview

This project tackles a real HR business problem: **predicting which employees are likely to be promoted**, enabling data-driven workforce decisions. The solution covers the full data science lifecycle — data preprocessing, exploratory analysis, feature engineering, machine learning modeling, BI reporting, and model deployment.

---

## 🗂️ Dataset

| Property | Details |
|---|---|
| Source | Real-world HR employee dataset |
| Records | ~17,400 employees |
| Features | 13 columns (department, age, KPIs, training score, ratings, etc.) |
| Target | Employee promotion prediction |
| Challenge | Class imbalance, missing values, outliers |

---

## ⚙️ Project Pipeline

### 1. Data Preprocessing
- Handled missing values using mode and median imputation
- Removed duplicate records
- Detected and treated outliers using the **IQR method**
- Standardized data types and column formats

### 2. Exploratory Data Analysis (EDA)
- Generated **10+ visualizations** using Matplotlib, Seaborn, and Plotly
- Analyzed distributions, correlations, and class imbalance
- Visualized KPI achievement rates, training scores, gender and department breakdowns, and recruitment channel performance
- Uncovered key patterns driving employee promotion

### 3. Feature Engineering & Data Normalization
- Engineered 2 new features:
  - `is_senior_employee` — flags long-tenure employees
  - `training_level` — categorizes training score into Low / Medium / High
- Normalized the dataset into **5 relational CSV tables**:
  - `employees_table`, `departments_table`, `performance_table`, `salaries_table`, `promotions`
- Loaded and queried tables using **SQL Server** (`HR_Analytics` database)

### 4. Machine Learning Model
- **Algorithm:** Logistic Regression
- **Class Imbalance:** Handled using **SMOTE** (Synthetic Minority Oversampling Technique)
- **Dimensionality Reduction:** PCA
- **Feature Scaling:** StandardScaler
- **Evaluation Metrics:**
  - Accuracy 98%
  - Classification Report (Precision, Recall, F1-score)
  - **5-Fold Cross-Validation**
  - **ROC-AUC Score**

### 5. Power BI Dashboard
- Built an interactive dashboard with **DAX measures** and dynamic slicers
- KPIs visualized: promotion rates, average training scores, rating distributions, department comparisons, gender breakdown, recruitment channel analysis

### 6. Streamlit Web App (Deployment)
- Deployed the trained model as a **live interactive web application**
- Accepts 13 employee features as input
- Returns **real-time promotion probability**
- Hosted via **Cloudflare tunnel** from Google Colab

---

## 🏆 Key Highlights

- ✅ Real dataset with 17,400+ employee records
- ✅ Full ETL pipeline from raw CSV to normalized SQL Server schema
- ✅ Class imbalance solved with SMOTE
- ✅ Model validated with cross-validation and ROC-AUC
- ✅ Interactive Power BI dashboard for business stakeholders
- ✅ Live Streamlit app — not just a notebook

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | scikit-learn, imbalanced-learn (SMOTE) |
| Database | SQL Server, T-SQL |
| BI Reporting | Power BI, DAX |
| Deployment | Streamlit, Cloudflare Tunnel |
| Environment | Google Colab, Jupyter Notebook |

---

## 📁 Project Structure

```
End-to-End HR Analytics Platform/
│
├── HR_Analytics_Platform.ipynb          # Main notebook (EDA + ML pipeline)
├── HR.pbix                              # Power BI dashboard
├── SQLQuery1.sql                        # SQL Server schema & queries
│
├── Uncleaned_employees_final_dataset.csv  # Raw input data
├── employees_table.csv                  # Normalized employees table
├── departments_table.csv                # Normalized departments table
├── performance_table.csv                # Normalized performance table
├── salaries_table.csv                   # Normalized salaries table
└── promotions.csv                       # Normalized promotions table
```

---

## 🚀 How to Run

1. **Clone the repo**
```bash
git clone https://github.com/nouralaa311/End-to-End-HR-Analytics-Platform.git
cd End-to-End-HR-Analytics-Platform
```

2. **Install dependencies**
```bash
pip install pandas numpy scikit-learn imbalanced-learn matplotlib seaborn plotly streamlit joblib
```

3. **Open the notebook**
```bash
jupyter notebook HR_Analytics_Platform.ipynb
```

4. **Run the Streamlit app** *(inside the notebook — Cloudflare tunnel section)*
```bash
streamlit run app.py
```

---
