class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        tot=sum([x[0]/x[1] for x in classes])
        blob = [[(x[0]-x[1])/(x[1])/(x[1]+1),x[1]] for x in classes]
        heapify(blob)
        while extraStudents:
            extraStudents-=1
            a=heappop(blob)
            if not a[0]:
                break
            tot-=a[0]
            heappush(blob,[a[0]*a[1]/(a[1]+2),a[1]+1])
        return tot/len(classes)
"""Description:
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted."""
