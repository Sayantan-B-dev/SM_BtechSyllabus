# Application of Bayes Theorem

**Course:** Probability and Statistics  
**Module:** 2 | **Lecture:** 5  
**Date:** 07-Aug-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 2  
**Learning Methodology:** Flip Class  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 4.14

## Notes

### Introduction

Bayes' Theorem is not just a theoretical result -- it has profound practical applications across many fields. This lecture explores real-world applications including spam filtering, medical diagnosis, machine learning (Naive Bayes), and the famous Monty Hall problem. Understanding these applications reveals why Bayes' Theorem is considered one of the most important ideas in data science.

---

### 1. Application 1: Medical Diagnosis

**Context:** Medical tests are never perfect. They have:
- **Sensitivity:** `P(positive | disease)` -- probability test catches the disease
- **Specificity:** `P(negative | no disease)` -- probability test correctly clears healthy people
- **Prevalence:** `P(disease)` -- how common the disease is in the population

The key insight from Bayes' Theorem is that even with a highly accurate test, a positive result may not mean you are likely to have the disease if the disease is rare.

**Extended Example -- Sequential Testing:**

**Problem:** A disease affects 0.5% of the population. Test T1 has sensitivity 98% and specificity 90%. Test T2 (a confirmatory test) has sensitivity 99% and specificity 99%. A person takes Test T1 and tests positive. They then take Test T2 and also test positive. What is the probability they actually have the disease?

**Solution:**

Let D = person has the disease.

**After Test T1 (positive):**
`P(D) = 0.005`
`P(T1+ | D) = 0.98`
`P(T1+ | D') = 0.10`

`P(T1+) = 0.005*0.98 + 0.995*0.10 = 0.0049 + 0.0995 = 0.1044`

`P(D | T1+) = 0.0049/0.1044 = 0.04693`

So after the first positive test, there is only about a 4.7% chance of having the disease.

**After Test T2 (also positive):**
Now we use `P(D | T1+) = 0.04693` as our new prior.

`P(D) = 0.04693` (updated prior)
`P(D') = 0.95307`
`P(T2+ | D) = 0.99`
`P(T2+ | D') = 0.01`

`P(T2+) = 0.04693*0.99 + 0.95307*0.01 = 0.04646 + 0.00953 = 0.05599`

`P(D | T1+ and T2+) = 0.04646/0.05599 = 0.8298`

After two positive tests, the probability jumps to about 83%. This shows how sequential Bayesian updating dramatically improves diagnostic accuracy.

---

### 2. Application 2: Spam Filtering (Naive Bayes)

**Context:** Email spam filters use Bayes' Theorem to classify emails as spam or not spam based on the words they contain.

**Problem:** Suppose we have the following data from a training set of 1000 emails:
- 400 emails are spam (S), 600 are not spam (NS)
- Among spam emails: 60% contain the word "free", 40% do not
- Among non-spam emails: 5% contain the word "free", 95% do not
- Among spam emails: 30% contain the word "money", 70% do not
- Among non-spam emails: 2% contain the word "money", 98% do not

An incoming email contains both "free" and "money". What is the probability it is spam?

**Solution using Naive Bayes:**

The "naive" assumption is that the words appear independently within each class (spam or not spam). While this assumption is rarely true in reality, the classifier still works well.

**Priors:**
`P(S) = 400/1000 = 0.40`
`P(NS) = 600/1000 = 0.60`

**Likelihoods:**
`P(free | S) = 0.60`,   `P(money | S) = 0.30`
`P(free | NS) = 0.05`, `P(money | NS) = 0.02`

**Naive assumption (conditional independence):**
`P(free and money | S) = P(free | S) * P(money | S) = 0.60 * 0.30 = 0.18`
`P(free and money | NS) = P(free | NS) * P(money | NS) = 0.05 * 0.02 = 0.001`

**Evidence:**
`P(free and money) = P(S)*0.18 + P(NS)*0.001 = 0.40*0.18 + 0.60*0.001 = 0.072 + 0.0006 = 0.0726`

**Posterior:**
`P(S | free and money) = 0.072 / 0.0726 = 0.9917`

So there is a 99.17% probability that this email is spam.

**Why the "naive" assumption matters:**
In reality, words like "free" and "money" often appear together in spam emails, so their occurrences are not independent. However, the Naive Bayes classifier typically still performs well for text classification tasks. If we had more training data, we could directly estimate `P(free and money | S)` without the independence assumption.

---

### 3. Application 3: Machine Learning Classification (Naive Bayes Classifier)

**General framework:**

Naive Bayes is a family of simple probabilistic classifiers based on applying Bayes' Theorem with strong (naive) independence assumptions between the features.

**The classification rule:**

Given a data point with features `x_1, x_2, ..., x_n`, the classifier assigns it to the class `C_k` that maximizes the posterior probability:

`P(C_k | x_1, x_2, ..., x_n) proportional to P(C_k) * prod_{i=1}^{n} P(x_i | C_k)`

The class with the highest posterior probability is chosen:

`Predicted class = argmax_k [P(C_k) * prod_{i=1}^{n} P(x_i | C_k)]`

**Advantages of Naive Bayes:**
- Simple and fast to train and predict
- Performs well even with limited training data
- Handles high-dimensional data well
- Works well for text classification, spam filtering, sentiment analysis

**Disadvantages:**
- The independence assumption is almost always violated
- Cannot learn interactions between features
- Zero probability problem (handled by smoothing techniques like Laplace smoothing)

---

### 4. Application 4: Factory with Multiple Production Units

**Problem:** A manufacturing company has four production units (Plants 1, 2, 3, and 4) that produce the same product. The distribution of production and defect rates are:

| Plant | Share of Production | Defect Rate |
|---|---|---|
| Plant 1 | 35% | 2.5% |
| Plant 2 | 25% | 3.0% |
| Plant 3 | 25% | 4.0% |
| Plant 4 | 15% | 1.0% |

(a) If a randomly selected item is defective, what is the probability it came from Plant 3?
(b) If two items are randomly selected (independently) and both are defective, what is the probability both came from Plant 3?
(c) The company implements quality improvements. After improvements, defect rates become: Plant 1: 1.5%, Plant 2: 2.0%, Plant 3: 2.5%, Plant 4: 0.5%. Production shares remain the same. A defective item is found. What is the probability it came from Plant 3 now?

**Solution (a):**

Let `P_i` = event item from Plant i (i = 1, 2, 3, 4). Let D = event item is defective.

**Step 1:** Priors.
`P(P_1) = 0.35`, `P(P_2) = 0.25`, `P(P_3) = 0.25`, `P(P_4) = 0.15`

**Step 2:** Likelihoods.
`P(D | P_1) = 0.025`, `P(D | P_2) = 0.030`, `P(D | P_3) = 0.040`, `P(D | P_4) = 0.010`

**Step 3:** Total probability of defect.
`P(D) = 0.35(0.025) + 0.25(0.030) + 0.25(0.040) + 0.15(0.010)`
`= 0.00875 + 0.00750 + 0.01000 + 0.00150`
`= 0.02775`

**Step 4:** Posterior for Plant 3.
`P(P_3 | D) = 0.25(0.040) / 0.02775 = 0.010/0.02775 = 0.36036`

About 36.04% chance it came from Plant 3.

**Solution (b):**

We want the probability that both defective items came from Plant 3.

Probability both are from Plant 3 AND both are defective:
`P(P_3 and D) = 0.25 * 0.04 = 0.01` for one item.
For two independent items: `(0.01)^2 = 0.0001`

Probability both are defective (regardless of source):
`P(D_1 and D_2) = (0.02775)^2 = 0.0007701` (using independence)

`P(both from P_3 | both defective) = 0.0001 / 0.0007701 = 0.1299`

So about 13% chance both came from Plant 3, even though Plant 3 has the highest defect rate. This is because the other plants together contribute most defects.

**Solution (c):**

After improvements:
`P(D | P_1) = 0.015`, `P(D | P_2) = 0.020`, `P(D | P_3) = 0.025`, `P(D | P_4) = 0.005`

`P(D) = 0.35(0.015) + 0.25(0.020) + 0.25(0.025) + 0.15(0.005)`
`= 0.00525 + 0.00500 + 0.00625 + 0.00075`
`= 0.01725`

`P(P_3 | D) = 0.00625 / 0.01725 = 0.3623`

Despite lower defect rates overall, the posterior for Plant 3 is similar (36.23%). This is because Plant 3's defect rate improved proportionally less than others.

---

### 5. Application 5: Monty Hall Problem Revisited (with Bayes)

**Problem:** On the game show "Let's Make a Deal," there are three doors. Behind one door is a car; behind the other two are goats. You pick a door (say, Door 1). The host, Monty Hall, who knows what is behind the doors, opens another door (say, Door 3) that has a goat. He then asks: "Do you want to switch to Door 2?" Should you switch?

**Solution using Bayes' Theorem:**

Let `C_i` = event that the car is behind Door i (i = 1, 2, 3).
Let `H_3` = event that Monty opens Door 3.

**Priors (before any doors are opened):**
`P(C_1) = P(C_2) = P(C_3) = 1/3`

**Likelihoods (probability that Monty opens Door 3 given where the car is):**
- If car behind Door 1: Monty can open Door 2 or Door 3, both with goats. He chooses randomly.
  `P(H_3 | C_1) = 1/2`
- If car behind Door 2: Monty must open Door 3 (the only goat door that is not your pick).
  `P(H_3 | C_2) = 1`
- If car behind Door 3: Monty cannot open Door 3 (it has the car).
  `P(H_3 | C_3) = 0`

**Evidence:**
`P(H_3) = P(C_1)*P(H_3|C_1) + P(C_2)*P(H_3|C_2) + P(C_3)*P(H_3|C_3)`
`= (1/3)(1/2) + (1/3)(1) + (1/3)(0)`
`= 1/6 + 1/3 + 0`
`= 1/2`

**Posteriors:**
`P(C_1 | H_3) = (1/3)(1/2) / (1/2) = 1/3`
`P(C_2 | H_3) = (1/3)(1) / (1/2) = 2/3`
`P(C_3 | H_3) = (1/3)(0) / (1/2) = 0`

**Conclusion:** Switching doubles your chance of winning from 1/3 to 2/3. You should switch.

**Intuition:** When you initially pick Door 1, there is a 1/3 chance the car is behind your door and a 2/3 chance it is behind one of the other two doors. Monty's action of opening a goat door gives you information: if the car were behind Door 2, Monty would be forced to open Door 3 (100% chance), but if the car were behind your door, Monty would only open Door 3 half the time. So the fact that he opened Door 3 is more likely if the car is behind Door 2.

---

### 6. Application 6: Lie Detection

**Problem:** A polygraph (lie detector) test is 85% accurate when a person is lying (it correctly identifies lies 85% of the time) and 80% accurate when a person is telling the truth. In a certain investigation, it is estimated that 10% of the suspects being tested are actually lying. If a suspect tests positive (classified as lying), what is the probability that they are actually lying?

**Solution:**

Let L = event that the suspect is lying, T = event that the test says lying.

**Priors:** `P(L) = 0.10`, `P(L') = 0.90`

**Likelihoods:** `P(T | L) = 0.85`, `P(T | L') = 0.20` (since 80% accuracy for truth means 20% false positive)

**Evidence:**
`P(T) = 0.10(0.85) + 0.90(0.20) = 0.085 + 0.18 = 0.265`

**Posterior:**
`P(L | T) = 0.085 / 0.265 = 0.3208`

Even with a positive lie detector result, there is only a 32.08% chance the suspect is actually lying. This illustrates why polygraph results are often inadmissible in court.

---

### 7. Application 7: Insurance Risk Assessment

**Problem:** An insurance company classifies drivers into three risk categories:
- High risk: 20% of drivers, accident probability 15%
- Medium risk: 50% of drivers, accident probability 8%
- Low risk: 30% of drivers, accident probability 3%

(a) What is the overall probability that a randomly selected driver has an accident?
(b) If a driver had an accident last year, what is the probability they are in the high-risk category?

**Solution:**

Let H, M, L = driver is high, medium, or low risk.
Let A = driver has an accident.

(a) `P(A) = P(H)*P(A|H) + P(M)*P(A|M) + P(L)*P(A|L)`
`= 0.20(0.15) + 0.50(0.08) + 0.30(0.03)`
`= 0.03 + 0.04 + 0.009`
`= 0.079`

Overall accident probability is 7.9%.

(b) `P(H | A) = 0.20(0.15) / 0.079 = 0.03 / 0.079 = 0.3797`

So about 38% of accident-involved drivers are from the high-risk category, even though high-risk drivers make up only 20% of all drivers.

---

### Summary of Applications

| Application | Key Insight |
|---|---|
| Medical Diagnosis | Even with good tests, rare diseases produce many false positives; sequential testing improves accuracy |
| Spam Filtering | Naive Bayes classifier combines word probabilities under conditional independence assumption |
| Naive Bayes Classifier | `argmax_k P(C_k) * prod P(x_i | C_k)` -- simple but effective classification |
| Quality Control | Bayes identifies which production unit is most likely responsible for defects |
| Monty Hall | Bayesian reasoning resolves a famous counterintuitive probability puzzle |
| Lie Detection | Imperfect tests can produce misleading posterior probabilities |
| Insurance | Prior risk categories combined with data yields fairer premium assessments |

---

### The Big Picture: Bayesian vs. Frequentist Thinking

- **Frequentist:** Probability is the long-run frequency of events. Parameters are fixed (unknown) constants.
- **Bayesian:** Probability represents degree of belief. Parameters have probability distributions. Bayes' Theorem provides a mathematical framework for updating beliefs as new data arrives.

Bayesian methods are increasingly dominant in machine learning, artificial intelligence, data science, and many scientific fields because they naturally incorporate prior knowledge and update with evidence.

---

## Practice Problems

1. A spam filter uses two keywords: "offer" and "congratulations". Among spam emails, 70% contain "offer" and 40% contain "congratulations". Among non-spam emails, 10% contain "offer" and 5% contain "congratulations". Assume 30% of all emails are spam. An email contains both "offer" and "congratulations". Using the Naive Bayes assumption, find the probability it is spam.

   <details>
   <summary>Show Answer</summary>
   1. `P(S|O&C) = 0.30*(0.70*0.40) / [0.30*(0.70*0.40) + 0.70*(0.10*0.05)] = 0.084/0.0875 = 0.96`. About 96% probability of spam.
   </details>

2. Three machines M1, M2, M3 produce 40%, 35%, and 25% of the items in a factory respectively. Their defect rates are 2%, 3%, and 1.5% respectively. A random item is defective. Find the probability it came from M2.

   <details>
   <summary>Show Answer</summary>
   2. `P(M2|D) = 0.35*0.03 / (0.40*0.02 + 0.35*0.03 + 0.25*0.015) = 0.0105/0.02125 = 0.4941`
   </details>

3. In the classic Monty Hall problem, suppose there are FOUR doors instead of three. One hides a car, three hide goats. You pick Door 1. Monty opens two doors with goats (say, Doors 3 and 4). What is the probability the car is behind Door 2? Should you switch?

   <details>
   <summary>Show Answer</summary>
   3. With 4 doors: `P(C_1) = 1/4`. Monty opens 2 goat doors. `P(C_1|open) = (1/4 * 1) / [(1/4)(1) + (1/4)(1) + ...]`. Actually: `P(H|C_1) = C(3,2)/C(3,2) = 1` (Monty opens any 2 of the 3 goat doors). `P(H|C_2) = C(2,2)/C(3,2) = 1/3` (must choose 2 specific goat doors from the 3 remaining). Similar for C_3, C_4. `P(H) = (1/4)(1) + 3*(1/4)(1/3) = 1/4 + 1/4 = 1/2`. `P(C_1|H) = (1/4)/0.5 = 1/2`. `P(C_2|H) = (1/4)(1/3)/0.5 = 1/6`. Switching to any specific remaining door gives 1/6, but switching to one of the two unopened doors gives 1/6 + 1/6 = 1/3. Better to switch.
   </details>

4. A weather forecaster predicts rain or sunshine. When it will actually rain, the forecaster predicts rain 90% of the time. When it will be sunny, the forecaster predicts rain 15% of the time. In the region, it rains 25% of the days. If the forecaster predicts rain, what is the probability it will actually rain?

   <details>
   <summary>Show Answer</summary>
   4. `P(Rain|Pred) = (0.25*0.90) / (0.25*0.90 + 0.75*0.15) = 0.225/0.3375 = 2/3`
   </details>

5. An AI system classifies images as "cat" or "dog". It is known that 45% of images in the test set are cats and 55% are dogs. The classifier has the following performance:
   - For cat images: correctly identifies 92% as cat, 8% as dog.
   - For dog images: correctly identifies 88% as dog, 12% as cat.
   If the classifier says an image is a cat, what is the probability it is actually a cat?
   <details>
   <summary>Show Answer</summary>
   5. `P(Cat|Classified Cat) = (0.45*0.92) / (0.45*0.92 + 0.55*0.12) = 0.414/0.48 = 0.8625`
   </details>
