class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letter_count = [0] * 26
        for letter in tasks:
            letter_count[ord(letter) - ord("A")] += 1
        processed = 0
        time = 0
        total = len(tasks)
        while processed < total:
            letter_count.sort(reverse=True)
            for i in range(n+1):
                time += 1
                if i>25:
                    continue
                if letter_count[i]:
                    processed+=1
                    letter_count[i] -= 1
                    if processed == total:
                        break
        return time
