# Credit Risk Prediction - GUI (run train.py first)

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import pickle

data = pickle.load(open('model.pkl', 'rb'))
models, scaler, columns, results = data['models'], data['scaler'], data['columns'], data['results']

root = tk.Tk()
root.title("Credit Risk Prediction System")

# ---------- Input fields ----------
fields = {}
numeric = [('Loan Amount ($)', 'loan_amnt', '10000'),
           ('Interest Rate (%)', 'int_rate', '12.5'),
           ('Annual Income ($)', 'annual_inc', '60000'),
           ('Debt-to-Income Ratio', 'dti', '15'),
           ('FICO Score', 'fico_range_low', '700'),
           ('Employment Length (yrs)', 'emp_length', '5')]
choices = [('Term (months)', 'term', ['36', '60']),
           ('Grade', 'grade', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
           ('Home Ownership', 'home_ownership', ['RENT', 'MORTGAGE', 'OWN']),
           ('Purpose', 'purpose', sorted(c.replace('purpose_', '') for c in columns if c.startswith('purpose_'))),
           ('Model', 'model', list(models.keys()))]

row = 0
for label, key, default in numeric:
    tk.Label(root, text=label).grid(row=row, column=0, sticky='w', padx=10, pady=3)
    e = tk.Entry(root)
    e.insert(0, default)
    e.grid(row=row, column=1, padx=10)
    fields[key] = e
    row += 1
for label, key, opts in choices:
    tk.Label(root, text=label).grid(row=row, column=0, sticky='w', padx=10, pady=3)
    cb = ttk.Combobox(root, values=opts, state='readonly')
    cb.current(0)
    cb.grid(row=row, column=1, padx=10)
    fields[key] = cb
    row += 1


# ---------- Prediction ----------
def predict():
    try:
        x = dict.fromkeys(columns, 0)
        for _, key, _ in numeric:
            x[key] = float(fields[key].get())
        x['term'] = int(fields['term'].get())
        x['grade'] = 'ABCDEFG'.index(fields['grade'].get()) + 1
        x['home_ownership_' + fields['home_ownership'].get()] = 1
        x['purpose_' + fields['purpose'].get()] = 1
        X = scaler.transform(pd.DataFrame([x])[columns])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    prob = models[fields['model'].get()].predict_proba(X)[0][1]
    if prob < 0.4:
        text, color = "LOW RISK - Approve Loan", "green"
    elif prob < 0.6:
        text, color = "MEDIUM RISK - Review Carefully", "orange"
    else:
        text, color = "HIGH RISK - Reject Loan", "red"
    result.config(text=f"Default Probability: {prob*100:.1f}%\n{text}", fg=color)


tk.Button(root, text="Predict Risk", command=predict, bg='lightblue').grid(row=row, column=0, columnspan=2, pady=10)
result = tk.Label(root, text="", font=('Arial', 14, 'bold'))
result.grid(row=row + 1, column=0, columnspan=2, pady=5)

# ---------- Model comparison table ----------
tk.Label(root, text="Model Performance Comparison", font=('Arial', 11, 'bold')).grid(row=row + 2, column=0, columnspan=2)
tk.Label(root, text=results.to_string(index=False), font=('Courier', 10), justify='left').grid(
    row=row + 3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
