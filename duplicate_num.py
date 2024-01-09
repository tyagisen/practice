non_duplicate = {}
duplicate_num = []
def findDuplicateNum(arr):
    for num in arr:
        if num not in non_duplicate:
            non_duplicate[num] = True
        else:
            duplicate_num.append(num)
    return duplicate_num



arr = [1,1,33,4,56,7,4,4]
print(list(set(findDuplicateNum(arr))))