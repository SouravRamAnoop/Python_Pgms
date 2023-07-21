# Selection sort in Python


def selectionSort(array, size):
    for step in range(size): #(0,5)
        min_idx = step  #0,1,2,3,4

        for i in range(step + 1, size): #(1,5),(2,5),(3,5)

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]: #fst 1<0,2<0,3<0,4<0, 2nd 2<1
                min_idx = i  #4

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])  # 0,4=4,0 |1,2=2,1|3,2=2,3


data = [-2, 45, 0, 11, -9]              #[-9,45,0,11,-2]
size = len(data)                        #
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)