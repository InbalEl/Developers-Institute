list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3): # only go as far it is possible
    print(item)

(1, 'a', 1.1)
(2, 'b', 2.2)
(3, 'c', 3.3)

zipped_list = list(zip(list1, list2, list3))
print(zipped_list)

