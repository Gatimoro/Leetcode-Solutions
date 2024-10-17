class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        #suma is provisionally our whole sum
        suma=sum(skill)
        #teams is just the length of the list/2, but i shifted right instead of dividing to preserve the int quality
        teams=len(skill)>>1
        #if you get a remainder when calculating the teams skill, return -1
        if suma%teams!=0:
            return -1
        #our players are ranked by skill
        skill=sorted(skill)
        #suma now adopts the value of the skill of each team, which is constant and an integer as we checked earlier.
        suma=suma//teams
        #initialize chem
        chem=0
        #now for each team's first player's skill, we will match them with someone of the 'opposite' skill value
        for n in range(teams):
            #at each step checking that the combined team skill is equal to the other teams.
            if skill[ n ]+skill[ -n -1]!=suma:
                return -1
            #lastly we add the product of both players' skills to our return var
            chem+=skill[ n ]*skill[ -n -1]
        return chem
