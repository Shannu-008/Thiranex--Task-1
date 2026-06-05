# Data Cleaning and Visualization Project

A beginner-friendly Python project demonstrating the end-to-end process of cleaning messy corporate data and generating actionable visual insights.

## 📌 Project Overview
This project takes a raw, messy dataset containing missing values, duplicates, and data entry errors, refines it using `pandas`, and visualizes the results with `seaborn`.

## 🛠️ Tech Stack & Libraries
*   **Language:** Python 3.x
*   **Data Manipulation:** Pandas, NumPy
*   **Data Visualization:** Matplotlib, Seaborn

## 📂 Repository Structure
*   `cleaning.py` - The main Python script containing data cleaning and visualization logic.
*   `output/` - Directory where generated data charts and insights are saved.
*   `README.md` - Documentation and project summary.

## 🧹 Cleaning Steps Performed
1.  **Duplicate Removal:** Dropped repeated rows to ensure data integrity.
2.  **Missing Value Imputation:** Handled missing age records by filling them with the calculated average age.
3.  **Error Correction:** Fixed mathematical anomalies (such as negative numbers in salary columns).
4.  **Data Type Conversion:** Cast decimal formatting to standard integers for clear reporting.

## 📊 Key Insights & Visualizations
Below is the generated chart showing the relationship between departments and compensation:

![Average Salary by Department](output/salary_by_department.png)

## 🚀 How to Run the Project
1. Clone this repository or download the files.
2. Open your terminal and install the required dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the cleaning script:
   ```bash
   python cleaning.py
   ```