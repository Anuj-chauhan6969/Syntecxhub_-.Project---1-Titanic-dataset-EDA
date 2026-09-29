# 🚢 Titanic Dataset — Exploratory Data Analysis

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the Titanic dataset using Python.

The analysis focuses on understanding passenger characteristics, missing data, and the relationship between passenger attributes and survival.

The project analyzes survival rates based on:

* 👤 Sex
* 🎫 Passenger Class
* 🎂 Age Groups

It also uses visualizations such as **bar charts, violin plots, and boxplots** to identify patterns, distributions, and outliers.

---

## 🎯 Objectives

The main objectives of this project are:

* Load and inspect the Titanic dataset.
* Analyze dataset structure, columns, and data types.
* Identify and inspect missing values.
* Calculate survival rates by sex.
* Calculate survival rates by passenger class.
* Divide passengers into age groups and analyze survival.
* Visualize important findings.
* Identify distribution patterns and potential outliers.
* Summarize the main findings from the analysis.

---

## 🛠️ Technologies Used

* **Python 3**
* **Pandas**
* **Seaborn**
* **Matplotlib**

---

## 📂 Project Structure

```text
Titanic-EDA/
│
├── analysis.py
├── README.md
├── requirements.txt
│
└── output/
    ├── survival_by_sex.png
    ├── survival_by_class.png
    ├── survival_by_age_group.png
    ├── age_violinplot.png
    ├── age_boxplot_by_class.png
    └── survival_by_sex_class.png
```

---

## 📊 Dataset

The project uses the **Titanic dataset** provided through the Seaborn dataset collection.

Important columns used in this analysis include:

| Column     | Description                               |
| ---------- | ----------------------------------------- |
| `survived` | Survival status                           |
| `pclass`   | Passenger class                           |
| `sex`      | Passenger sex                             |
| `age`      | Passenger age                             |
| `fare`     | Passenger fare                            |
| `embarked` | Port of embarkation                       |
| `alone`    | Whether the passenger was traveling alone |

---

## 🔍 Analysis Performed

### 1. Dataset Inspection

The dataset is inspected to understand:

* Number of rows and columns
* Column names
* Data types
* First few records
* Missing values

### 2. Missing Value Analysis

Missing values are checked using Pandas.

Particular attention is given to columns such as:

* `age`
* `embarked`
* `deck`

This helps understand the completeness of the dataset before analysis.

### 3. Survival Rate by Sex

The project calculates and visualizes the percentage of passengers who survived according to sex.

**Output:**

`output/survival_by_sex.png`

### 4. Survival Rate by Passenger Class

Survival rates are compared across:

* First Class
* Second Class
* Third Class

**Output:**

`output/survival_by_class.png`

### 5. Survival Rate by Age Group

Passengers are divided into the following age groups:

* Child
* Teenager
* Young Adult
* Adult
* Senior

Their survival rates are then compared.

**Output:**

`output/survival_by_age_group.png`

### 6. Violin Plot

A violin plot is used to examine the distribution of passenger ages according to survival status.

**Output:**

`output/age_violinplot.png`

### 7. Boxplot

A boxplot is used to examine the age distribution across passenger classes and identify potential outliers.

**Output:**

`output/age_boxplot_by_class.png`

### 8. Sex and Class Analysis

The project also examines survival rates by combining:

* Sex
* Passenger Class

**Output:**

`output/survival_by_sex_class.png`

---

## 📈 Key Insights

* Female passengers had a substantially higher survival rate than male passengers.
* Survival rates varied significantly between passenger classes.
* First-class passengers generally had higher survival rates than passengers in lower classes.
* Survival patterns varied across different age groups.
* Age distributions differed across passenger classes, with boxplots showing variation and potential outliers.
* The combined analysis of sex and passenger class provides additional insight into survival patterns.

---

## ▶️ How to Run the Project

### Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Titanic-EDA.git
```

### Step 2 — Open the project

```bash
cd Titanic-EDA
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run the analysis

```bash
python analysis.py
```

The generated charts will be saved automatically inside the `output` folder.

---

## 📷 Visualizations

The project generates the following visualizations:

### Survival by Sex

![Survival by Sex](output/survival_by_sex.png)

### Survival by Passenger Class

![Survival by Class](output/survival_by_class.png)

### Survival by Age Group

![Survival by Age Group](output/survival_by_age_group.png)

### Age Distribution — Violin Plot

![Age Violin Plot](output/age_violinplot.png)

### Age Distribution by Class — Boxplot

![Age Boxplot](output/age_boxplot_by_class.png)

### Survival by Sex and Class

![Survival by Sex and Class](output/survival_by_sex_class.png)

---

## 📚 Learning Outcomes

Through this project, I practiced:

* Exploratory Data Analysis
* Data cleaning and inspection
* Missing-value analysis
* Data grouping and aggregation
* Categorical analysis
* Age bucketing
* Data visualization
* Bar charts
* Violin plots
* Boxplots
* Python data-analysis libraries

---

## 👨‍💻 Author

**Anuj Chauhan**

Python | Data Analysis | Cybersecurity | Machine Learning

---

## ⭐ Project Status

Completed ✅
