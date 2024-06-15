# Approach: Recursively check for all possible subsequences 
#           if the temp sum is equal to the target sum.
def powerSetSumBruteForce(nums, target):
    def generate(ans, temp, nums, ind):
        if ind == len(nums):
            ans.append(temp)
            return
        
        generate(ans, temp + nums[ind], nums, ind+1)
        generate(ans, temp, nums, ind + 1)
    
    ans = []
    generate(ans, 0, nums, 0)
    count = 0

    for i in ans:
        if i == target: count += 1
        else:   continue
    
    return count

# Approach: Use dynamic programming
def powerSetSumOptimal(nums, target):
    MOD = 1e9 + 7
    n = len(nums)
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, target + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(target + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
            dp[i][j] %= MOD

    return int(dp[n][target] % MOD)

nums = [5, 2, 3, 10, 6, 8]
target = 10

print(powerSetSumBruteForce(nums, target))
print(powerSetSumOptimal(nums, target))