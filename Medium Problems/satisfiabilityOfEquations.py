class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        papa = dict()
        weight = defaultdict(int)

        for eq in equations:
            papa[eq[0]] = eq[0]
            papa[eq[3]] = eq[3]
        
        def dad_of_(var):
            if papa[var] != papa[papa[var]]:
                papa[var] = dad_of_(papa[var])
            return papa[var]


        def same_dad(billy, joe):
            bob, john = dad_of_(billy), dad_of_(joe)
            if bob == john:
                return
            if weight[bob] > weight[john]:
                papa[john] = bob
            elif weight[bob] < weight[john]:
                papa[bob] = john
            else:
                papa[john] = bob
                weight[bob] += 1


        ineq = []
        for eq in equations:
            if eq[1]=='!':
                ineq.append(eq)
            else:
                ahmed, hamood = eq[0], eq[3]
                same_dad(ahmed, hamood)
        for eq in ineq:
            ahmed, hamood = eq[0], eq[3]
            if dad_of_(ahmed) == dad_of_(hamood):
                return False
        
        return True
"""You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise."""
