# 🟢 Level 1 — Beginner
# Python / NumPy Basics
import numpy as np
# Create a NumPy array containing:

# 10, 20, 30, 40, 50
FirstArry = np.array([10,20,30,40,50])
print(FirstArry)

# Find its:
# shape
print(FirstArry.shape)
# size
print(FirstArry.size) #It shows the element
# number of dimensions
print(FirstArry.ndim)

# data type

# Create an array containing numbers from 1 to 20 using arange().
num = np.arange(1,21)
print(num)

# Create an array of 10 zeros.
zero = np.zeros(9 , dtype=np.int16).reshape(3,3)
print(zero)

# Create an array of 5 ones.
one = np.ones(5 ,dtype=np.int16)
print(one)

# Create an array:

# [1, 2, 3, 4, 5, 6]
arr = np.arange(1,7)
print(arr)
# Reshape it into:

# 2 × 3
arr = arr.reshape(2,3)
print(arr)

# Create numbers from 1 to 12 and reshape them into:

# 3 × 4
num2 = np.arange(1,13).reshape(3,4)
print(num2)
# Given:

# a = np.array([10, 20, 30, 40, 50])

a = np.array([10, 20, 30, 40, 50])

# Find:

# first element
print(a[0])
# last element
print(a[-1])

# first three elements
print(a[:3])
# elements from index 2 to 4
print(a[2:])
# Given:

# a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5])
# Multiply every element by 10.
b = b*10
print(b)

# Add these two arrays:

# a = np.array([1, 2, 3])
c = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
d = np.array([4, 5, 6])
e = c+d
print(e)

# Find the:
# minimum
print(np.min(b))
# maximum
print(np.max(b))
# sum
print(np.sum(b))
# mean
# of:
# [12, 15, 18, 20, 25]
mean = np.array([12, 15, 18, 20, 25])
print(np.mean(mean))
# 🟡 Level 2 — Concept Building
# Understand what's actually happening
# What is the difference between:
# np.array([1, 2, 3])

# and

# np.array([[1, 2, 3]])

# What are their shapes?

# What will happen here?
# a = np.arange(1, 10)
# a.reshape(2, 5)

# Explain why.

# Can this array:
# np.arange(1, 13)

# be reshaped into:

# 2 × 6
# 3 × 4
# 4 × 3
# 6 × 2

# Explain the rule.

# Predict the output:
# a = np.array([1, 2, 3, 4, 5])

# print(a * 2)
# print(a + 10)
# Predict:
# a = np.array([10, 20, 30, 40, 50])

# print(a[a > 25])
# Given:
# marks = np.array([45, 67, 32, 89, 76, 55])
marks = np.array([45, 67, 32, 89, 76, 55])
# Find all students' marks that are:

# > 60 
for i in  marks :
    if i > 60 :
        print("The Marks Above 60 is :", i)
    
# Find all values between 40 and 70.
for i in  marks :
    if i > 40 and i < 70 :
        print("The Marks Above 40 and less than 70 is :", i)
# Given:
# a = np.array([1, 2, 3, 4, 5])

# Find the mean manually first, then verify it using NumPy.
a = np.array([1, 2, 3, 4, 5])
sum = 0 
count = 0
for i in a :
    sum = sum + i 
    count = count +1
print(count)
manualMean = sum // count
print(manualMean)
print(np.mean(a))

# Given:
# [2, 4, 6, 8, 10]

# Calculate the variance manually.
variance = np.arange(2,11,2)
print(variance)
sum = 0 
count = 0
for i in variance :
    sum = sum + i 
    count = count +1
print(count)
manualMean = sum / count

sq = 0
for i in variance :
    sq = sq + (i - manualMean)**2
manualVariance = sq / count
print(manualVariance)

print(np.var(variance))

# Why is variance measured in squared units?
# 🟠 Level 3 — Statistics Problems

# These are important for ML.

# Mean
# Calculate the mean:

# 10, 20, 30, 40, 50
mean = np.arange(10,51,10)
print(mean)
print(np.mean(mean))
# Dataset:
# 5, 10, 15, 20, 100
Dataset = np.array([5, 10, 15, 20, 100])
# Calculate the mean.
print(np.mean(Dataset))
# Then answer:

# Does 100 have a large effect on the mean? Why?

# Median
# Find the median:
# 10, 20, 30, 40, 50
print(np.median(mean))
# Find the median:
# 10, 20, 30, 40
num1 = np.array([10, 20, 30, 40])
print(np.median(num1))
# Which is more affected by an outlier?
# Mean
# Median
# answer : mean
# Explain why.
# because the value or element have same differances it ok to use mean but the gap is more as comparier to other value it create an outliner 
# Mode
# Find the mode:
# 2, 3, 3, 4, 5, 3, 6, 7
Mode = np.array([2, 3, 3, 4, 5, 3, 6, 7])
# Can a dataset have more than one mode?
# Yes it is 3

# Create an example.

# 🔵 Level 4 — Dispersion

# This is especially important because you were previously confused about measure of dispersion.

# Consider:
# A = [10, 10, 10, 10, 10]

# B = [2, 6, 10, 14, 18]

# Both have the same mean.

# Which dataset has more spread?

# Don't just answer. Explain what "spread" means here.

# Calculate the range:
# 4, 8, 10, 15, 20
range = np.array([4, 8, 10, 15, 20])
print("range :" , range[-1]-range[0])

# Calculate the variance for:
# 1, 2, 3, 4, 5
cal = np.array([1, 2, 3, 4, 5])
print(np.var(cal))
# Calculate the standard deviation for:
# 1, 2, 3, 4, 5
print(np.std(cal))
# Explain why we take the square root of variance to obtain standard deviation.

# Ans : to obtain original spread of value from center mean

# Dataset A:
# 10, 10, 10, 10, 10

# Dataset B:

# 5, 8, 10, 12, 15

# Calculate their standard deviations.
DatasetA = np.array([10, 10, 10, 10, 10])
Datasetb = np.array([5, 8, 10, 12, 15])
print(np.std(DatasetA))
print(np.std(Datasetb))
# What does the difference tell you?
# because it DatasetA their is a constant value so it not spread but be Datasetb is spread with different value 

# 🟣 Level 5 — Coefficient of Variation
# Dataset A:
# Mean = 100
# Standard deviation = 10
Mean = 100
Standarddeviation = 10
# Calculate CV.
print((Standarddeviation/Mean)*100)
# Dataset B:
# Mean = 50
Standarddeviation = 10
Mean = 50
# Standard deviation = 10

# Calculate CV.
print((Standarddeviation/Mean)*100)

# Both have the same standard deviation.

# Why are their CVs different?

# A machine produces:
# Mean = 500
# SD = 25
Mean = 500
SD = 25
print((SD/Mean)*100)
# Another machine:

# Mean = 100
# SD = 10
Mean = 100
SD = 10
print((SD/Mean)*100)
# Calculate CV for both.

# Explain what CV tells you about relative variability.

# 🔴 Level 6 — NumPy + Statistics
# Given:
# data = np.array([10, 20, 30, 40, 50])
data = np.array([10, 20, 30, 40, 50])
# Write NumPy code to calculate:

# mean
print(np.mean(data))
# median
print(np.median(data))
# variance
print(np.var(data))
# standard deviation
print(np.std(data))
# minimum
print(np.min(data))
# maximum
print(np.max(data))
# range
print(data[-1] - data[0])
# Given:
# data = np.array([10, 20, 20, 30, 40, 100])
data = np.array([10, 20, 20, 30, 40, 100])
# Use NumPy to find the mean and median.
print(np.median(data))

# Which one changes more because of 100?

# Given:
# marks = np.array([45, 67, 89, 32, 76, 91, 55, 40])
marks = np.array([45, 67, 89, 32, 76, 91, 55, 40])
# Find:

# Mean
print(np.mean(data))
# Median
print(np.median(data))
# Minimum
print(np.min(data))
# Maximum
print(np.max(data))
# Range
print(np.max(data))
# Variance
print(np.var(data))
# Standard deviation
print(np.std(data))
# Create a NumPy array containing 100 random numbers.
numpyarr = np.array([np.random.random(100)*100] , dtype=np.int32)
print(numpyarr)
print(np.size(numpyarr))
# Calculate its:

# mean
print(np.mean(numpyarr))
# variance
print(np.var(numpyarr))
# standard deviation
print(np.std(numpyarr))
# Then change the random numbers so that the spread becomes larger.

# Observe what happens to standard deviation.

# 🔥 Level 7 — ML-Oriented Problems

# These are the problems I recommend you really understand if your goal is ML/AI.

# Dataset:
# Student A: [90, 90, 90]
# Student B: [50, 90, 130]
StudentA = np.array( [90, 90, 90])
StudentB =  np.array([50, 90, 130])

# Both students have the same average.

# Are their performances equally consistent?

# Use standard deviation to investigate.
print(np.std(StudentA))
print(np.std(StudentB))
# Dataset:
# Age = [20, 21, 22, 23, 24]
Age = [20, 21, 22, 23, 24]
# Calculate mean and standard deviation.
print(np.std(Age))
print(np.mean(Age))
# Then add:

# 100
Age = Age + 100
# Calculate them again.
print(np.std(Age))
print(np.mean(Age))
# Explain what changed.

# Suppose two ML features are:
# Age:
# 20, 21, 22, 23, 24

# Salary:
# 20000, 40000, 60000, 80000, 100000

# Why might these features need scaling before some ML algorithms?

# You have:
# Feature A:
# 1, 2, 3, 4, 5

# Feature B:
# 1000, 2000, 3000, 4000, 5000

# Which feature has larger numerical values?

# Does larger numerical scale automatically mean greater importance?

# Explain.

# A dataset has:
# 1, 2, 3, 4, 1000

# You are training an ML model.

# Answer:

# What is the outlier?
# What happens to the mean?
# What happens to the median?
# What happens to variance?
# Why can outliers become a problem?
# 💀 Level 8 — Challenge Problems
# Without using NumPy's mean():
# data = np.array([10, 20, 30, 40, 50])

# calculate the mean using a loop.

# Without using np.max() or np.min(), find the maximum and minimum.
# Without using np.std(), calculate standard deviation manually.
# Write a program that takes:
# [10, 20, 30, 40, 50]

# and returns:

# Mean
# Median
# Range
# Variance
# Standard deviation

# without using statistical functions.

# Final challenge:

# Given:

# data = np.array([12, 15, 18, 21, 25, 30, 100])