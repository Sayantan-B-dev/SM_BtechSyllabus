# Basics of Data Mining

**Course:** Database Management Systems  
**Module:** 5 | **Lecture:** 2  
**Date:** 29-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Data Mining?

Data mining is the process of discovering patterns, correlations, and knowledge from large datasets using techniques from statistics, machine learning, and database systems. It is often described as "knowledge discovery from data."

**Common synonyms:** Knowledge Discovery in Databases (KDD), pattern discovery, knowledge extraction.

### Examples of Data Mining in Practice

- **Retail (Market Basket Analysis):** "Customers who bought diapers also bought beer." -- Association rule mining on transaction data.
- **Banking:** "Which transactions are likely to be fraudulent?" -- Anomaly detection on account activity.
- **Healthcare:** "Which patients are at high risk for readmission within 30 days?" -- Classification based on patient history.
- **E-commerce:** "Group customers based on purchasing behavior for targeted marketing." -- Clustering.
- **Finance:** "Predict tomorrow's stock price." -- Regression.

## The KDD Process

Knowledge Discovery in Databases (KDD) is the overall process of which data mining is a core step.

```
+------------+    +-----------+    +----------+    +----------+    +----------+
| Selection  |--->|Preprocess |--->|Transform |--->| Data     |--->|Interpre- |
| (Target    |    |(Clean,    |    |(Reduce,   |    | Mining   |    |tation/   |
|  Data)     |    | Remove    |    | Aggregate,|    |(Apply    |    |Evaluation|
|            |    | Noise)    |    | Normalize)|    |Algorithm)|    |          |
+------------+    +-----------+    +----------+    +----------+    +----------+
      |                |                |               |               |
      v                v                v               v               v
   Raw data       Clean data      Transformed       Patterns       Knowledge
                                  data
```

### Step 1: Selection
Identify the relevant data sources and select the subset of data needed for the analysis. Example: selecting customer transaction records from the last 3 years.

### Step 2: Preprocessing
Clean the data: handle missing values, remove noise, correct inconsistencies, and resolve data quality issues.

| Issue              | Example                      | Solution                      |
|--------------------|------------------------------|-------------------------------|
| Missing values     | NULL in age column           | Impute with mean/median/mode  |
| Outliers           | Salary = $10 million         | Cap or remove                  |
| Duplicate records  | Same customer listed twice   | Deduplicate                   |
| Inconsistent data  | "NY" vs "New York"           | Standardize to common format  |

### Step 3: Transformation
Convert data into formats suitable for mining. This includes normalization (scaling values to a range), discretization (converting continuous values to categories), feature selection, and dimensionality reduction.

### Step 4: Data Mining
Apply algorithms to discover patterns. This is the core step, covered in detail below.

### Step 5: Interpretation / Evaluation
Assess the discovered patterns for validity, novelty, usefulness, and understandability. Patterns that are trivial (e.g., "most customers buy bread") or random are discarded.

## Data Mining Techniques

### 1. Classification

**Goal:** Assign a label to a data point based on past labeled examples.

**How it works:** Train a model on a labeled dataset (where the class is known), then use the model to predict the class of new, unlabeled data.

**Example:** Email spam detection. Train on emails labeled "spam" or "not spam." Predict whether a new email is spam.

```
+-----------------------------+
| Input: Email features       |
| - Contains "FREE"           |
| - Contains "click here"     |
| - Contains image/text ratio |
| - Sender not in contacts    |
+-----------------------------+
             |
             v
+-----------------------------+
| Classification Model        |
| (Trained on labeled emails) |
+-----------------------------+
             |
             v
+-----------------------------+
| Output: "Spam" or "Not Spam"|
+-----------------------------+
```

**Algorithms:** Decision Trees, Random Forest, Support Vector Machines (SVM), Naive Bayes, k-Nearest Neighbors (k-NN), Neural Networks.

### 2. Clustering

**Goal:** Group similar data points together without using pre-existing labels (unsupervised learning).

**How it works:** The algorithm finds natural groupings in the data based on feature similarity. Data points within a cluster are more similar to each other than to points in other clusters.

**Example:** Customer segmentation in marketing. Group customers by purchasing behavior, demographics, and browsing history. Each cluster represents a customer segment (e.g., "budget shoppers", "premium buyers", "impulse buyers").

```
Before Clustering:                   After Clustering:
                                         Cluster A
    .    .   .   .     .                 .  .  .
      .     .       .                    .   .
   .       .     .   .                         Cluster B
      .         .                              .  .
          .   .      .                .  .        .
                                         Cluster C
                                              .   .
                                            .     .
```

**Algorithms:** k-Means, DBSCAN, Hierarchical Clustering, Gaussian Mixture Models.

### 3. Association Rule Mining

**Goal:** Find relationships between items in large transaction datasets.

**How it works:** Identify items that frequently appear together. Rules take the form: `X -> Y` (if X occurs, Y is likely to occur).

**Key metrics:**

| Metric       | Formula                          | Meaning                              |
|--------------|----------------------------------|--------------------------------------|
| Support      | (X and Y count) / (Total trans)  | How often the rule applies           |
| Confidence   | (X and Y count) / (X count)      | How often Y happens when X happens   |
| Lift         | Confidence / (Y probability)     | How much better than random          |

**Example -- Market Basket Analysis:**

Transaction data:
| Transaction | Items                              |
|-------------|------------------------------------|
| T1          | bread, milk, diapers               |
| T2          | bread, diapers, beer, eggs        |
| T3          | milk, diapers, beer, cola         |
| T4          | bread, milk, diapers, beer        |
| T5          | bread, milk, eggs, cola           |

Rule: `{diapers} -> {beer}`

- Support: `{diapers, beer}` appears in 3/5 transactions = 0.6
- Confidence: `{diapers, beer}` / `{diapers}` = 3/4 = 0.75
- Lift: 0.75 / (3/5) = 1.25 (positive correlation)

**Algorithm:** Apriori (details below).

### 4. Regression

**Goal:** Predict a continuous numeric value based on input features.

**How it works:** Learn a function f(x) that maps input variables to a numeric output.

**Example:** Predicting house prices based on square footage, number of bedrooms, location, and age.

```
Real estate data:
+--------+-------+------+------+----------+
| SqFt   | Bed   | Bath | Age  | Price    |
+--------+-------+------+------+----------+
| 1500   | 3     | 2    | 10   | $350,000 |
| 2000   | 4     | 3    | 5    | $485,000 |
| 1200   | 2     | 1    | 20   | $220,000 |
| ...    | ...   | ...  | ...  | ...      |
+--------+-------+------+------+----------+

Goal: Predict Price = f(SqFt, Bed, Bath, Age)
```

**Algorithms:** Linear Regression, Polynomial Regression, Decision Tree Regression, Neural Networks.

### 5. Anomaly Detection

**Goal:** Identify rare items, events, or observations that differ significantly from the majority of the data.

**How it works:** Model the "normal" behavior and flag points that deviate from it.

**Example:** Credit card fraud detection. A card used in New York at 10 AM and in London at 11 AM is flagged as anomalous.

```
Normal transactions:    Anomalous transaction:
. . . . . . . . .
. . . . . . . . .           X (fraudulent)
. . . . . . . . .
. . . . . . . . .
```

**Algorithms:** Isolation Forest, One-Class SVM, Local Outlier Factor (LOF), Z-score.

## Supervised vs Unsupervised Learning

| Aspect              | Supervised Learning            | Unsupervised Learning         |
|---------------------|--------------------------------|-------------------------------|
| Training data       | Labeled (input + output)       | Unlabeled (input only)        |
| Goal                | Predict output for new input   | Find hidden structure         |
| Techniques          | Classification, Regression     | Clustering, Association       |
| Evaluation          | Compare prediction to label    | Subjective (internal metrics) |
| Example algorithm   | Decision Tree                  | k-Means                       |
| Analogy             | Learn with a teacher           | Learn by exploring            |

## Overview of Key Algorithms

### Apriori Algorithm (Association Rule Mining)

**Purpose:** Find frequent itemsets and generate association rules.

**How it works:**
1. Generate candidate itemsets of size k.
2. Count support for each candidate by scanning the database.
3. Prune itemsets with support below the minimum support threshold.
4. Generate candidates for k+1 from frequent k-itemsets.
5. Repeat until no new candidates are found.

**Key property (Apriori principle):** If an itemset is frequent, then all of its subsets must also be frequent. Conversely, if an itemset is infrequent, all its supersets can be pruned without counting.

```
Dataset transactions:

T1: {A, B, D}
T2: {A, C, D}
T3: {B, C, D}
T4: {A, B, C}
T5: {A, B, C, D}

Min support = 3/5 = 0.6

Step 1: Count single items
A: 4, B: 4, C: 3, D: 4     All are frequent

Step 2: Generate pairs
AB: 3, AC: 3, AD: 3, BC: 2 (pruned), BD: 3, CD: 2 (pruned)

Step 3: Generate triples from frequent pairs
ABD: {A,B,D} appears in T1, T5 = 2 (pruned)
ACD: {A,C,D} appears in T2 = 1 (pruned)
ABC: {A,B,C} appears in T4, T5 = 2 (pruned)

Frequent itemsets: {A}, {B}, {C}, {D}, {A,B}, {A,C}, {A,D}, {B,D}
```

### k-Means Clustering

**Purpose:** Partition n data points into k clusters.

**Algorithm:**
1. Choose k initial centroids (randomly or using heuristics).
2. Assign each data point to the nearest centroid.
3. Recompute centroids as the mean of all points in the cluster.
4. Repeat steps 2-3 until convergence (centroids stop moving significantly).

```
Initial centroids (k=2):           After first iteration:
  C1 = (0,0), C2 = (5,5)            C1 = (1,1), C2 = (6,6)

  . . . . . . . . . .                Cluster 1: . . .
  . . . . . . . . . .                Cluster 2:     . . . . . .
  . . . . . . . . . .                          .
                                            .
```

**Challenges:** Choosing k, sensitivity to initial centroids, works best with spherical clusters.

### Decision Trees (Classification)

**Purpose:** Create a tree-like model of decisions based on feature values.

**Structure:**
- **Internal nodes:** Test a feature.
- **Branches:** Outcome of the test.
- **Leaves:** Class label.

```
Example: Should we play tennis?

                  Outlook
               /    |     \
            Sunny  Overcast  Rain
            /        |        \
       Humidity    Yes       Wind
       /     \               /   \
    High    Normal         Strong  Weak
     |        |              |      |
     No      Yes             No    Yes
```

**How it works (ID3 algorithm):**
1. Select the feature that best splits the data (highest information gain / lowest Gini impurity).
2. Create a node for that feature.
3. Partition the data by the feature's values.
4. Recursively build subtrees for each partition.
5. Stop when all data in a partition has the same class, or no features remain.

**Advantages:** Easy to interpret, handles both numeric and categorical data, requires little preprocessing.

## Summary

- Data mining discovers patterns in large datasets.
- The KDD process has 5 stages: Selection, Preprocessing, Transformation, Mining, Evaluation.
- Major techniques: classification (labeled prediction), clustering (grouping), association (relationship discovery), regression (numeric prediction), anomaly detection (outlier identification).
- Supervised learning requires labeled data; unsupervised learning does not.
- Key algorithms: Apriori (frequent itemsets), k-Means (clustering), Decision Trees (classification).

---

## Practice Problems

1. Explain the KDD process. For each step, describe what happens using a concrete example.
   <details>
   <summary>Show Answer</summary>
   Knowledge Discovery in Databases (KDD) process: (1) **Selection** — choose relevant data (e.g., select customer purchase history from the database). (2) **Preprocessing** — clean data (remove null values, fix inconsistencies). (3) **Transformation** — convert data into suitable format (e.g., normalize numeric values, create date parts). (4) **Data Mining** — apply algorithms (e.g., Apriori to find frequent itemsets). (5) **Interpretation/Evaluation** — validate patterns (e.g., "customers who buy milk also buy bread" has 70% confidence).
   </details>
2. What is the difference between supervised and unsupervised learning? Give two algorithms for each.
   <details>
   <summary>Show Answer</summary>
   **Supervised learning** uses labeled training data to predict outcomes. Algorithms: Linear Regression, Decision Trees, Random Forest, SVM. **Unsupervised learning** finds patterns in unlabeled data without predefined outputs. Algorithms: k-Means Clustering, Apriori, Hierarchical Clustering, DBSCAN. Example: Predicting house prices (supervised) vs. segmenting customers into groups (unsupervised).
   </details>
3. Describe the Apriori algorithm. Given transactions [T1: {milk, bread, eggs}, T2: {bread, butter}, T3: {milk, bread, butter}, T4: {milk, eggs}], find all frequent itemsets with minimum support of 0.5.
   <details>
   <summary>Show Answer</summary>
   Apriori finds frequent itemsets by iteratively generating candidate itemsets of size k+1 from frequent itemsets of size k, pruning those failing minimum support.
   Support threshold: 0.5 × 4 = 2 transactions.
   **Step 1:** Count single-item support: milk=3, bread=3, eggs=2, butter=2. All meet min support (≥2). **Step 2:** Generate size-2 candidates: {milk,bread}=2, {milk,butter}=1, {milk,eggs}=2, {bread,butter}=2, {bread,eggs}=1, {butter,eggs}=0. Frequent: {milk,bread}=2, {milk,eggs}=2, {bread,butter}=2. **Step 3:** Generate size-3 candidates from size-2: {milk,bread,eggs}=1 (fails support). **Frequent itemsets:** {milk}=3, {bread}=3, {eggs}=2, {butter}=2, {milk,bread}=2, {milk,eggs}=2, {bread,butter}=2.
   </details>
4. How does k-Means clustering work? What is the elbow method used for?
   <details>
   <summary>Show Answer</summary>
   k-Means clustering: (1) Choose k initial centroids randomly. (2) Assign each data point to the nearest centroid. (3) Recompute centroids as the mean of all points in each cluster. (4) Repeat steps 2–3 until centroids stabilize (no change in assignments). The **elbow method** plots the within-cluster sum of squares (WCSS) against k values. The "elbow" point (where WCSS improvement slows) indicates the optimal number of clusters.
   </details>
5. Draw a decision tree for a loan approval system based on features: income, credit score, and employment status.
   <details>
   <summary>Show Answer</summary>
   ```
                     [Loan Application]
                            |
                    Income >= $50K?
                    /              \
                 Yes                 No
                  |                   |
          Credit Score >= 700?   Credit Score >= 750?
           /          \             /           \
         Yes          No          Yes            No
          |            |           |              |
       Employed?   Rejected   Employed?      Rejected
       /      \               /      \
    Yes       No            Yes       No
     |         |             |         |
  Approved  Rejected     Approved  Rejected
   ```
   The tree splits on the most discriminating feature first, creating decision rules at each node.
   </details>
