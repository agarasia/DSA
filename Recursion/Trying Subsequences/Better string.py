def countSub(s):
    last = {} #dictionary to store the last occurrence of each character
    n = len(s)
    dp = [0] * (1 + n) #dp array to store the count of distinct substrings ending at index i
    dp[0] = 1 #initializing the first element of dp as 1
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1] #doubling the count from the previous index
        if s[i - 1] in last: #if the current character has occurred before
            dp[i] = dp[i] - dp[last[s[i - 1]]] #subtract the count of distinct substrings that end at the previous occurrence of this character
        last[s[i - 1]] = i - 1 #update the last occurrence of this character
    return dp[n] #returning the count of distinct substrings in the given string

#Function to compare two strings and return the better one.
def betterString(str1, str2):
    a = countSub(str1) #counting the number of distinct substrings in str1
    b = countSub(str2) #counting the number of distinct substrings in str2
    if a < b: #if str2 has more distinct substrings
        return str2 #return str2 as the better string
    return str1 #else return str1 as the better string



s1, s2 = "gfg", "ggg"

print(betterString(s1, s2))