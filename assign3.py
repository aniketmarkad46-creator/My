list = [10,8,3,5,6,7,2,4,9,1]
print("list: ",list)

def bubble_sort(list):
    n = len(list)
    for i in range (n):
        for j in range (0,n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list
print("bubble sorted list: ",bubble_sort(list))

            
salary = [1500,2000,3500,1800,1200,2200,2500,3000,2800,3200]
#salary = [10,8,3,5,6,7,2,4,9,1]
print("salary: ",salary)
def selection_sort(salary):
    n = len(salary)
    for i in range (n):
        min_index = i
        for j in range(i+1,n):
            if salary[j] < salary[min_index]:
                min_index = j
        salary[i],salary[min_index] = salary[min_index],salary[i]
    return salary
selection_sorted = salary.copy()
selection_sort(selection_sorted)
print("selection sorted list: ", selection_sorted)

print("top 5 salaries (selection sort): ",selection_sorted[5:][::-1])
