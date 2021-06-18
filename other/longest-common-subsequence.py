#Given lowercase alphabet strings a, b, and c, return the length of their longest common subsequence

class Solution:
    def solve(self, a, b, c):
        # dp[i][j][k] represents ith of a, jth of b, kth of c and the maximum length subsequence up to that point
        dp = [[[0 for k in range(len(c))] for j in range(len(b))] for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    if a[i] == b[j] == c[k]:
                        dp[i][j][k] = 1 + self.get(i - 1, j - 1, k - 1, dp)
                    else:
                        dp[i][j][k] = max(self.get(i - 1, j, k, dp), self.get(i, j - 1, k, dp),
                                          self.get(i, j, k - 1, dp))
        return self.get(len(a) - 1, len(b) - 1, len(c) - 1, dp)

    def get(self, i, j, k, dp):
        if i < 0 or j < 0 or k < 0:
            return 0
        else:
            return dp[i][j][k]
