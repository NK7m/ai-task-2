import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('titanic.csv')

# 1. Basic Statistics
print("Summary Statistics:")
print(df.describe())
print("\nSurvival Rate:", df['Survived'].mean())

# 2. Data Quality Check
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Visualizations
plt.figure(figsize=(12,8))

# Survival by Class
plt.subplot(2,2,1)
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')

# Age Distribution
plt.subplot(2,2,2)
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')

# Fare Distribution
plt.subplot(2,2,3)
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare Distribution by Survival')

# Gender Survival
plt.subplot(2,2,4)
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')

plt.tight_layout()
plt.savefig('titanic_visuals.png')
plt.show()

# 4. Correlation Analysis
corr_matrix = df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.show()

# 5. Advanced Analysis
# Family size impact
df['FamilySize'] = df['SibSp'] + df['Parch']
sns.barplot(x='FamilySize', y='Survived', data=df)
plt.title('Survival Rate by Family Size')
plt.savefig('family_size_impact.png')
plt.show()