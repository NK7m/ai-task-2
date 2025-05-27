# AI & ML Internship - Task 2: Exploratory Data Analysis

## Overview
This repository contains my EDA of the Titanic dataset as part of the AI & ML Internship tasks. The analysis includes statistical summaries, visualizations, and correlation analysis to understand factors influencing passenger survival.

## Files Included
1. `eda_analysis_report.txt` - Detailed findings from the EDA
2. `interview_answers.txt` - Answers to the interview questions
3. `titanic_eda.py` - Python script used for the analysis
4. Visualizations (saved as PNG files)

## Methodology
1. **Data Loading & Initial Inspection**: Checked structure and missing values
2. **Statistical Summaries**: Calculated key metrics for all features
3. **Univariate Analysis**: Created histograms and boxplots for numeric features
4. **Bivariate Analysis**: Examined relationships between features and survival
5. **Correlation Analysis**: Identified relationships between numeric features
6. **Advanced Analysis**: Created derived features (FamilySize) for deeper insights

## Key Findings
- Strong class bias in survival rates (1st class > 2nd > 3rd)
- "Women and children first" pattern clearly visible
- Fare amount showed positive correlation with survival
- Family size had non-linear relationship with survival

## How to Reproduce
1. Install requirements: `pip install pandas matplotlib seaborn`
2. Download Titanic dataset from Kaggle
3. Run `python titanic_eda.py`

## References
- Titanic dataset from Kaggle
- Pandas documentation
- Seaborn visualization examples
- Various Medium articles on EDA best practices