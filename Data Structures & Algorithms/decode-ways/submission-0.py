class Solution:
    def numDecodings(self, s: str) -> int:
        code_len = len(s)
    
        dp =[0 for _ in range(code_len)]
        for i in range(code_len):
            
            if i == 0 and int(s[i]) != 0:
                dp[i] = 1
                continue
            if int(s[i-1] + s[i]) > 26 or int(s[i]) == 0 or int(s[i-1]) == 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i - 1] + 1
                
        return dp[-1]