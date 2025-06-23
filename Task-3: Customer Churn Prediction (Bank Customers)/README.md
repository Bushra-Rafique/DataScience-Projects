# Customer Churn Prediction (Bank Customers):
A project to identify customers likely to leave the bank (churn), based on demographic and account-related features.

## Objective:
Predict whether a customer will **churn (exit the bank)** using classification algorithms and identify which features contribute the most to their decision.

## Dataset:

- **Source:** [Churn Modelling Dataset on Kaggle](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)
- **File:** `Churn_Modelling.csv`
- **Target Variable:** `Exited` (1 = Churned, 0 = Stayed)

## Steps Performed:
### 1. Data Cleaning:
- Removed irrelevant columns: `RowNumber`, `CustomerId`, and `Surname`.

### 2. Encoding:
- Encoded **Gender** using LabelEncoder.
- One-hot encoded **Geography** (France, Spain, Germany).

### 3. Feature Engineering:
- Standardized features using **StandardScaler**.

### 4. Train-Test Split:
- 80% Training / 20% Testing split.

### 5. Model Training:
- **Random Forest Classifier** was used for prediction.

### 6. Evaluation:
- Accuracy Score
- Confusion Matrix
- Classification Report

### 7. Feature Importance:
- Analyzed feature importance to understand key churn drivers.


## Results:

| Metric     | Score (approx.) |
|------------|------------------|
| Accuracy   | ~86%             |
| Key Drivers of Churn | Age, Geography (Germany), Balance, Tenure, IsActiveMember |

> The model suggests that **older customers, those with high balances, or from certain regions are more likely to churn.**
