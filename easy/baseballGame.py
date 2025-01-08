class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=deque()
        for operation in operations:
            match operation:
                case "C":
                    record.pop()
                case "+":
                    record.append(record[-1]+record[-2])
                case "D":
                    record.append(record[-1]<<1)
                case _:
                    record.append(int(operation))
        return sum(record)
