#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def max_sub_array(array, start, end):
    if start == end-1:
       return start,end, array[start]
    else:
       mid = (start + end)//2
       left_start, left_end, left_max = max_sub_array(array, start, mid)
       right_start, right_end, right_max = max_sub_array(array, mid, end)
       cross_start, cross_end, cross_max = max_cross_sub_array(array, start, mid, end)
       if (left_max > right_max and left_max > cross_max):
           return left_start, left_end, left_max
       elif (right_max > left_max and right_max > cross_max):
           return right_start, right_end, right_max
       else:
           return cross_start, cross_end, cross_max
 
def max_cross_sub_array(array, start, mid, end):
    
    left_sum = float('-inf')
    sum = 0
    cross_start = mid
    for i in range(mid - 1, start -1, -1):
       sum =sum + array[i]
       if(sum > left_sum):
            left_sum =sum
            cross_start = i
 
    right_sum = float('-inf')
    sum = 0
    cross_end = mid + 1
    for i in range(mid, end):
       sum =sum + array[i]
       if(sum > right_sum):
            right_sum =sum
            cross_end = i + 1
    return cross_start, cross_end, left_sum + right_sum
 
array = input('Enter the list of numbers: ')
array = array.split()
array = [int(x) for x in array]
start, end, maximum = max_sub_array(array, 0,len(array))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum of {}.'.format(start, end-1, maximum))


# In[ ]:




