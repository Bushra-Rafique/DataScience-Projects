# Credit Risk Prediction:
A project to predict whether a loan applicant is likely to **default or not**, using the **Loan Prediction Dataset** from Kaggle.

## Objective:
Predict the loan approval status (`Loan_Status`) based on applicant details such as income, loan amount, education, credit history, and more.

## Dataset:
- **Source:** [Kaggle - Loan Prediction Dataset](https://www.kaggle.com/)
- **Target Variable:** `Loan_Status` (Y/N)
- **Features:** Gender, Married, Education, ApplicantIncome, LoanAmount, Credit_History, etc.

## ⚙Steps Performed:

### 1. Data Cleaning:
- Handled missing values using mode (for categorical) and median (for numerical).
- Dropped remaining nulls if any.

### 2. Feature Engineering:
- Created `TotalIncome` = ApplicantIncome + CoapplicantIncome
- Applied `Log` transformation to handle skewness (optional)
- Binned income into categories for visualization

### 3. Data Visualization:
- Countplot of `Education` vs `Loan_Status`
- Distribution plots for `LoanAmount` and `TotalIncome`
- **Countplot**: Income bins vs `Loan_Status`
- Scatter plot: TotalIncome vs LoanAmount (colored by Loan_Status)

### 4. Encoding & Splitting:
- Used Label Encoding for categorical features
- Selected key features: `Credit_History`, `Education`, `LoanAmount`, `TotalIncome`
- Performed Train-Test split (80-20)

### 5. Model Training:
- **Logistic Regression**
- **Decision Tree Classifier**

### 6. Evaluation:
- Accuracy Score
- Confusion Matrix for both models
  

## Results:

| Model               | Accuracy |
|---------------------|----------|
| Logistic Regression | ~80%     |
| Decision Tree       | ~75%     |

> Logistic Regression performed slightly better in this binary classification task.
