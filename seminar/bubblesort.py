# Bubble sort in Python

def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)): #(0,5)

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):#fst (0,4), snd (0,3), third (0,2), fourth (0,1]

            # compare two adjacent elements
            if array[j] > array[j + 1]:         #Fst pass [0]>[0+1],1>2,2>3,3>4, snd pass 0>1,1>2,2>3,third 0>1,1>2
                # swapping elements if elements
                # are not in the intended order     #[-2,0,11,-9,45]
                temp = array[j]                     #[-2,0,-9,11,45]
                array[j] = array[j + 1]             #[-2,-9,0,11,45]
                array[j + 1] = temp                 #[-9,-2,0,11.45]


data = [-2, 45, 0, 11, -9]
bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)