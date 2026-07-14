# Population and Sample

**Course:** Probability and Statistics  
**Module:** 4 | **Lecture:** 1  
**Date:** 04-Sep-2026  
**Faculty:** RITTIKA BHATTACHARYA  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Fundamentals of Mathematical Statistics (Gupta & Kapoor) Chapter: 14

## Notes

### 1. Introduction to Population and Sample

In statistics, we are often interested in learning something about a large group of individuals or objects. However, examining every single member of that group is usually impractical. This lecture introduces the fundamental concepts that allow us to draw conclusions about a large group by studying a smaller part of it.

---

### 2. Population

A **population** is the entire collection of all individuals, objects, or measurements of interest in a statistical study.

#### 2.1 Finite Population

A population with a countable (and usually limited) number of elements.

- **Definition:** A population is finite if the number of elements N is a fixed, countable number.
- **Examples:**
  - All students enrolled in a university this semester (N = 25,000).
  - All light bulbs produced by a factory in a specific day (N = 10,000).
  - All voting-age citizens in a country.
- **Key point:** In a finite population, it is theoretically possible (though often impractical) to enumerate every single element.

#### 2.2 Infinite Population

A population with an uncountable or unlimited number of elements.

- **Definition:** A population is infinite if the number of elements is either unlimited or cannot be counted.
- **Examples:**
  - All possible tosses of a coin (the coin could be tossed forever).
  - All possible measurements of the boiling point of water (infinite continuum of values).
  - All possible outcomes of a manufacturing process if it runs indefinitely.
- **Key point:** For infinite populations, it is impossible to enumerate every element, even in theory.

---

### 3. Sample

A **sample** is a subset of the population selected for study. The sample is used to gather information about the population without examining the entire population.

- **Size of sample:** Denoted by `n` (the number of elements in the sample).
- **Goal:** The sample should be representative of the population so that conclusions drawn from the sample (called inferences) can be extended to the population.

#### Why Sampling is Necessary

| Reason | Explanation |
|--------|-------------|
| Cost | Examining the entire population is often prohibitively expensive. |
| Time | Collecting data from the whole population takes too long; decisions may be needed quickly. |
| Destructive testing | Some tests destroy the item (e.g., testing the lifetime of a light bulb). If we test all bulbs, there are none left to sell. |
| Accessibility | Some populations are infinite or hypothetical, making a complete enumeration impossible. |
| Accuracy | A well-designed sample can sometimes yield more accurate results than a poorly conducted census (due to reduced non-sampling errors). |

---

### 4. Census vs Sample Survey

| Feature | Census | Sample Survey |
|---------|--------|---------------|
| **Definition** | Collection of data from every member of the population. | Collection of data from a subset (sample) of the population. |
| **Coverage** | Complete enumeration (100% of population). | Partial enumeration. |
| **Cost** | Very high. | Relatively low. |
| **Time required** | Long. | Short. |
| **Accuracy** | Subject to non-sampling errors only (no sampling error). | Subject to both sampling and non-sampling errors. |
| **Feasibility** | Often impractical for large or infinite populations. | Practical and widely used. |
| **Example** | National census of population conducted by the government. | Opinion poll surveying 1,000 voters to predict election results. |

---

### 5. Sampling Frame

A **sampling frame** is the list of all elements in the population from which the sample is actually drawn.

- The sampling frame should ideally match the population of interest.
- **Examples:**
  - If the population is "all registered voters in a city", the voter registration list is the sampling frame.
  - If the population is "all students at a university", the university's enrollment database is the sampling frame.
- **Sampling frame error:** When the frame does not accurately represent the population (e.g., the voter list is outdated and missing some voters).

---

### 6. Parameter vs Statistic

This is one of the most fundamental distinctions in statistics.

| Concept | Definition | Notation | Applies to |
|---------|------------|----------|------------|
| **Parameter** | A numerical characteristic of the **population**. | Greek letters (e.g., `mu`, `sigma`, `p`) | Population |
| **Statistic** | A numerical characteristic of the **sample**. | Roman letters (e.g., `bar{x}`, `s`, `hat{p}`) | Sample |

#### Common Parameters and Their Corresponding Statistics

| Parameter (Population) | Statistic (Sample) |
|------------------------|--------------------|
| `mu` = population mean | `bar{x}` = sample mean |
| `sigma^2` = population variance | `s^2` = sample variance |
| `sigma` = population standard deviation | `s` = sample standard deviation |
| `p` = population proportion | `hat{p}` = sample proportion |
| `N` = population size | `n` = sample size |

**Key idea:** We use statistics (computed from the sample) to estimate or make inferences about parameters (of the population).

---

### 7. Worked Examples

#### Example 1: Identifying Population and Sample

A researcher wants to study the average height of adult women in India. She measures the heights of 500 adult women selected from cities across India.

- **Population:** All adult women in India.
- **Sample:** The 500 adult women selected for the study.
- **Parameter:** The true average height of all adult women in India (denoted `mu`).
- **Statistic:** The average height of the 500 women in the sample (denoted `bar{x}`).

---

#### Example 2: Identifying Parameter and Statistic

A factory produces 50,000 light bulbs per day. The quality control team tests 200 bulbs and finds that 12 of them are defective.

- **Population:** All 50,000 light bulbs produced that day (finite population).
- **Sample:** The 200 bulbs tested.
- **Parameter:** The true proportion of defective bulbs in the entire day's production (denoted `p`).
- **Statistic:** The sample proportion of defective bulbs = `12/200 = 0.06` or 6% (denoted `hat{p}`).

---

#### Example 3: Finite vs Infinite Population

For each of the following, state whether the population is finite or infinite.

(a) The lifetimes of all batteries of a particular brand.
    - **Answer:** Infinite (the production process can theoretically continue forever; also, testing all batteries is destructive).

(b) The number of books in all libraries in New York City.
    - **Answer:** Finite (there is a fixed, countable number of libraries and books, though it may be large).

(c) The outcomes of rolling a die repeatedly.
    - **Answer:** Infinite (the die can be rolled an unlimited number of times).

---

#### Example 4: Census vs Sample Survey

A pharmaceutical company wants to determine the effectiveness of a new drug.

- Would a census or sample survey be appropriate?
- **Answer:** A sample survey is appropriate. A census would require administering the drug to every person in the population, which is impractical and unethical without first establishing safety and efficacy. Clinical trials use carefully selected samples.

---

### 8. Key Takeaways

1. The **population** is the entire group of interest; the **sample** is the subset we actually study.
2. A **parameter** describes the population; a **statistic** describes the sample.
3. **Sampling** is necessary due to cost, time, destructiveness, and infeasibility of complete enumeration.
4. The **sampling frame** is the actual list from which the sample is drawn; it should match the target population.

---

## Practice Problems

**Problem 1:** A political pollster wants to estimate the proportion of voters who support a particular candidate in an upcoming election. She randomly calls 2,000 registered voters and asks their preference.

(a) What is the population?
(b) What is the sample?
(c) What is the parameter of interest?
(d) What is the corresponding statistic?

   <details>
   <summary>Show Answer</summary>
   **Problem 1:** (a) All registered voters. (b) The 2,000 voters called. (c) True proportion of all voters supporting the candidate (`p`). (d) Sample proportion (`hat{p}`) from the 2,000 respondents.
   </details>

**Problem 2:** State whether the following populations are finite or infinite:
(a) The number of fish in the Atlantic Ocean.
(b) The possible outcomes of measuring the temperature at noon in a city (in Celsius).
(c) The number of students in all universities in Japan.
(d) The sequence of heads and tails when a coin is flipped indefinitely.

   <details>
   <summary>Show Answer</summary>
   **Problem 2:** (a) Finite (though very large and uncountable in practice, the number is theoretically finite). (b) Infinite (temperature is a continuous measurement). (c) Finite. (d) Infinite.
   </details>

**Problem 3:** A bakery produces 5,000 loaves of bread each day. The baker tests 50 loaves to check the quality (taste, texture, appearance). He finds that 3 loaves are substandard.

(a) What is the population? Is it finite or infinite?
(b) What is the sample?
(c) What is the parameter (define in words)?
(d) What is the statistic (compute the proportion)?

   <details>
   <summary>Show Answer</summary>
   **Problem 3:** (a) All 5,000 loaves produced that day; finite. (b) The 50 loaves tested. (c) The true proportion of substandard loaves among all 5,000 loaves. (d) `hat{p} = 3/50 = 0.06`.
   </details>

**Problem 4:** Explain why a census is usually not preferred over a sample survey for quality control in a manufacturing plant that produces thousands of items daily.

   <details>
   <summary>Show Answer</summary>
   **Problem 4:** A census would require testing every item, which is destructive for many quality tests (e.g., testing the breaking strength of a loaf would destroy it). It would also be too expensive and time-consuming.
   </details>

**Problem 5:** Distinguish between a parameter and a statistic. Give one example of each.
   <details>
   <summary>Show Answer</summary>
   **Problem 5:** A parameter is a numerical measure describing a population (e.g., `mu` = average height of all Indians). A statistic is a numerical measure describing a sample (e.g., `bar{x}` = average height of 500 sampled Indians).
   </details>
