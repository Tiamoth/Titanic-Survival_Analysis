# This is your main Python script.
# You will need to install a few libraries first:
# pip install pandas matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_analysis():
    print("Starting Titanic Survival Analysis...")

    # --- 1. ACQUIRE THE DATA ---
    # Load the dataset. Make sure 'titanic.csv' is in the same folder as this script.
    # You can download it from Kaggle: https://www.kaggle.com/c/titanic/data (download 'train.csv' and rename it)
    try:
        data = pd.read_csv('titanic.csv')
    except FileNotFoundError:
        print("Error: 'titanic.csv' not found.")
        print("Please download 'train.csv' from the Kaggle Titanic competition and rename it to 'titanic.csv'")
        return

    # --- 2. EXPLORE & CLEAN THE DATA ---
    
    # Get a quick overview of our data
    print("\n--- Data Info ---")
    data.info()

    # We can see missing values for 'Age', 'Cabin', and 'Embarked'.
    
    # Strategy for cleaning:
    # 1. 'Age': Fill missing values with the median (average) age.
    median_age = data['Age'].median()
    data['Age'].fillna(median_age, inplace=True)
    print(f"\nFilled missing 'Age' values with median: {median_age}")

    # 2. 'Embarked': Fill with the most common port (the 'mode').
    mode_embarked = data['Embarked'].mode()[0]
    data['Embarked'].fillna(mode_embarked, inplace=True)
    print(f"Filled missing 'Embarked' values with mode: {mode_embarked}")

    # 3. 'Cabin': Too many missing values. We'll drop this column for our simple analysis.
    data.drop('Cabin', axis=1, inplace=True)
    print("Dropped 'Cabin' column due to too many missing values.")

    # 4. Feature Engineering: Create a 'FamilySize' column. This is often more useful than 'SibSp' and 'Parch' alone.
    data['FamilySize'] = data['SibSp'] + data['Parch'] + 1 # +1 for the person themselves
    print("Created 'FamilySize' feature.")

    print("\n--- Data cleaning complete. No more missing values in key columns. ---")

    # --- 3. ANALYZE & VISUALIZE ---
    # Now we ask questions and answer them with plots.
    # We'll use seaborn for beautiful plots.
    sns.set(style="darkgrid")

    # Question 1: What was the overall survival rate?
    print("Generating Plot 1: Overall Survival Rate")
    plt.figure(figsize=(6, 6))
    data['Survived'].value_counts(normalize=True).plot(kind='pie', autopct='%1.1f%%', labels=['Did Not Survive', 'Survived'], colors=['#FF6347', '#90EE90'])
    plt.title('Overall Survival Rate')
    plt.ylabel('') # Hide the 'Survived' label on the y-axis
    plt.savefig('plot_1_survival_rate.png')
    print("Saved 'plot_1_survival_rate.png'")

    # Question 2: Did passenger class affect survival?
    print("Generating Plot 2: Survival by Passenger Class")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Pclass', hue='Survived', data=data, palette={0: '#FF6347', 1: '#90EE90'})
    plt.title('Survival Rate by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Count')
    plt.legend(title='Survival', labels=['Did Not Survive', 'Survived'])
    plt.savefig('plot_2_class_survival.png')
    print("Saved 'plot_2_class_survival.png'")

    # Question 3: Did gender affect survival?
    print("Generating Plot 3: Survival by Gender")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Sex', hue='Survived', data=data, palette={0: '#FF6347', 1: '#90EE90'})
    plt.title('Survival Rate by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(title='Survival', labels=['Did Not Survive', 'Survived'])
    plt.savefig('plot_3_gender_survival.png')
    print("Saved 'plot_3_gender_survival.png'")

    # Question 4: What was the age distribution of survivors vs. non-survivors?
    print("Generating Plot 4: Survival by Age Distribution")
    plt.figure(figsize=(12, 7))
    # Use seaborn's FacetGrid to draw two histograms on top of each other
    g = sns.FacetGrid(data, col='Survived', height=6, hue='Survived', palette={0: '#FF6347', 1: '#90EE90'})
    g.map(sns.histplot, 'Age', bins=20, kde=False)
    g.add_legend(title='Survival', labels=['Did Not Survive', 'Survived'])
    g.set_axis_labels('Age', 'Count')
    g.set_titles("Survived = {col_name}")
    plt.savefig('plot_4_age_survival.png')
    print("Saved 'plot_4_age_survival.png'")

    # Question 5: How did family size affect survival?
    print("Generating Plot 5: Survival by Family Size")
    plt.figure(figsize=(12, 7))
    sns.countplot(x='FamilySize', hue='Survived', data=data, palette={0: '#FF6347', 1: '#90EE90'})
    plt.title('Survival Rate by Family Size')
    plt.xlabel('Family Size (Self + Relatives)')
    plt.ylabel('Count')
    plt.legend(title='Survival', labels=['Did Not Survive', 'Survived'])
    plt.savefig('plot_5_family_survival.png')
    print("Saved 'plot_5_family_survival.png'")

    print("\n--- Analysis Complete! All plots saved as .png files. ---")

# This makes sure the script runs when you call it from the command line
if __name__ == "__main__":
    run_analysis()
