# creating an empty list 
list1 = []
list2=[]
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    list1.append(ele) # adding the element 
      
print(list1) 

n1 = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n1): 
    ele = int(input()) 
  
    list2.append(ele) # adding the element 
      
print(list2)

listThree = list()

oddElements = list1[1::2]
print("Element at odd-index positions from list one")
print(oddElements)

EvenElement = list2[0::2]
print("Element at even-index positions from list two")
print(EvenElement)

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)
