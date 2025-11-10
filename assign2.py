customer_ids = [1034, 2025, 1022, 1505, 3002, 2501, 1890, 1200]

def linear_search(ids, target):
	for i in range (len(ids)):
		if ids[i] == target:
			return i
	 
	return -1


def binary_search(ids, target):
	left = 0 
	right = len(ids)-1
	
	while left <= right:
		mid = (left + right)//2
		if ids[mid] == target:
			return mid
		elif ids[mid] < target:
			left = mid + 1
			return left
		else:
			right = mid - 1
			return right 
			
	return -1

print("customer ids search system ")
print("list of customer ides: ",customer_ids)
try:
	target = int(input("enter the target: "))
except ValueError:
	print("iNVALID INPUT!, please enter a numeric ID.")
	exit()
	
index_linear = linear_search(customer_ids, target)
if index_linear != -1:
	print("linear search: customer ID ",target," found at indexn ",index_linear)
else:
	print("linear search: customer ID ",target," not found.")

sorted_ids = sorted(customer_ids)
print("Sorted customer IDs for binary search: ",sorted_ids)

index_binary = binary_search(customer_ids, target)
if index_binary != -1:
	print("binary search: customer ID ",target," found at indexn ",index_binary)
else:
	print("binary search: customer ID ",target," not found.")