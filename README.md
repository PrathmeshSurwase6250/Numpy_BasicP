# NumPy & Statistics Practice

This repository contains my practice programs and problem-solving exercises using **Python, NumPy, and Statistics**.

The main goal of this practice is to build a strong foundation in **NumPy, descriptive statistics, data analysis, and ML-oriented statistical concepts**.

## 🟢 Level 1 — NumPy Basics

Practiced the fundamental NumPy operations:

* Creating NumPy arrays using `np.array()`
* Creating sequences using `np.arange()`
* Creating arrays of zeros using `np.zeros()`
* Creating arrays of ones using `np.ones()`
* Checking array:

  * Shape
  * Size
  * Number of dimensions
  * Data type
* Reshaping arrays using `reshape()`
* Array indexing
* Array slicing
* Element-wise multiplication
* Element-wise addition
* Finding:

  * Minimum
  * Maximum
  * Sum
  * Mean

### Example

```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)
```

## 🟡 Level 2 — NumPy Concept Building

Practiced understanding how NumPy arrays behave rather than only memorizing syntax.

Topics covered:

* Difference between 1D and 2D arrays
* Understanding array shapes
* Reshaping rules
* Number of elements required for reshaping
* Element-wise operations
* Boolean conditions
* Boolean indexing
* Filtering values from arrays

### Example

```python
a = np.array([10, 20, 30, 40, 50])

print(a[a > 25])
```

Output:

```text
[30 40 50]
```

Also practiced filtering values based on conditions such as:

* Marks greater than 60
* Values between 40 and 70

## 🟠 Level 3 — Statistics

Practiced the fundamental measures of central tendency.

### Mean

Learned how to calculate the average of a dataset.

Formula:

```text
Mean = Sum of all values / Number of values
```

Example:

```python
data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))
```

### Median

Practiced finding the middle value after sorting the dataset.

```python
data = np.array([10, 20, 30, 40, 50])

print(np.median(data))
```

Also practiced median with an even number of values.

### Mode

Practiced understanding the most frequently occurring value.

Example:

```text
2, 3, 3, 4, 5, 3, 6, 7
```

Mode:

```text
3
```

Also learned that a dataset can have more than one mode.

### Outliers

Practiced understanding how an extreme value can affect statistical measures.

For example:

```text
5, 10, 15, 20, 100
```

The value `100` has a significant effect on the mean.

## 🔵 Level 4 — Measures of Dispersion

Practiced understanding **spread/variability** in data.

The main idea of dispersion is:

> It tells us how far the values in a dataset are spread from each other or from the central value.

### Range

Formula:

```text
Range = Maximum Value - Minimum Value
```

Example:

```python
data = np.array([4, 8, 10, 15, 20])

print(np.max(data) - np.min(data))
```

### Variance

Variance measures how much the values differ from the mean.

Formula for population variance:

```text
Variance = Σ(x - μ)² / N
```

Example:

```python
data = np.array([1, 2, 3, 4, 5])

print(np.var(data))
```

I also practiced calculating variance manually using loops.

### Standard Deviation

Standard deviation is the square root of variance.

```python
data = np.array([1, 2, 3, 4, 5])

print(np.std(data))
```

It is useful because it expresses the spread in the **same units as the original data**.

### Comparing Spread

Compared datasets such as:

```text
A = [10, 10, 10, 10, 10]

B = [5, 8, 10, 12, 15]
```

Dataset A has no variation, while Dataset B has values spread around the mean.

## 🟣 Level 5 — Coefficient of Variation

Practiced the **Coefficient of Variation (CV)**.

Formula:

```text
CV = (Standard Deviation / Mean) × 100
```

CV measures **relative variability**.

Example:

```python
mean = 100
sd = 10

cv = (sd / mean) * 100

print(cv)
```

Also compared datasets having different means but the same standard deviation.

## 🔴 Level 6 — NumPy + Statistics

Combined NumPy operations with statistical concepts.

Practiced calculating:

* Mean
* Median
* Variance
* Standard deviation
* Minimum
* Maximum
* Range

Example:

```python
data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))
print(np.median(data))
print(np.var(data))
print(np.std(data))
print(np.min(data))
print(np.max(data))
print(np.max(data) - np.min(data))
```

Also practiced generating random numbers using:

```python
np.random.random()
```

and analyzing their:

* Mean
* Variance
* Standard deviation

## 🔥 Level 7 — ML-Oriented Statistics

Applied statistical concepts to situations related to **Machine Learning**.

### Consistency

Compared:

```text
Student A = [90, 90, 90]

Student B = [50, 90, 130]
```

Both have the same average, but their standard deviations are different.

This demonstrates that:

> Mean alone does not tell us how consistent the data is.

### Outliers

Practiced understanding the effect of adding an extreme value to a dataset.

Example:

```text
20, 21, 22, 23, 24
```

Then adding:

```text
100
```

Observed how the mean and standard deviation change.

### Feature Scaling

Studied why ML features may require scaling.

Example:

```text
Age:
20, 21, 22, 23, 24

Salary:
20000, 40000, 60000, 80000, 100000
```

The numerical scales of the features are very different.

This introduced the importance of **feature scaling** for some machine learning algorithms.

### Numerical Scale vs Importance

Compared:

```text
Feature A:
1, 2, 3, 4, 5

Feature B:
1000, 2000, 3000, 4000, 5000
```

Learned that a larger numerical scale does **not automatically mean that a feature is more important**.

## 💀 Level 8 — Challenge Problems

Practiced implementing statistical operations manually without relying completely on NumPy statistical functions.

Challenges included:

* Calculate mean using a loop
* Find maximum without `np.max()`
* Find minimum without `np.min()`
* Calculate variance manually
* Calculate standard deviation manually
* Calculate mean, median, range, variance, and standard deviation without statistical functions

### Final Challenge

Worked with the dataset:

```python
data = np.array([12, 15, 18, 21, 25, 30, 100])
```

The objective is to analyze the dataset and understand the effect of the outlier `100`.

## 🧠 Key Concepts Learned

Through these exercises, I practiced:

* NumPy arrays
* Array dimensions
* Array shape and size
* Indexing and slicing
* Reshaping
* Element-wise operations
* Boolean indexing
* Mean
* Median
* Mode
* Range
* Variance
* Standard deviation
* Coefficient of variation
* Outliers
* Data spread
* Data consistency
* Feature scaling
* Relative variability
* Basic ML-oriented statistics

## 🛠️ Technologies Used

* Python
* NumPy

## 🎯 Goal

The goal of this practice is to build a strong foundation in **Python, NumPy, and Statistics** before moving deeper into **Machine Learning and Artificial Intelligence**.

I am focusing on understanding the concepts through both:

1. **NumPy implementation**
2. **Manual implementation using Python loops**

This helps me understand what is happening internally instead of only using built-in functions.
