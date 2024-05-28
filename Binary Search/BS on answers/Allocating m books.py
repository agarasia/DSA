def allocateBooksBruteForce(books, children):
    # Helper Function: How many children can the pages
    #                  be alloted?
    def studentsAllocated(pages):
        n = len(books)
        numStudents = 1
        pagesAlloted = 0

        for i in range(n):
            if pagesAlloted + books[i] <= pages:
                pagesAlloted += books[i]
            else:
                numStudents += 1
                pagesAlloted = books[i]
        
        return numStudents
    
    # Driver Code

    # Edge Case: when there aren't enough books
    if len(books) < children:
        return -1
    
    maxPages, totalPages = -float('inf'), 0
    for pages in books:
        maxPages = max(maxPages, pages)
        totalPages += pages
    
    for pages in range(maxPages, totalPages+1):
        if studentsAllocated(pages) == children:
            return pages
    
    return maxPages
# T(n)= O( n * (sum(a[]) - max(a[]) ) )

def allocateBooksOptimal(books, children):
    # Helper Function: How many children can the pages
    #                  be alloted?
    def studentsAllocated(pages):
        n = len(books)
        numStudents = 1
        pagesAlloted = 0

        for i in range(n):
            if pagesAlloted + books[i] <= pages:
                pagesAlloted += books[i]
            else:
                numStudents += 1
                pagesAlloted = books[i]
        
        return numStudents
    
    # Driver Code

    # Edge Case: when there aren't enough books
    if len(books) < children:
        return -1
    
    maxPages, totalPages = -float('inf'), 0
    for pages in books:
        maxPages = max(maxPages, pages)
        totalPages += pages
    
    low, high = maxPages, totalPages

    while low <= high:
        mid = low + (high-low)//2
        students = studentsAllocated(mid)
        if students > children:
            low = mid + 1
        else:
            high = mid - 1
    
    return low
# T(n)= O( n * log(sum(a[]) - max(a[]) ) )

books = [25, 46, 28, 49, 24]
children = 4

print(allocateBooksBruteForce(books, children))
print(allocateBooksOptimal(books, children))