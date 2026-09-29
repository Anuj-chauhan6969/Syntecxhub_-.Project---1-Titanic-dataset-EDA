import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load Titanic dataset
df = sns.load_dataset("titanic")

# -----------------------------
# 1. Basic Dataset Inspection
# -----------------------------

print("=" * 60)
print("TITANIC DATASET - EDA")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
print(df.info())

# -----------------------------
# 2. Missing Value Analysis
# -----------------------------

missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

print("\nColumns with Missing Values:")
print(missing)

# -----------------------------
# 3. Survival Rate by Sex
# -----------------------------

sex_survival = df.groupby("sex")["survived"].mean() * 100

print("\nSurvival Rate by Sex:")
print(sex_survival)

plt.figure(figsize=(7, 5))
sns.barplot(
    x=sex_survival.index,
    y=sex_survival.values
)

plt.title("Titanic Survival Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("output/survival_by_sex.png", dpi=300)
plt.show()

# -----------------------------
# 4. Survival Rate by Class
# -----------------------------

class_survival = df.groupby("pclass")["survived"].mean() * 100

print("\nSurvival Rate by Passenger Class:")
print(class_survival)

plt.figure(figsize=(7, 5))
sns.barplot(
    x=class_survival.index.astype(str),
    y=class_survival.values
)

plt.title("Titanic Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("output/survival_by_class.png", dpi=300)
plt.show()

# -----------------------------
# 5. Create Age Groups
# -----------------------------

df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=[
        "Child",
        "Teenager",
        "Young Adult",
        "Adult",
        "Senior"
    ]
)

age_survival = df.groupby(
    "age_group",
    observed=True
)["survived"].mean() * 100

print("\nSurvival Rate by Age Group:")
print(age_survival)

plt.figure(figsize=(8, 5))
sns.barplot(
    x=age_survival.index,
    y=age_survival.values
)

plt.title("Titanic Survival Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=20)
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("output/survival_by_age_group.png", dpi=300)
plt.show()

# -----------------------------
# 6. Violin Plot - Age vs Survival
# -----------------------------

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=df,
    x="survived",
    y="age"
)

plt.title("Age Distribution by Survival Status")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Age")

plt.tight_layout()
plt.savefig("output/age_violinplot.png", dpi=300)
plt.show()

# -----------------------------
# 7. Boxplot - Age by Class
# -----------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="pclass",
    y="age"
)

plt.title("Age Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Age")

plt.tight_layout()
plt.savefig("output/age_boxplot_by_class.png", dpi=300)
plt.show()

# -----------------------------
# 8. Survival by Sex and Class
# -----------------------------

sex_class = (
    df.groupby(["sex", "pclass"])["survived"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=sex_class,
    x="pclass",
    y="survived",
    hue="sex"
)

plt.title("Survival Rate by Sex and Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.ylim(0, 1)

plt.tight_layout()
plt.savefig("output/survival_by_sex_class.png", dpi=300)
plt.show()

print("\nEDA completed successfully!")
print("Charts have been saved in the 'output' folder.")
