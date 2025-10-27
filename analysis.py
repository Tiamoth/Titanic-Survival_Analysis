

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_analysis():
    print("Starting Titanic Survival Analysis...")

   
    try:
        data = pd.read_csv('titanic.csv')
    except FileNotFoundError:
        print("Error: 'titanic.csv' not found.")
        print("Please download 'train.csv' from the Kaggle Titanic competition and rename it to 'titanic.csv'")
        return

   
    print("\n--- Data Info ---")
    data.info()


    median_age = data['Age'].median()
    data['Age'].fillna(median_age, inplace=True)
    print(f"\nFilled missing 'Age' values with median: {median_age}")

  
    mode_embarked = data['Embarked'].mode()[0]
    data['Embarked'].fillna(mode_embarked, inplace=True)
    print(f"Filled missing 'Embarked' values with mode: {mode_embarked}")


    data.drop('Cabin', axis=1, inplace=True)
    print("Dropped 'Cabin' column due to too many missing values.")

  
    data['FamilySize'] = data['SibSp'] + data['Parch'] + 1 
    print("Created 'FamilySize' feature.")

    print("\n--- Data cleaning complete. No more missing values in key columns. ---")


    sns.set(style="darkgrid")

    print("Generating Plot 1: Overall Survival Rate")
    plt.figure(figsize=(6, 6))
    data['Survived'].value_counts(normalize=True).plot(kind='pie', autopct='%1.1f%%', labels=['Did Not Survive', 'Survived'], colors=['#FF6347', '#90EE90'])
    plt.title('Overall Survival Rate')
    plt.ylabel('') 
    plt.savefig('plot_1_survival_rate.png')
    print("Saved 'plot_1_survival_rate.png'")

   
    print("Generating Plot 2: Survival by Passenger Class")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Pclass', hue='Survived', data=data, palette={0: '#FF6347', 1: '#90EE90'})
    plt.title('Survival Rate by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Count')
    plt.legend(title='Survival', labels=['Did Not Survive', 'Survived'])
    plt.savefig('plot_2_class_survival.png')
    print("Saved 'plot_2_class_survival.png'")

  
    print("Generating Plot 3: Survival by Gender")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Sex', hue='Survived', data=data, palette={0: '#FF6347', 1: '#90EE90'})
    plt.title('Survival Rate by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(title='Survival', labels=['Did Not Survive', 'Survived'])
    plt.savefig('plot_3_gender_survival.png')
    print("Saved 'plot_3_gender_survival.png'")

    
    print("Generating Plot 4: Survival by Age Distribution")
    plt.figure(figsize=(12, 7))

    g = sns.FacetGrid(data, col='Survived', height=6, hue='Survived', palette={0: '#FF6347', 1: '#90EE90'})
    g.map(sns.histplot, 'Age', bins=20, kde=False)
    g.add_legend(title='Survival', labels=['Did Not Survive', 'Survived'])
    g.set_axis_labels('Age', 'Count')
    g.set_titles("Survived = {col_name}")
    plt.savefig('plot_4_age_survival.png')
    print("Saved 'plot_4_age_survival.png'")


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

