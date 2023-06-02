#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:31:45 2023

@author: adelita
"""

import matplotlib.pyplot as plt
import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_performance(sort_func, data):
    start_time = time.time()
    sorted_data = sort_func(data)
    end_time = time.time()
    execution_time = end_time - start_time
    return sorted_data, execution_time

def plot_performance(x, y_qs, y_ms):
    plt.plot(x, y_qs, marker="o", color="b", linestyle='-', label="QuickSort")
    plt.plot(x, y_ms, marker="o", color="r", linestyle='-', label="MergeSort")
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Rendimiento de QuickSort y MergeSort")
    plt.legend()
    plt.show()

TAM_MAX = 1000
STEP = 100

sizes = range(STEP, TAM_MAX + 1, STEP)
time_qs = []
time_ms = []

for size in sizes:
    data = random.sample(range(size), size)
    _, exec_time_qs = measure_performance(quicksort, data)
    _, exec_time_ms = measure_performance(mergesort, data)
    time_qs.append(exec_time_qs)
    time_ms.append(exec_time_ms)

plot_performance(sizes, time_qs, time_ms)
