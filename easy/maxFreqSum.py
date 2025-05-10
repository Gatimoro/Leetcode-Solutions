class Solution:
    def maxFreqSum(self, s: str) -> int:
        cou = Counter(s)
        v, con, vf, cf = '', '', 0, 0
        for c, freq in cou.items():
            if c in 'aeiou':
                if freq > vf:
                    vf = freq
            else:
                if freq > cf:
                    cf = freq

        return cf + vf
                ©leetcode
  #return frequencies of the mosts frequent vowel and consonant.
