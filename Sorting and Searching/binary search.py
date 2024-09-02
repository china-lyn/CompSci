from bubble_sort import userlist, bubblesort

#get list
l = userlist()
tnum = int(input('Enter your target number: '))
#sort list
l = bubblesort(l)
print(l)
# set values
low = 0
high = len(l) - 1
mid = (low + high) // 2
 
while l[mid] != tnum:
    if l[mid] < tnum:
        low = mid + 1
    elif l[mid] > tnum:
        high = mid - 1
    mid = (low + high) // 2
print(f'The index position of your target number is {mid}')