# Task 1 - Iris Dataset Analysis

## Objective:
To explore and visualize the famous **Iris dataset** using Python libraries such as **Pandas**, **Seaborn**, and **Matplotlib**.  
This task demonstrates:
- Dataset loading
- Summary and structure overview
- Visualizations for insights


## Dataset:
- **Name:** Iris Flower Dataset  
- **Source:** Loaded directly using `seaborn.load_dataset("iris")`  
- **Optional CSV:** A copy of the dataset is also saved as `iris.csv` in this folder.


## Steps Performed:

1. **Imported libraries:**  
   `pandas`, `seaborn`, `matplotlib.pyplot`

2. **Loaded dataset:**  
   Used `sns.load_dataset("iris")` to load into a DataFrame.

3. **Saved CSV file (optional):**  
   `df.to_csv("iris.csv", index=False)`

4. **Explored dataset:**  
   - Shape
   - Column names
   - First 5 rows using `.head()`

5. **Visualizations:**
   -  **Scatter Plot (Pairplot)** – Showed pairwise relationships between features.
   -  **Histograms** – Displayed distribution of each feature.
   -  **Box Plots** – Identified outliers and compared species differences:
     - Sepal width by species
     - Petal width by species
     - Overall feature spread

## Tools Used:
- Python
- Google Colab / Jupyter Notebook
- Pandas
- Seaborn
- Matplotlib

