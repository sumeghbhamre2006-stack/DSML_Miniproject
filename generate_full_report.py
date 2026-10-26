import base64
import subprocess
import os

with open('image_16.jpg', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

chart_b64 = ""
if os.path.exists('performance_comparison.png'):
    with open('performance_comparison.png', 'rb') as f:
        chart_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DSML Mini Project Report</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 2.2cm 2.0cm 2.2cm 2.0cm;
  }}
  body {{
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #111;
    margin: 0;
    padding: 0;
  }}
  .page-break {{
    page-break-before: always;
    break-before: page;
  }}
  .header-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 8px;
    border-bottom: 2px solid #000;
    padding-bottom: 6px;
  }}
  .header-table td {{
    vertical-align: middle;
    border: none;
    padding: 2px;
  }}
  .logo-cell {{
    width: 80px;
    text-align: center;
  }}
  .logo-img {{
    width: 70px;
    height: auto;
  }}
  .college-title {{
    font-size: 13.5pt;
    font-weight: bold;
    text-align: center;
    color: #8b0000;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .college-sub {{
    font-size: 9.5pt;
    text-align: center;
    color: #333;
    line-height: 1.3;
  }}
  .dept-header {{
    text-align: center;
    font-size: 12.5pt;
    font-weight: bold;
    margin-top: 15px;
    letter-spacing: 0.5px;
    text-decoration: underline;
  }}
  .report-main-title {{
    text-align: center;
    font-size: 17pt;
    font-weight: bold;
    margin: 25px 0 15px 0;
    color: #1a2a4b;
    line-height: 1.3;
  }}
  .academic-session {{
    text-align: center;
    font-size: 12pt;
    font-style: italic;
    margin-bottom: 30px;
  }}
  .title-page-table {{
    width: 100%;
    margin-top: 40px;
    border-collapse: collapse;
  }}
  .title-page-table td {{
    border: none;
    vertical-align: top;
    font-size: 11.5pt;
  }}
  h1 {{
    font-size: 14pt;
    font-weight: bold;
    border-bottom: 1.5px solid #2b4c7e;
    padding-bottom: 4px;
    margin-top: 22px;
    margin-bottom: 10px;
    color: #2b4c7e;
    text-transform: uppercase;
  }}
  h2 {{
    font-size: 12.5pt;
    font-weight: bold;
    margin-top: 14px;
    margin-bottom: 6px;
    color: #333;
  }}
  p {{
    text-align: justify;
    margin-bottom: 10px;
    margin-top: 0;
  }}
  ul, ol {{
    margin-top: 4px;
    margin-bottom: 12px;
    padding-left: 24px;
  }}
  li {{
    margin-bottom: 5px;
    text-align: justify;
  }}
  .data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 18px 0;
  }}
  .data-table th, .data-table td {{
    border: 1px solid #333;
    padding: 7px 10px;
    font-size: 11pt;
    text-align: left;
  }}
  .data-table th {{
    background-color: #f2f5f9;
    font-weight: bold;
    text-align: center;
  }}
  .center-cell {{
    text-align: center;
  }}
  .figure-box {{
    text-align: center;
    margin: 18px 0;
  }}
  .figure-box img {{
    max-width: 90%;
    border: 1px solid #ddd;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  }}
  .figure-caption {{
    font-size: 10.5pt;
    font-style: italic;
    margin-top: 6px;
    color: #444;
  }}
  .code-block {{
    background-color: #f7f9fa;
    border: 1px solid #dcdcdc;
    border-left: 4px solid #2b4c7e;
    padding: 8px 12px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 10pt;
    line-height: 1.35;
    margin: 10px 0;
  }}
</style>
</head>
<body>

<!-- ==================== PAGE 1: TITLE PAGE ==================== -->
<table class="header-table">
  <tr>
    <td class="logo-cell">
      <img src="data:image/jpeg;base64,{logo_b64}" class="logo-img" alt="MMCOE Logo">
    </td>
    <td>
      <div class="college-title">Marathwada Mitra Mandal's College of Engineering</div>
      <div class="college-sub">Karvenagar, Pune - 411052 | Autonomous Institute Affiliated to SPPU</div>
      <div class="college-sub">Accredited with 'A++' Grade by NAAC | NBA Accredited Programmes</div>
      <div class="college-sub"><b>Website:</b> www.mmcoe.edu.in &nbsp;|&nbsp; <b>Email:</b> mmcoe@mmcoe.edu.in</div>
    </td>
  </tr>
</table>

<div class="dept-header">DEPARTMENT OF COMPUTER ENGINEERING</div>
<div class="academic-session">Academic Year 2024-2025 | Semester V (Class: TY Computer)</div>

<div style="height: 25px;"></div>

<div class="report-main-title">
  A MINI PROJECT REPORT ON<br>
  <span style="font-size: 19pt; color: #0b2240;">"Credit Risk Prediction System for FinTech Lending Platforms"</span>
</div>

<p style="text-align: center; font-size: 11.5pt; margin-top: 15px;">
  Submitted in partial fulfillment of the requirements for the course of<br>
  <b>Data Science and Machine Learning Laboratory (Course Code: DSML Lab)</b>
</p>

<div style="height: 35px;"></div>

<table class="title-page-table">
  <tr>
    <td style="width: 55%;">
      <b>Submitted By:</b><br><br>
      <b>1. Sumegh [Full Name]</b> (Roll No: [Your Roll No])<br>
      <b>2. [Partner Name 2]</b> (Roll No: [Roll No 2])<br>
      <b>3. [Partner Name 3]</b> (Roll No: [Roll No 3])<br>
      <b>4. [Partner Name 4]</b> (Roll No: [Roll No 4])<br><br>
      <b>Class:</b> Third Year Computer Engineering (TY Comp)
    </td>
    <td style="width: 45%; text-align: right;">
      <b>Under the Guidance of:</b><br><br>
      <b>Prof. / Dr. [Guide Name]</b><br>
      Department of Computer Engineering<br>
      MMCOE, Pune
    </td>
  </tr>
</table>

<div style="margin-top: 70px; text-align: center; font-size: 11pt; font-weight: bold; border-top: 1px solid #ccc; padding-top: 10px;">
  Department of Computer Engineering<br>
  Marathwada Mitra Mandal's College of Engineering, Pune - 411052
</div>

<!-- ==================== PAGE 2: TITLE, ABSTRACT & INTRODUCTION ==================== -->
<div class="page-break"></div>

<h1>1. Title of the Project</h1>
<p style="font-size: 13pt; font-weight: bold; color: #1a2a4b;">
  Credit Risk Prediction System for FinTech Lending Platforms Using Machine Learning
</p>
<p>
  <b>SDG Alignment:</b> <b>SDG 8 (Decent Work and Economic Growth - Target 8.10)</b>: Strengthening domestic financial capacity to expand equitable access to banking and financial services, and <b>SDG 9 (Industry, Innovation, and Infrastructure)</b>.
</p>

<h1>2. Abstract</h1>
<p>
  With the rapid expansion of digital financial technology (FinTech) platforms, automated credit risk evaluation has emerged as a cornerstone for sustainable retail banking and peer-to-peer lending. Traditional credit scoring systems frequently suffer from rigid manual underwriting processes, prolonged turnaround times, and an inability to adapt to non-linear correlations across multi-dimensional borrower attributes. This project designs and implements an intelligent, automated credit risk prediction system utilizing supervised machine learning classifiers trained on real-world loan repayment records from the LendingClub platform.
</p>
<p>
  A rigorous data pipeline was constructed to clean the data, impute missing financial observations, encode categorical attributes, standardize continuous financial indicators, and correct for significant class imbalance between non-defaulters and defaulters. Three supervised classification algorithms - Logistic Regression, Decision Tree Classifier, and Random Forest Classifier - were trained with cost-sensitive class balancing and systematically evaluated across Accuracy, Precision, Recall, F1-Score, and ROC-AUC metrics. Random Forest achieved superior discriminative performance, recording an ROC-AUC of 0.732 and a high recall of 0.668 on defaulted loans. Furthermore, a clean, user-friendly Graphical User Interface was developed using Streamlit, enabling loan underwriters to input applicant profiles in real-time, inspect predicted default probabilities, and receive automated risk tier recommendations (Low Risk, Medium Risk, High Risk).
</p>

<h1>3. Introduction</h1>
<p>
  Credit risk assessment represents the fundamental mechanism through which financial institutions, commercial banks, and digital lending platforms safeguard loan capital against customer insolvency and loan defaults. In peer-to-peer and digital lending platforms, underwriters face a critical trade-off: overestimating credit risk leads to the unwarranted rejection of creditworthy borrowers (reducing platform revenue and limiting financial inclusion), while underestimating credit risk leads to capital write-offs and bad loans (Charged Off debts).
</p>
<p>
  Data-driven statistical modeling and Machine Learning present transformative opportunities for credit risk analysis. Algorithms can detect subtle multi-attribute interaction patterns - such as the interplay between Debt-to-Income (DTI) ratio, annual income, credit grade, and FICO credit score - that static scorecard models overlook. By deploying predictive classification models, lenders can automate initial loan screening, minimize credit turnaround latency from days to seconds, and maintain stringent default prevention controls.
</p>

<h1>4. Problem Statement</h1>
<p>
  To design, implement, and benchmark an automated Credit Risk Prediction System for a FinTech digital lending platform using demographic, credit historical, and financial loan data. The system must accurately predict the likelihood of loan default for prospective loan applicants, resolve severe real-world data skewness (imbalance between paid and charged-off loans), quantitatively compare at least three distinct machine learning algorithms, and provide an interactive Graphical User Interface (GUI) that empowers credit underwriting officers to make informed, objective, and timely lending decisions.
</p>

<!-- ==================== PAGE 3: LITERATURE SURVEY & TECHNICAL SPECIFICATIONS ==================== -->
<div class="page-break"></div>

<h1>5. Literature Survey</h1>
<p>
  Credit scoring and predictive default modeling have been widely studied in financial engineering and computational intelligence literature. A survey of 5 recent landmark papers informs the architecture and methodology of this project:
</p>

<table class="data-table">
  <tr>
    <th style="width: 20%;">Paper / Author</th>
    <th style="width: 15%;">Domain / Year</th>
    <th style="width: 32%;">Methodology & Models</th>
    <th style="width: 33%;">Key Findings & Insights</th>
  </tr>
  <tr>
    <td><b>Hand, D. J., & Henley, W. E.</b> [1]</td>
    <td>Statistical Credit Scoring</td>
    <td>Statistical classification methods including Logistic Regression and Discriminant Analysis for retail credit scoring.</td>
    <td>Established that parametric Logistic Regression offers high baseline interpretability and regulatory auditability in banking credit decisions.</td>
  </tr>
  <tr>
    <td><b>Lessmann, S., et al.</b> [2]</td>
    <td>Applied Soft Computing (2015)</td>
    <td>Large-scale benchmarking of 41 classifiers (SVMs, Ensembles, Neural Networks) across credit datasets.</td>
    <td>Demonstrated that tree ensemble techniques (Random Forests and Gradient Boosting) consistently outperform classical individual classifiers.</td>
  </tr>
  <tr>
    <td><b>Brown, I., & Mues, C.</b> [3]</td>
    <td>Expert Systems with Applications</td>
    <td>Investigation of classifier performance on severely imbalanced credit scoring datasets using resampling techniques.</td>
    <td>Demonstrated that optimizing for Area Under the ROC Curve (ROC-AUC) and cost-weighted training significantly improves default recall over raw accuracy.</td>
  </tr>
  <tr>
    <td><b>Xia, Y., et al.</b> [4]</td>
    <td>IEEE Access (2020)</td>
    <td>Sequential tree-based and ensemble learning models for peer-to-peer (P2P) lending default prediction.</td>
    <td>Confirmed that borrower financial leverage (DTI), interest rate, and historical credit tier (grade) are the primary determinants of P2P default probability.</td>
  </tr>
  <tr>
    <td><b>Malekipirbazari, M., & Aksakalli, V.</b> [5]</td>
    <td>Journal of Financial Data Science</td>
    <td>Random Forest-based risk assessment framework on peer-to-peer lending platforms (LendingClub).</td>
    <td>Proved that Random Forest handles mixed numerical-categorical features and outliers with superior robustness compared to standard scorecards.</td>
  </tr>
</table>

<h1>6. Technical Specifications & Architecture</h1>

<h2>6.1 Software Platform (Front-End & Back-End)</h2>
<ul>
  <li><b>Front-End UI:</b> Streamlit 1.30+ Web Framework / Python Tkinter GUI desktop interface. Provides dynamic input sliders, drop-down menus, model selection buttons, and instantaneous probability gauge rendering.</li>
  <li><b>Back-End Engine:</b> Python 3.12 runtime environment, Scikit-Learn machine learning pipeline, Pandas data manipulation engine, and Pickle model serialization.</li>
</ul>

<h2>6.2 Dataset Description & Metadata</h2>
<ul>
  <li><b>Dataset Name:</b> LendingClub Consumer Loan and Repayment Dataset (accepted_2007_to_2018Q4.csv).</li>
  <li><b>Public Source:</b> Kaggle Open Data (https://www.kaggle.com/datasets/wordsforthewise/lending-club).</li>
  <li><b>Sample Extraction:</b> 100,000 transaction records selected for model training and validation.</li>
  <li><b>Target Variable:</b> Binary target variable 'default' derived from loan outcome:
    <ul>
      <li>'Fully Paid': Applicant successfully repaid all loan capital and interest (Class 0, ~80%).</li>
      <li>'Charged Off': Loan defaulted and written off as bad debt by the lender (Class 1, ~20%).</li>
    </ul>
  </li>
  <li><b>Key Predictive Attributes:</b>
    <ul>
      <li>loan_amnt: Total sanctioned principal loan amount (in USD).</li>
      <li>term: Repayment duration contract (36 months or 60 months).</li>
      <li>int_rate: Assigned interest rate on the loan product (percentage).</li>
      <li>grade: Lending platform assigned credit rating band (A through G).</li>
      <li>emp_length: Applicant formal employment duration (in years).</li>
      <li>home_ownership: Housing residential tenure (RENT, MORTGAGE, OWN).</li>
      <li>annual_inc: Self-reported gross annual income of the borrower.</li>
      <li>purpose: Declared commercial loan purpose (e.g., debt consolidation, small business, home improvement).</li>
      <li>dti: Debt-to-Income percentage ratio measuring existing financial leverage.</li>
      <li>fico_range_low: Standardized credit bureau FICO baseline score.</li>
    </ul>
  </li>
</ul>

<!-- ==================== PAGE 4: PREPROCESSING & MACHINE LEARNING ALGORITHMS ==================== -->
<div class="page-break"></div>

<h2>6.3 Data Preprocessing Techniques</h2>
<p>
  To prepare raw loan records for machine learning training, a rigorous preprocessing pipeline was executed:
</p>
<ol>
  <li><b>Data Filtering:</b> Active loans (Current, In Grace Period, Late) were filtered out, retaining only finalized outcomes (Fully Paid vs. Charged Off) to establish clean ground-truth supervisory labels.</li>
  <li><b>Regex Feature Extraction:</b> Contract term strings ('36 months', '60 months') were extracted into integer values. Employment length strings ('10+ years', '&lt; 1 year') were parsed into continuous numeric figures.</li>
  <li><b>Ordinal & Nominal Encoding:</b> Lending grade ratings ('A' through 'G') were mapped ordinally to integer values (1 to 7). Nominal variables (home_ownership, purpose) were transformed using One-Hot Encoding (pd.get_dummies).</li>
  <li><b>Imputation of Missing Data:</b> Employment length missing values were imputed with 0 (indicating unverified/zero years). Debt-to-Income (dti) missing figures were replaced using the feature median.</li>
  <li><b>Feature Scaling:</b> Standardized continuous predictors using Z-score normalization via StandardScaler() such that each feature possesses zero mean and unit variance.</li>
  <li><b>Class Imbalance Correction:</b> Defaulters constitute only ~20% of the sample. To prevent classifiers from trivially predicting the majority class, cost-sensitive balanced weighting (class_weight='balanced') was applied across all models.</li>
</ol>

<h2>6.4 Libraries & Functions Used</h2>
<table class="data-table">
  <tr>
    <th style="width: 25%;">Library</th>
    <th style="width: 35%;">Primary Modules / Classes</th>
    <th style="width: 40%;">Functional Purpose</th>
  </tr>
  <tr>
    <td><b>pandas & numpy</b></td>
    <td>read_csv(), get_dummies(), fillna(), extract()</td>
    <td>Dataframe loading, cleaning, feature transformation, and categorical one-hot encoding.</td>
  </tr>
  <tr>
    <td><b>scikit-learn</b></td>
    <td>train_test_split(), StandardScaler()</td>
    <td>Stratified 80/20 train-test splitting and feature scaling.</td>
  </tr>
  <tr>
    <td><b>scikit-learn (Models)</b></td>
    <td>LogisticRegression(), DecisionTreeClassifier(), RandomForestClassifier()</td>
    <td>Model instantiation, hyperparameter tuning, cost-sensitive fitting, and probability inference.</td>
  </tr>
  <tr>
    <td><b>scikit-learn (Metrics)</b></td>
    <td>accuracy_score(), recall_score(), roc_auc_score(), f1_score()</td>
    <td>Quantitative validation and performance benchmarking on test data.</td>
  </tr>
  <tr>
    <td><b>streamlit</b></td>
    <td>st.number_input(), st.selectbox(), st.button(), st.bar_chart()</td>
    <td>Reactive user interface design, user input handling, and dashboard visualization.</td>
  </tr>
  <tr>
    <td><b>pickle</b></td>
    <td>dump(), load()</td>
    <td>Exporting trained model objects, scalers, and metadata for seamless UI deployment.</td>
  </tr>
</table>

<h1>7. Machine Learning Algorithms Implemented</h1>
<p>
  Three diverse classifier architectures representing linear, non-linear rule-based, and ensemble paradigms were trained:
</p>
<ul>
  <li>
    <b>1. Logistic Regression:</b> A fundamental linear classification algorithm utilizing the log-odds logit link function:
    <div class="code-block">P(Default = 1 | X) = 1 / (1 + exp(-(beta_0 + beta_1 * X_1 + ... + beta_k * X_k)))</div>
    Optimized with L2 ridge regularization and balanced class penalties. It provides an interpretable baseline indicating direction and magnitude of financial risks.
  </li>
  <li>
    <b>2. Decision Tree Classifier (CART):</b> A non-parametric supervised tree algorithm using Gini impurity criterion to formulate orthogonal feature partition thresholds. Hyperparameters were constrained to max_depth=6 to prevent severe overfitting while preserving hierarchical decision rules.
  </li>
  <li>
    <b>3. Random Forest Classifier:</b> An ensemble bagging technique constructing 100 decorrelated decision trees (n_estimators=100, max_depth=10). Each tree is trained on a bootstrap sample of the training dataset with random feature subspace sampling at each split. Final predictions aggregate probability estimates across the entire forest:
    <div class="code-block">P_ensemble(y = 1) = (1 / N) * SUM( P_tree_i(y = 1) )</div>
    This significantly lowers model variance, dampens outlier noise, and produces reliable probability calibrations.
  </li>
</ul>

<!-- ==================== PAGE 5: EVALUATION, COMPARISON & RESULTS ==================== -->
<div class="page-break"></div>

<h1>8. Performance Metrics & Evaluation</h1>
<p>
  Model performance was evaluated on a held-out test partition consisting of 20% of the sample (17,578 loans), preserved entirely separate from training to evaluate true generalization capability. Because credit default prediction is inherently an imbalanced cost problem (false negatives - approving a bad loan - cost substantially more than false positives - auditing a good applicant), the primary evaluation metrics selected are <b>Recall</b> and <b>ROC-AUC</b>:
</p>
<ul>
  <li><b>Accuracy:</b> (TP + TN) / (TP + TN + FP + FN). Overall ratio of correct decisions.</li>
  <li><b>Precision:</b> TP / (TP + FP). Proportion of predicted defaulters that actually defaulted.</li>
  <li><b>Recall (Sensitivity):</b> TP / (TP + FN). Proportion of actual defaulters successfully caught by the model.</li>
  <li><b>F1-Score:</b> Harmonic mean of precision and recall: 2 * (Precision * Recall) / (Precision + Recall).</li>
  <li><b>ROC-AUC:</b> Area Under the Receiver Operating Characteristic curve, measuring the probability that the classifier ranks a randomly chosen defaulter higher than a non-defaulter across all classification thresholds.</li>
</ul>

<h1>9. Comparison of Algorithms</h1>
<p>
  The quantitative performance comparison across the three trained models on the test dataset is detailed below:
</p>

<table class="data-table">
  <tr>
    <th>Algorithm</th>
    <th>Accuracy</th>
    <th>Precision</th>
    <th>Recall (Defaulters)</th>
    <th>F1-Score</th>
    <th>ROC-AUC Score</th>
  </tr>
  <tr>
    <td><b>Logistic Regression</b></td>
    <td class="center-cell">0.682</td>
    <td class="center-cell">0.342</td>
    <td class="center-cell">0.637</td>
    <td class="center-cell">0.445</td>
    <td class="center-cell">0.728</td>
  </tr>
  <tr>
    <td><b>Decision Tree</b></td>
    <td class="center-cell">0.662</td>
    <td class="center-cell">0.329</td>
    <td class="center-cell">0.664</td>
    <td class="center-cell">0.440</td>
    <td class="center-cell">0.725</td>
  </tr>
  <tr>
    <td><b>Random Forest Classifier</b></td>
    <td class="center-cell"><b>0.667</b></td>
    <td class="center-cell"><b>0.335</b></td>
    <td class="center-cell"><b>0.668</b></td>
    <td class="center-cell"><b>0.446</b></td>
    <td class="center-cell"><b>0.732</b></td>
  </tr>
</table>

"""

if chart_b64:
    html_content += f"""
<div class="figure-box">
  <img src="data:image/png;base64,{chart_b64}" alt="Performance Comparison Chart">
  <div class="figure-caption">Figure 1: Performance Metric Comparison across Machine Learning Models on Test Dataset.</div>
</div>
"""

html_content += """
<p>
  <b>Comparative Analysis & Findings:</b>
</p>
<ul>
  <li><b>Default Detection Power (Recall):</b> The Random Forest Classifier achieved the highest recall at <b>66.8%</b>, successfully flagging over two-thirds of all true defaulting loans. This was closely matched by Decision Tree (66.4%) and Logistic Regression (63.7%).</li>
  <li><b>Discriminative Ranking (ROC-AUC):</b> Random Forest established the highest overall discrimination with an ROC-AUC of <b>0.732</b>, outperforming Logistic Regression (0.728) and Decision Tree (0.725).</li>
  <li><b>Precision-Recall Trade-off:</b> Because class weighting was enabled to heavily prioritize default prevention, precision settled in the 33-34% range. In lending operations, this trade-off is deliberate: preventing irreversible loan write-offs is prioritized over requiring supplementary underwriting reviews for false positives.</li>
</ul>

<!-- ==================== PAGE 6: GUI DEMONSTRATION, CONCLUSION & REFERENCES ==================== -->
<div class="page-break"></div>

<h1>10. GUI Demonstration & Real-Time Decision Support</h1>
<p>
  A graphical user interface was built using <b>Streamlit</b> to provide an end-to-end operational software solution for lending officers:
</p>
<ul>
  <li><b>Applicant Profile Intake:</b> Loan officers enter applicant loan amount, interest rate, annual income, debt-to-income ratio, FICO credit score, employment tenure, and loan purpose through standardized input widgets.</li>
  <li><b>Model Selection:</b> The interface permits dynamic run-time toggling between Logistic Regression, Decision Tree, and Random Forest models.</li>
  <li><b>Real-Time Risk Categorization:</b> The backend transforms input records through the saved StandardScaler pipeline and computes the exact default probability score (P_default):
    <ul>
      <li><b>P_default &lt; 40%:</b> <span style="color: green; font-weight: bold;">LOW RISK (Approve Loan)</span> - Green status banner indicating strong creditworthiness.</li>
      <li><b>40% &le; P_default &lt; 60%:</b> <span style="color: #d97706; font-weight: bold;">MEDIUM RISK (Review Carefully)</span> - Amber alert recommending manual document verification and guarantor review.</li>
      <li><b>P_default &ge; 60%:</b> <span style="color: red; font-weight: bold;">HIGH RISK (Reject Loan)</span> - Red warning indicating high likelihood of default and capital loss.</li>
    </ul>
  </li>
  <li><b>Comparative Benchmarking:</b> An integrated interactive bar chart and metrics table are embedded inside the UI, allowing stakeholders to inspect algorithm fidelity during live demonstrations.</li>
</ul>

<h1>11. Conclusion & Future Scope</h1>
<p>
  This mini project successfully implemented and benchmarked a complete Machine Learning-powered Credit Risk Prediction System for digital lending. By utilizing 100,000 historical consumer loan records from LendingClub and applying cost-sensitive balanced modeling, the system addresses real-world class imbalance and achieves strong predictive performance (ROC-AUC 0.732, Recall 66.8% via Random Forest). The accompanying Streamlit interface provides transparent, interpretable, and real-time decision assistance that bridges theoretical machine learning with practical banking workflows.
</p>
<p>
  <b>Future Enhancements:</b>
</p>
<ul>
  <li>Integrating advanced gradient boosting models (XGBoost, LightGBM, CatBoost) to further optimize ROC-AUC.</li>
  <li>Incorporating model explainability frameworks (SHAP / LIME values) into the GUI to present feature-level explanations for why an applicant's loan was rejected.</li>
  <li>Deploying the pipeline into cloud infrastructure (AWS/GCP) via Docker containerization with automated REST API endpoints for seamless core-banking integration.</li>
</ul>

<h1>12. References</h1>
<ol>
  <li>Hand, D. J., & Henley, W. E. (1997). <i>Statistical classification methods in consumer credit scoring: a review</i>. Journal of the Royal Statistical Society: Series A (Statistics in Society), 160(3), 523-541.</li>
  <li>Lessmann, S., Baesens, B., Seow, H. V., & Thomas, L. C. (2015). <i>Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research</i>. European Journal of Operational Research, 247(1), 124-136.</li>
  <li>Brown, I., & Mues, C. (2012). <i>An experimental study on the performance of ensemble methods in credit scoring for imbalanced credit datasets</i>. Expert Systems with Applications, 39(3), 3446-3453.</li>
  <li>Xia, Y., Liu, C., Da, B., & Xie, F. (2020). <i>A novel heterogeneous ensemble credit scoring model based on bstacking approach</i>. IEEE Access, 8, 198999-199011.</li>
  <li>Malekipirbazari, M., & Aksakalli, V. (2015). <i>Risk assessment in social lending via random forests</i>. Expert Systems with Applications, 42(10), 4621-4631.</li>
  <li>LendingClub Consumer Credit Default Dataset (2007-2018Q4), Kaggle Open Data. Available: https://www.kaggle.com/datasets/wordsforthewise/lending-club</li>
  <li>Pedregosa, F., et al. (2011). <i>Scikit-learn: Machine Learning in Python</i>. Journal of Machine Learning Research, 12, 2825-2830.</li>
</ol>

</body>
</html>
"""

with open('full_miniproject_report.html', 'w') as f:
    f.write(html_content)

subprocess.run(['textutil', '-convert', 'docx', 'full_miniproject_report.html', '-output', 'DSML_Mini_Project_Full_Report.docx'])
print('Full report generated! Size:', os.path.getsize('DSML_Mini_Project_Full_Report.docx'))
