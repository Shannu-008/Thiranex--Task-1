# Corporate Data Cleansing & Advanced Analytics Pipeline

An industry-grade Python pipeline demonstrating automated data cleaning workflows, statistical imputation, and advanced visualizations for enterprise transaction records.

## 📌 Project Architecture
This project simulates an enterprise database export plagued with common data-entry errors (whitespace padding, unexpected data-type variances, duplicate entries, and financial outliers) and refines it into clean, production-ready assets.

## 📂 Repository Structure
*   `data/` - Storage directory for raw input files and generated clean CSV outputs.
*   `output/` - Automated storage for structural analytical dashboards and chart metrics.
*   `cleaning.py` - Core execution file utilizing pandas engines and visualization wrappers.
*   `requirements.txt` - Complete dependency specification for deployment.

## 🧹 Data Cleaning Pipeline Execution
The script automatically executes the following data engineering operations:
1.  **Transactional Deduplication:** Filters records using unique constraints to eliminate double-counting.
2.  **String Normalization:** Cleans data columns by stripping leading/trailing whitespaces and fixing casing anomalies.
3.  **Financial Anomaly Handling:** Detects erroneous negative values and programmatically corrects them using category-specific medians.
4.  **Statistical Group Imputation:** Replaces missing demographic records using regional median cluster metrics rather than a basic global average.

## 📊 Business Intelligence Visualizations
The automated analytics engine evaluates corporate distributions and demographic targets:

### 1. Revenue Distribution Matrix
![Revenue Distribution](output/category_revenue_distribution.png)

### 2. Regional Demographic Breakdown
![Regional Profiles](output/regional_demographics.png)

## 🚀 Deployment Instructions
1. Clone or download this project workspace.
2. Install the necessary baseline software layers:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute the full analytics and formatting wrapper:
   ```bash
   python cleaning.py
   ```