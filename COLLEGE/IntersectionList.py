def intersection(list1,list2):
    return list(set(list1) & set(list2))
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
print("The first list is:",list1)
print("The second list is:",list2)
print(f"The intersection of the two lists is:{intersection(list1,list2)}")