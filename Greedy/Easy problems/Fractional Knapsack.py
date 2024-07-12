class Item:
    def __init__(self, val, weight) -> None:
        self.val = val
        self.weight = weight

# Approach: Arrange the elements based on profit/weight.
def fractionalKnapsack(w, arr):
    ratio = []
    for i in range(len(arr)):
        ratio.append((arr[i].val/arr[i].weight, i))
    
    ratio.sort(reverse = True)
    value = 0.0
    i = 0

    while w and i < len(arr):
        item = arr[ratio[i][1]]

        if item.weight > w:
            value += (item.val * (w/item.weight))
            w -= w
        
        if item.weight <= w:
            value += item.val
            w -= item.weight

        i += 1

    return value
# T(n) = O(n * logn)
# S(n) = O(n)


i1 = Item(60, 10)
i2 = Item(100, 20)
i3 = Item(120, 30)

w = 50
arr = [i1, i2, i3]

print(fractionalKnapsack(w, arr))