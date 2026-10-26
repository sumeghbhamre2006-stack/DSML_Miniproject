# Credit Risk Prediction - Training Script
# Trains 3 models (Logistic Regression, Decision Tree, Random Forest),
# compares them, and saves the models for the GUI.

import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# ---------- 1. Load data ----------
cols = ['loan_amnt', 'term', 'int_rate', 'grade', 'emp_length', 'home_ownership',
        'annual_inc', 'purpose', 'dti', 'fico_range_low', 'loan_status']
df = pd.read_csv('accepted_2007_to_2018Q4.csv', usecols=cols, nrows=100000)

# ---------- 2. Preprocessing ----------
# Keep only finished loans. Default = 1, Fully Paid = 0
df = df[df['loan_status'].isin(['Fully Paid', 'Charged Off'])]
df['default'] = (df['loan_status'] == 'Charged Off').astype(int)
df = df.drop(columns=['loan_status'])

# Convert text to numbers
df['term'] = df['term'].str.extract(r'(\d+)').astype(int)
df['emp_length'] = df['emp_length'].str.extract(r'(\d+)').astype(float)
df['grade'] = df['grade'].map({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7})

# Fill missing values
df['emp_length'] = df['emp_length'].fillna(0)
df['dti'] = df['dti'].fillna(df['dti'].median())

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=['home_ownership', 'purpose'])

X = df.drop(columns=['default'])
y = df['default']
print("Data shape:", X.shape, "| Default rate: %.2f%%" % (y.mean() * 100))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# ---------- 3. Models ----------
# class_weight='balanced' because defaults are fewer than paid loans
models = {
    'Logistic Regression': LogisticRegression(max_iter=5000, class_weight='balanced'),
    'Decision Tree': DecisionTreeClassifier(max_depth=10, class_weight='balanced', random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10, class_weight='balanced', random_state=42),
}

# ---------- 4. Train & evaluate ----------
results = []
for name, model in models.items():
    model.fit(X_train_s, y_train)
    pred = model.predict(X_test_s)
    prob = model.predict_proba(X_test_s)[:, 1]
    results.append([name,
                    accuracy_score(y_test, pred),
                    precision_score(y_test, pred),
                    recall_score(y_test, pred),
                    f1_score(y_test, pred),
                    roc_auc_score(y_test, prob)])

results = pd.DataFrame(results, columns=['Model', 'Accuracy', 'Precision', 'Recall', 'F1', 'ROC-AUC']).round(3)
print("\n", results.to_string(index=False))

# ---------- 5. Comparison chart ----------
results.set_index('Model').plot(kind='bar', figsize=(9, 5))
plt.title('Model Comparison')
plt.ylabel('Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('comparison.png')

# ---------- 6. Save ----------
pickle.dump({'models': models, 'scaler': scaler, 'columns': list(X.columns),
             'results': results}, open('model.pkl', 'wb'))
print("\nSaved model.pkl and comparison.png")
