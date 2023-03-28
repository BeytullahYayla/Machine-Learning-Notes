
import random
def quick_sort(array,low_index:int,high_index:int):
    if low_index>=high_index:
        return 
    pivot=array[high_index]#We Selected High index value as a pivot value
    left_pointer=low_index
    right_pointer=high_index
    
    
    while left_pointer<right_pointer:
        while array[left_pointer]<=pivot and left_pointer<right_pointer:
            left_pointer+=1
            
        while array[right_pointer]>=pivot and left_pointer<right_pointer:
            right_pointer-=1
            
        swap(array, left_pointer, right_pointer)
        
        
        
    swap(array,left_pointer,high_index)
    quick_sort(array, low_index, left_pointer-1)
    quick_sort(array, left_pointer+1, high_index)

    
def swap(array,index1:int,index2:int):
    temp=array[index1]
    array[index1]=array[index2]
    array[index2]=temp
    

array=[30,40,100,50,80]
quick_sort(array, low_index=0, high_index=len(array)-1)

    
    
    

