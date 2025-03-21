class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indeg = dict()
        ans = []
        unlock = defaultdict(list)
        suppliez = set(supplies)
        for i in range(len(ingredients)):
            c=0
            for pre in ingredients[i]:
                if pre not in suppliez:
                    unlock[pre].append(recipes[i])
                    c+=1

            if not c:
                ans.append(recipes[i])
            else:
                indeg[recipes[i]] = c
        i = 0
        while i < len(ans):
            new = ans[i]
            for next_recipe in unlock[new]:
                indeg[next_recipe] -= 1
                if not indeg[next_recipe]:
                    ans.append(next_recipe)
            i+=1
        return ans
"""You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients."""
