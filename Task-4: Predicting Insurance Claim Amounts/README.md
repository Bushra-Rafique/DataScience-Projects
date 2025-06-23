# Predicting Insurance Claim Amounts
A machine learning regression project that estimates **medical insurance charges** based on personal and lifestyle data such as age, BMI, and smoking habits.

## Objective:
Build a **Linear Regression** model to predict the `charges` (medical insurance claim amount) and analyze the impact of **BMI**, **age**, and **smoking status** on those charges.

## Dataset:
- **Source:** [Medical Cost Personal Dataset on Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **File:** `insurance.csv`
- **Target Variable:** `charges` — medical cost billed to customers

## Steps Performed:
### 1. Data Preprocessing:
- Encoded categorical features (`sex`, `smoker`, `region`) using `LabelEncoder`
- No missing values were found

### 2. Exploratory Data Visualization:
- **BMI vs Charges** using scatter plot
- **Age vs Charges** using scatter plot
- **Smoking status vs Charges** using box plot

### 3. Model Training:
- Used **Linear Regression** model from `scikit-learn`
- Selected key features: `age`, `bmi`, and `smoker`

### 4. Model Evaluation:
- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**

## Results:

| Metric | Score (approx.) |
|--------|------------------|
| MAE    | ~4200            |
| RMSE   | ~6100            |

> Smoking status significantly increases medical charges.  
> Age and BMI also show strong positive correlation with charges.
