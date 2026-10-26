# Credit Risk Prediction System for FinTech Lending Platforms

An end-to-end Machine Learning mini project designed to evaluate loan applicant demographic and financial indicators, predict default probabilities, and assist credit underwriters in making objective, data-driven loan decisions.

---

## 📌 Problem Statement
FinTech lending platforms need reliable risk assessment systems to distinguish creditworthy borrowers from potential defaulters. Traditional static scorecard systems are rigid and cannot capture non-linear feature interactions. This project implements and benchmarks three supervised machine learning algorithms on real-world lending records, handling heavy class imbalance and providing an intuitive graphical user interface (GUI) for real-time predictions.

---

## 🚀 Key Features
- **Data Preprocessing**: Regex parsing of loan terms and employment tenure, missing value imputation, one-hot categorical encoding, and feature standardization with `StandardScaler`.
- **Class Imbalance Handling**: Cost-sensitive balanced class weighting (`class_weight='balanced'`) to prioritize catching defaulting loans (Recall).
- **Multi-Algorithm Comparison**: Trains and evaluates:
  1. Logistic Regression
  2. Decision Tree Classifier
  3. Random Forest Classifier
- **Dual GUI Support**:
  - **Streamlit Web Application (`app.py`)**: Interactive browser dashboard with live probability scoring, dynamic risk tiers (Low/Medium/High Risk), and comparison charts.
  - **Tkinter Desktop Interface (`gui.py`)**: Lightweight native desktop GUI.

---

## 📊 Dataset
- **Source**: [LendingClub Loan Dataset](https://www.kaggle.com/datasets/wordsforthewise/lending-club) (`accepted_2007_to_2018Q4.csv`)
- **Target**: `default` (Derived: `Charged Off` = 1, `Fully Paid` = 0)
- **Key Features**:
  - `loan_amnt`: Sanctioned principal amount ($)
  - `term`: Repayment duration (36 or 60 months)
  - `int_rate`: Interest rate (%)
  - `grade`: Credit rating tier (A to G)
  - `emp_length`: Employment tenure (years)
  - `home_ownership`: RENT, MORTGAGE, OWN
  - `annual_inc`: Borrower gross annual income ($)
  - `purpose`: Debt consolidation, small business, etc.
  - `dti`: Debt-to-Income ratio
  - `fico_range_low`: Bureau FICO score

---

## 📈 Model Performance Comparison

Evaluated on held-out test data (20% split, 17,578 loans):

| Algorithm | Accuracy | Precision | Recall (Defaulters) | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 0.682 | 0.342 | 0.637 | 0.445 | 0.728 |
| **Decision Tree** | 0.662 | 0.329 | 0.664 | 0.440 | 0.725 |
| **Random Forest Classifier** | **0.667** | **0.335** | **0.668** | **0.446** | **0.732** |

> **Note**: Cost-sensitive class balancing is intentionally enabled to achieve high Recall (~67%), minimizing false negatives (unnoticed bad loans) at the acceptable expense of requiring secondary review for false positives.

---

## 🛠️ Project Structure
```text
├── train.py                    # Data preprocessing, model training & evaluation
├── app.py                      # Interactive Streamlit Web GUI
├── gui.py                      # Lightweight Tkinter Desktop GUI
├── generate_full_report.py     # Script to generate documentation/reports
├── comparison.png              # Benchmark chart comparing model metrics
├── performance_comparison.png  # Detailed multi-metric visualization chart
├── model.pkl                   # Serialized models, scaler, and metadata
├── .gitignore                  # Git ignore rules (excludes venv and 1.6GB CSV)
└── README.md                   # Project documentation
```

---

## 💻 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sumeghbhamre2006-stack/DSML_Miniproject.git
cd DSML_Miniproject
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install scikit-learn pandas streamlit matplotlib
```

### 3. Dataset Setup
Download `accepted_2007_to_2018Q4.csv` from [Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club) and place it in the root project directory.

### 4. Train Models
```bash
python3 train.py
```
*Generates `model.pkl` and `comparison.png`.*

### 5. Run User Interface
- **Streamlit Web UI (Recommended)**:
  ```bash
  streamlit run app.py
  ```
- **Tkinter Desktop UI**:
  ```bash
  python3 gui.py
  ```

---

## 🎯 Sustainable Development Goals (SDG)
- **SDG 8 (Decent Work & Economic Growth - Target 8.10)**: Expanding access to banking and financial services responsibly through automated credit assessment.
- **SDG 9 (Industry, Innovation & Infrastructure)**: Fostering FinTech innovation in credit risk management.
