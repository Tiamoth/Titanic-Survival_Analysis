# 🚢 Data Experimentation: Titanic Survival Analysis

## Project Overview
This project performs an **Exploratory Data Analysis (EDA)** on the historical Titanic passenger dataset. The goal is to analyze survival trends and visualize the complex relationship between a passenger's attributes (Class, Gender, Age, and Family Size) and their probability of survival. This project follows a fundamental data science workflow.

***

## 📊 Data Science Workflow

This analysis follows a simple, repeatable 5-step workflow:

1.  **Acquire:** Load the data from `titanic.csv`.
2.  **Explore & Clean:** Examine data for missing values (e.g., 'Age', 'Cabin') and prepare it for analysis.
3.  **Analyze:** Ask specific, testable questions about survival factors.
4.  **Visualize:** Create plots to answer the questions and demonstrate the insights.
5.  **Present:** Report the key findings and conclusions.

### Dataset Source
* **Source:** Kaggle: Titanic - Machine Learning from Disaster
* **File Used:** `titanic.csv`

***

## 📈 Key Findings & Visualizations

### Finding 1: Overall Survival Rate
* **Insight:** Only **38.4%** of the passengers in this dataset survived the sinking of the Titanic.
* **Visualization:** (plot_1_survival_rate.png)

### Finding 2: Did Passenger Class Affect Survival?
* **Insight:** Yes, dramatically. **1st Class** passengers had a significantly higher chance of survival than those in 3rd Class, suggesting a strong correlation between socio-economic status and lifeboat access.
* **Visualization:** (plot_2_class_survival.png)

### Finding 3: Did Gender Affect Survival?
* **Insight:** This was one of the strongest factors. Female passengers had a far higher survival rate than male passengers, aligning with the **"women and children first"** protocol.
* **Visualization:** (plot_3_gender_survival.png)

### Finding 4: What was the Age Distribution of Survivors?
* **Insight:** **Children (under 10)** had a noticeably higher survival rate. The vast majority of adults in the 20-40 age range did not survive.
* **Visualization:** (plot_4_age_survival.png)

### Finding 5: How did Family Size Affect Survival?
* **Insight:** Passengers in **small families (Size 2-4)** had the best survival rate. Those traveling alone (Size 1) or in large families (Size 5+) had the worst outcomes, suggesting family management in the chaos was critical.
* **Visualization:** (plot_5_family_survival.png)

***

## 🛠️ Tools Used
* **Python 3**
* **Pandas:** For data loading and manipulation (cleaning).
* **Matplotlib & Seaborn:** For data visualization.
