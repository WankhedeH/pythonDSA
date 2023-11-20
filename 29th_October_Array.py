#!/usr/bin/env python
# coding: utf-8

# In[9]:


arr = [1, 2, 4, 2, 5, 9]
# A function that returns true if the array has any duplicates, false otherwise
def check_duplicate(arr):
  # Create an empty dictionary
  dict = {}
  # Iterate over the array
  for i in arr:
    # Check if the element is already a key in the dictionary
    if i in dict:
      # Return true if a duplicate is found
      return True
    # Otherwise, add the element as a key without value
    else:
      dict[i] = None
  # Return false if no duplicates are found
  return False


# In[11]:


check_duplicate(arr)


# In[23]:


arr1 = [1, 2, 3, 4, 5, 6, 7]
k = 3

def rotate_element(arr1 , k):
    
    size = len(arr1)
    # Use slicing to create a new list with the rotated elements
    # Use the modulo operator to handle the case when k is larger than size
    return arr1[(size - k) % size:] + arr1[:(size - k) % size]


# In[24]:


rotate_element = rotate_element(arr1, k)
print(rotate_element)


# In[5]:



#Time Complexcity O(n)
#Space Complexcity O(1)

def reverse_array(aar2):
    
    n = len(arr2)
    # loop from 0 to n/2
    for i in range(n//2):
        # swap the i-th element from the left with the i-th element from the right
        arr2[i], arr2[n-i-1] = arr2[n-i-1] , arr2[i]
    return arr2    
        
    
#Driver code
arr2 = [2, 4, 5, 7, 9, 12]

reverse_array(arr2)
print(arr2)


# In[8]:


def maximum_element(arr4):
    
    # base case condition if the array has only one element, return that element
    if len(arr4) == 1:
        return arr4[0]
    # recursive condition compare the first element with the maximum element of the rest of the array
    else:
        return max(arr4[0], maximum_element(arr4[1:]))


#Driver code
arr4 = [10, 5, 20, 8, 15]
max_ele = maximum_element(arr4)
print(max_ele)


# In[1]:



def remove_duplicate(arr5):
    
    if len(arr5) <= 1:
        return arr5
    
    # compare the first element with the second element
    if arr5[0] == arr5[1]:
    # remove the first element and recursively call the function on the remaining array
        return remove_duplicate(arr5[1:])
    else:
    # append the first element to the result of the recursive call on the rest of the array
        return [arr5[0]] + remove_duplicate(arr5[1:])


#Driver code
arr5 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]
print(remove_duplicate(arr5))


# In[ ]:




