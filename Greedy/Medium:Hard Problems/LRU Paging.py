def numberOfPageFault(pages, c):
    memory = set()
    pagingOrder = []
    pagingFaults = 0

    for page in pages:
        if page in memory:
            pagingOrder.remove(page)
            pagingOrder.append(page)
        else:
            pagingFaults += 1
            if len(pagingOrder) >= c:
                lruPage = pagingOrder.pop(0)
                memory.remove(lruPage)
            memory.add(page)
            pagingOrder.append(page)
    
    return pagingFaults
# T(n) = O(n)
# S(n) = O(n)

pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]
capacity = 4

print(numberOfPageFault(pages, capacity))