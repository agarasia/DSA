# Approach: Find frequencies of each element and then check for majority
def majorityElementBruteForce(nums):
    Set = set()                 # Keep track of Unique elements
    ans = []                    # List of majority elements

    for i in nums:              # Making a set of unique elements
        Set.add(i)
    
    n = len(nums)
    majority = n//3             # How many times an element needs 
                                # to be there to be majority element

    # Count the frequency of each element in set and if majority element,
    # Append it to the answer and return it
    for i in Set:
        count = 0
        for j in nums:
            if i == j:
                count += 1
            else:   continue
        if count > majority:
            ans.append(i)
    return ans


# Approach: Use a hash map to keep track of the count
def majorityElementBetter(nums):
    hashMap = {}                # Initialize a hash map
    ans = []

    for i in nums:              # Add elements to the map
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1
    
    n = len(nums)
    majority = n // 3

    for i in hashMap:
        if hashMap[i] > majority:   # If element in hashmap occurs more than majority
            ans.append(i)           # Append it to the answer
    
    return ans

# Approach: Extended Moore's voting algorithm
def majorityElementOptimal(v):
    n = len(v) # size of the array

    cnt1, cnt2 = 0, 0 # counts
    el1, el2 = float('-inf'), float('-inf') # element 1 and element 2

    # applying the Extended Boyer Moore’s Voting Algorithm:
    for i in range(n):
        if cnt1 == 0 and el2 != v[i]:
            cnt1 = 1
            el1 = v[i]
        elif cnt2 == 0 and el1 != v[i]:
            cnt2 = 1
            el2 = v[i]
        elif v[i] == el1:
            cnt1 += 1
        elif v[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = [] # list of answers

    # Manually check if the stored elements in
    # el1 and el2 are the majority elements:
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if v[i] == el1:
            cnt1 += 1
        if v[i] == el2:
            cnt2 += 1

    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)

    return ls


nums = [1, 3, 3, 4]
print(majorityElementBruteForce(nums), majorityElementBetter(nums), majorityElementOptimal(nums))