# Personal Loan Acceptance Prediction
A classification project that predicts whether a customer is likely to accept a **personal loan offer**, based on their personal and financial information.

## Objective:
Train a machine learning model to predict if a customer will accept a loan offer, and analyze which customer groups are more responsive to marketing efforts.

## Dataset:
- **Source:** [Bank Marketing Dataset – UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
- **File:** `bank-full.csv` (semicolon-separated)
- **Target Variable:** `y`  
  (`yes` = accepted, `no` = did not accept)

## Steps Performed:
### 1. Data Exploration:
- Explored features like `age`, `job`, and `marital status`
- Plotted:
  - `Job vs Loan Acceptance`
  - `Marital Status vs Loan Acceptance`
  - `Age Distribution by Acceptance`

### 2. Data Preprocessing:
- One-hot encoded categorical features (e.g., job, marital, education, contact)
- Encoded target variable: `y` → 1 (yes), 0 (no)

### 3. Model Training:
- Used both:
  - **Logistic Regression**
  - **Decision Tree Classifier**

### 4. Model Evaluation:
- Evaluated models using:
  - **Accuracy Score**
  - **Classification Report**
  - **Confusion Matrix**

### 5. Group Analysis:
- Grouped data by `job` to compare **loan acceptance rates**
- Identified which customer groups are more likely to accept offers

## Results Summary:

| Model               | Accuracy (approx.) |
|---------------------|--------------------|
| Logistic Regression | ~88%               |
| Decision Tree       | ~85%               |

> Customers with jobs like "student" and "retired" showed higher acceptance rates.
