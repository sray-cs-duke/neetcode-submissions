class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        longest = 0
        highest_frequency = 0
        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1

            highest_frequency = max(
                highest_frequency,
                count[char]
            )
            while (
                right - left + 1 - highest_frequency > k
            ):
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest