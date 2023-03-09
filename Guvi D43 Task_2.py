# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:09:13 2023

@author: Aditi
"""

#Guvi D43 Task_2
import numpy as np
import numpy.random as npr

#create a vector of 1 to 10 by adding 1 to the result of the arange function.
vector = np.arange(1,11) + 1
print(vector)

#Reshape the vector to a 2D array with shape ((10,1))
reshaped_vector = vector.reshape((10,1))

#Add the vector to its transpose to create a 10x10 matrix A.
A = reshaped_vector + vector
print(A)

#Create a fake dataset with 50 examples, each with 5 dimensions
data = np.exp(npr.randn(50,5))

#Standarize the data to have zero mean and unit variance using broadcasting
data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
print(data)

mean_vec = np.mean(data,axis=0)
std_vec = np.std(data,axis=0)
print("Mean vector:", mean_vec)
print("standard deviation vector:", std_vec)

normalized = (data - np.mean(data,axis=0)) / np.std(data, axis=0)
norm_mean_vec = np.mean(normalized, axis=0)
norm_std_vec = np.std(normalized, axis=0)
print("Mean vector of normalized data:", norm_mean_vec)
print("standard deviaton vector of standarized data:", norm_std_vec)

#PART 2
import scipy.stats as stats
import numpy as np

#create the contigency table
table = np.array([[141,68,4],[179,159,7],[220,216,4],[86,101,4]])

#Calculate the expected values
row_totals = table.sum(axis=1)
col_totals = table.sum(axis=0)
total = table.sum()
expected = np.outer(row_totals, col_totals)/total

#Calculate the chi-squared statistic and p-value
chi_squared_stat = ((table - expected)**2 / expected).sum()
df = (table.shape[0]-1)*(table.shape[1]-1)
p_value = 1 - stats.chi2.cdf(chi_squared_stat, df)

#print the results
print(f"Chi-squared statistic:{chi_squared_stat:.3f}")
print(f"Degrees of freedom: {df}")
print(f"P-value: {p_value:.3f}")

if p_value<0.05:
    print("There is evidence of a relationship between age group and movie genre inclination.")
else:
    print("There is no evidence of a relationship between age group and movie genre inclination.")




