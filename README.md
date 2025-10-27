Data Experimentation: Titanic Survival Analysis

This is a classic introductory data science project focused on Exploratory Data Analysis (EDA). The goal is to analyze the Titanic passenger dataset to uncover factors that influenced survival rates.

This project follows a simple 5-step data science workflow:

Acquire: Load the data from a .csv file.

Explore & Clean: Examine the data, identify missing values (like 'Age' or 'Cabin'), and handle them.

Analyze: Ask specific questions about the data.

Visualize: Create plots to answer those questions.

Present: Report the findings.

Dataset

Source: Kaggle: Titanic - Machine Learning from Disaster

File Used: train.csv (renamed to titanic.csv)

Key Findings & Visualizations

Here are the main questions I asked and the insights I found:

Finding 1: What was the overall survival rate?

Only 38.4% of the passengers in this dataset survived the sinking of the Titanic.

Finding 2: Did passenger class affect survival?

Yes, dramatically. Passengers in 1st Class had a much higher chance of survival than those in 3rd Class.

Insight: This suggests a strong correlation between socio-economic status and survival.

Finding 3: Did gender affect survival?

Yes, this was one of the strongest factors. Female passengers had a far higher survival rate than male passengers.

Insight: This aligns with the "women and children first" protocol.

Finding 4: What was the age distribution of survivors?

The plots show that children (under 10) had a noticeably higher survival rate. Very elderly passengers (70+) had a very poor survival rate. For adults in the 20-40 age range, a large number did not survive.

Finding 5: How did family size affect survival?

This was interesting.

People traveling alone (FamilySize = 1) had a lower survival rate.

People in small families (FamilySize = 2-4) had the best survival rate.

People in large families (FamilySize = 5+) had a very poor survival rate.

Insight: Traveling with a small group may have provided support, while trying to manage a large family in the chaos may have been a disadvantage.

Tools Used

Python 3

Pandas: For data loading and manipulation (cleaning).

Matplotlib & Seaborn: For data visualization.roup may have provided support, while trying to manage a large family in the chaos may have been a disadvantage.Tools UsedPython 3Pandas: For data loading and manipulation (cleaning).Matplotlib & Seaborn: For data visualization.
