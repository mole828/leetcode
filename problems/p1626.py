class Solution:
    def bestTeamScore(self, scores, ages):
        n = len(scores)
        players = sorted(zip(ages, scores))
        dp = [score for age, score in players]
        print(players, dp)
        for i in range(n):
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
                    print(dp)
        return max(dp)