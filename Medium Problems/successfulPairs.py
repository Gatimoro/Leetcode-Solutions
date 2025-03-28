class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sort_spells= [(spell, index) for index,spell in sorted(enumerate(spells), key = lambda x: x[1])]
        cooked = 0
        last = -1
        potions.sort(reverse = True)
        for spell, index in sort_spells:
            if spell == last or cooked == len(potions) or potions[cooked] * spell < success:
                spells[index] = cooked
                continue

            while cooked < len(potions) and potions[cooked] * spell >= success:
                cooked += 1
            last = spell
            spells[index] = cooked

        return spells
"""You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

"""
