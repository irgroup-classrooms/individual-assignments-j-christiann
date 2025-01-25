# Dataset: Adult Income

import pandas as pd
import urllib.request

train_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
test_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"

columns = [
    "age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
    "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income"
]

train_data = pd.read_csv(train_url, header=None, names=columns, skipinitialspace=True)
test_data = pd.read_csv(test_url, header=None, names=columns, skiprows=1, skipinitialspace=True)

print("Training Data:")
print(train_data.head())

print("\nTest Data:")
print(test_data.head())

save_dir = r"C:\Users\Joshua Christian\Desktop\Semester 3\DIS08"

train_data.to_csv(f"{save_dir}adult_train.csv", index=False)
test_data.to_csv(f"{save_dir}adult_test.csv", index=False)

## Creating Age Groups
import pandas as pd

train_file = r"C:\Users\Joshua Christian\Desktop\Semester 3\DIS08\DIS08adult_train.csv"
test_file = r"C:\Users\Joshua Christian\Desktop\Semester 3\DIS08\DIS08adult_test.csv"

columns = [
    "age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
    "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income"
]

train_data = pd.read_csv(train_file, header=0, names=columns, skipinitialspace=True)

bins = [0, 20, 30, 40, 50, 60, 70, 100]
labels = ['0-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70+']

train_data['age_group'] = pd.cut(train_data['age'], bins=bins, labels=labels, right=False)

age_grouped = train_data.groupby('age_group').size()

print(age_grouped)

## Average Age by Income Class
average_age_by_income = data.groupby("income")["age"].mean()
print(average_age_by_income)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))  # Set figure size
sns.barplot(x=age_grouped.index, y=age_grouped.values, palette="viridis")

plt.title("Distribution of Individuals by Age Group", fontsize=16)
plt.xlabel("Age Groups", fontsize=14)
plt.ylabel("Number of Individuals", fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

plt.tight_layout()
plt.show()

## Creating a Boxplot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\Joshua Christian\Desktop\Semester 3\DIS08\DIS08adult_train.csv"  # Update this with your file path
data = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="income", y="age", palette="Set2")

plt.title("Age Distribution by Income Group", fontsize=16)
plt.xlabel("Income Group", fontsize=14)
plt.ylabel("Age", fontsize=14)

plt.show()

## Conducting KKN on The Dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

file_path = r"C:\Users\Joshua Christian\Desktop\Semester 3\DIS08\DIS08adult_train.csv"
columns = [
    "age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
    "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income"
]
data = pd.read_csv(file_path, header=0, names=columns, skipinitialspace=True)

categorical_columns = ["workclass", "education", "marital_status", "occupation", "relationship", "race", "sex", "native_country", "income"]
encoder = LabelEncoder()
for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])

scaler = StandardScaler()
numerical_columns = ["age", "fnlwgt", "education_num", "capital_gain", "capital_loss", "hours_per_week"]
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

X = data.drop("income", axis=1)  # Features
y = data["income"]  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

k = 5  # Choose number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

## Conducting Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

file_path = r"C:\Users\Joshua Christian\Desktop\Semester 3\DIS08\DIS08adult_train.csv"
columns = [
    "age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
    "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income"
]
data = pd.read_csv(file_path, header=0, names=columns, skipinitialspace=True)

X = data.drop("income", axis=1)
y = data["income"]

categorical_columns = ["workclass", "education", "marital_status", "occupation", 
                       "relationship", "race", "sex", "native_country"]
numerical_columns = ["age", "fnlwgt", "education_num", "capital_gain", "capital_loss", "hours_per_week"]

encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
scaler = StandardScaler()

X_categorical = encoder.fit_transform(X[categorical_columns])
X_numerical = scaler.fit_transform(X[numerical_columns])

import numpy as np
X_processed = np.hstack((X_categorical, X_numerical))

X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.3, random_state=42)

logreg = LogisticRegression(max_iter=500)
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
