# Python program to print positive Numbers in a List
  
# list of numbers
list1 = [12 , -7, 5 , 64, -14] 
  
# using list comprehension 
pos_nos = [num for num in list1 if num >= 0] 
  
print("Positive numbers in the list: ", *pos_nos) 


list2 = [12, 14 , -95,3] 
  
# using list comprehension 
pos_nos = [num for num in list2 if num >= 0] 
  
print("Positive numbers in the list: ", *pos_nos) 