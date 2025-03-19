class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times + [float('inf')]
        maxim = 0
        votes = defaultdict(int)
        self.leader = [None] * len(persons)
        for index in range(len(persons)):
            votes[persons[index]] += 1
            if votes[persons[index]] >= maxim:
                maxim = votes[persons[index]]
                self.leader[index] = persons[index]
            else:
                self.leader[index] = self.leader[index - 1]
                

        

    def q(self, t: int) -> int:
        return self.leader[ bisect_right(self.times, t)-1]
  """You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:

TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules."""

        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
