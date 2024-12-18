# -*- coding: utf-8 -*-
"""Exp2_MLP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GIZmxdy_hJ6tVEHNUJS4Qj_dAUV7ZJs2

# **Linear Expression**
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error ,r2_score , mean_absolute_error

# ==============================
# Dataset Selection (Uncomment the desired dataset)
# ==============================

# 1. Breast Cancer Dataset (sklearn default):
breast_cancer = load_breast_cancer()
df = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
labels = breast_cancer.target

# # 2. External Breast Cancer Dataset (CSV):
# df = pd.read_csv("breast-cancer.csv")
# labels = df['diagnosis']  # Assuming 'diagnosis' is the correct column name
# df = df.drop(['diagnosis'], axis=1)

# 3. Red Wine Quality Dataset:
df = pd.read_csv("winequality-red.csv", delimiter=",")
labels = df['quality']
df = df.drop(['quality'], axis=1)

# # 4. Housing Loan Approval Dataset:
# df = pd.read_csv("loan_sanction_train.csv")
# labels = df['Loan_Status']  # Assuming 'Loan_Status' is the target column
# labels = LabelEncoder().fit_transform(labels)  # Encode categorical target
# # Drop target column and preprocess categorical features
# df = df.drop(['Loan_Status'], axis=1)
# df = pd.get_dummies(df, drop_first=True)

# Exploratory Data Analysis for all 3
scatter_matrix(df.iloc[:, :5], figsize=(10, 10))  # Using first 5 features for visualization
plt.show()

sns.set(style="ticks", color_codes=True)
if 'species' in df.columns:
    sns.pairplot(df, hue='species')

plt.figure(figsize=(12, 10))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

# ==============================
# Preprocessing (Applies to all datasets , Except Bahar wala Breast cancer)
# ==============================

# Impute missing values and scale features
imputer = SimpleImputer(strategy='mean')
df_imputed = imputer.fit_transform(df)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_imputed)

# # ==============================
# # Preprocessing (Applies  Bahar wala Breast cancer)
# # ==============================

# # Encode categorical labels to numeric
# label_encoder = LabelEncoder()
# labels_encoded = label_encoder.fit_transform(labels)


# Impute missing values
imputer = SimpleImputer(strategy='mean')
df_imputed = imputer.fit_transform(df)

# Scale the imputed dataset
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_imputed)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(df_scaled, labels, test_size=0.2, random_state=42) # rest sabke liya
# X_train, X_test, y_train, y_test = train_test_split(df_scaled, labels_encoded, test_size=0.2, random_state=42) # for bahar wala breast cancer


# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Model Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

# ==============================
# Inference and Conclusion Plot
# ==============================

# Plot actual vs. predicted for the test set
predictions = model.predict(X_test)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, alpha=0.7, edgecolors="k")
plt.plot([min(y_test),max(y_test)],[min(y_test),max(y_test)], color = 'red')
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.grid(True)
plt.show()

"""# **Linear Regression using Sample Data**"""

# Given data
area = [340, 1080, 640, 880, 990, 510]
rent = [500, 1700, 1100, 800, 1400, 500]

# Step 1: Calculate required sums
n = len(area)
sum_x = 0
sum_y = 0
sum_x2 = 0
sum_xy = 0

for i in range(n):
    sum_x += area[i]
    sum_y += rent[i]
    sum_x2 += area[i] ** 2
    sum_xy += area[i] * rent[i]

# Step 2: Calculate b1 and b0
b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b0 = (sum_y - b1 * sum_x) / n

# Step 3: Calculate the linear regression line for A = 790
A = 1000
predicted_y = b0 + b1 * A

# Output the results
print(f"n: {n}")
print(f"Sum of x: {sum_x}")
print(f"Sum of y: {sum_y}")
print(f"Sum of x^2: {sum_x2}")
print(f"Sum of xy: {sum_xy}")
print(f"b1: {b1}")
print(f"b0: {b0}")
print(f"Predicted Rent for Area {A}: {predicted_y}")