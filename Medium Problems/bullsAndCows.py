class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        letters=Counter(secret)
        guesses=Counter(guess)
        bulls, cows = 0, 0;
        for a, b in zip(secret,guess):
            if a==b and letters[a]>=0:
                letters[a]-=1
                guesses[b]-=1
                bulls+=1
        for gess, num in guesses.items():
            cows+=min(num,letters[gess])
        return f"{bulls}A{cows}B"
"""You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 """
