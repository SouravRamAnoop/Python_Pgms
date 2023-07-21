# Insertion sort in Python


def insertionSort(array):
    for i in range(1, len(array)): #(1,5)
        key = array[i] #1,2,3,4
        j = i - 1  #0,1,2,3

        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < array[j]:           # j=0 fst 5<9,snd j=1 1<9 1<5,,thrd 4<9 4<5 4<1, forth 3<9 3<5 3<4 3<1
            array[j + 1] = array[j]                # fst a[0]=5 ,a[1]=9,            [
            j = j - 1
                                                   #[5,9,1,4,3]
                                                   # [1,5,9,4,3]
                                                   #[1,4,5,9,3]
                                                   #[1,3,4,5,9]

        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)