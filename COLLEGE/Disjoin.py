#using inbuilt function
def disjoin(set1,set2):
    if set1 & set2:
        return False
    return True
# without inbuilt function
def disjoinCheck(set1,set2):
    for element in set1:
        if element in set2:
            return False
    return True
set1={1,2,3}
set2={6,4,5}
if disjoinCheck(set1,set2):
    print("The sets are disjoined")
else:
    print("The sets are not disjoined")