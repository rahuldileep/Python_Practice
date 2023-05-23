#brute force - selection sort

def selection_sort(A):
	for i in range(len(A)):
		min_idx = i
		for j in range(i+1,len(A)):
			if A[j] < A[min_idx]:
				min_idx = j
		A[i], A[min_idx] = A[min_idx], A[i]

A = [4,3,5,1,2]
print(A)
selection_sort(A)
print('selection_sort',A)

#brute force - bubble sort

def bubble_sort(A):
	for i in range(len(A)):
		for j in range(len(A)-1,i,-1):
			if A[j] < A[j-1]:
				A[j],A[j-1] = A[j-1],A[j]

A = [4,3,5,1,2]
print(A)
bubble_sort(A)
print('bubble_sort',A)


#decrease and conquer - insertion sort 

def insertion_sort_iterative(A):
	for i in range(1,len(A)):
		nth = A[i]
		j = i-1
		while j>=0 and A[j]>nth:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = nth
A = [4,3,5,1,2]
print(A)
insertion_sort_iterative(A)
print('insertion_sort_iterative',A)

def insertion_sort_recursive(A,n):
	if n<2:
		return
	insertion_sort_recursive(A,n-1)
	nth = A[n-1]
	j = n-2
	while j>=0 and A[j] > nth:
		A[j+1] = A[j]
		j -= 1
	A[j+1] = nth
	return

A = [4,3,5,1,2]
print(A)
insertion_sort_recursive(A,len(A))
print('insertion_sort_recursive',A)

#divide and conquer - mergesort

def mergesort(A):
	def helper(A,start,end):
		if start >= end:
			return
		mid = start+(end-start)//2
		helper(A,start,mid)
		helper(A,mid+1,end)
		i = start
		j = mid+1
		temp = []
		while i <= mid and j <= end:
			if A[i] < A[j]:
				temp.append(A[i])
				i += 1
			else:
				temp.append(A[j])
				j += 1
		while i<=mid:
			temp.append(A[i])
			i += 1
		while j<=end:
			temp.append(A[j])
			j += 1
		A[start:end+1] = temp[:]
	helper(A,0,len(A)-1)

A = [4,3,5,1,2]
print(A)
mergesort(A)
print('mergesort',A)

def quicksort(A):
	def helper(A, start, end):
		if start >= end:
			return
		import random
		rand_idx = random.randint(start,end)
		A[start], A[rand_idx] = A[rand_idx], A[start]
		pivot = A[start]
		smaller = start
		bigger = start
		for bigger in range(start+1,end+1):
			if A[bigger] < pivot:
				smaller += 1
				A[smaller], A[bigger] = A[bigger], A[smaller]
		A[smaller], A[start] = A[start], A[smaller]
		helper(A,start,smaller-1)
		helper(A, smaller+1,bigger)
	helper(A,0,len(A)-1)

A = [4,3,5,1,2]
print(A)
quicksort(A)
print('quicksort',A)

import heapq

def heapsort(A):
	aux = []
	heapq.heapify(A)
	while A:
		aux.append(heapq.heappop(A))
	A[:] = aux[:]

A = [4,3,5,1,2]
print(A)
heapsort(A)
print('heapsort',A)