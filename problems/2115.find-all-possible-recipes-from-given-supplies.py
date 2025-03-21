#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#

# @lc code=start
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipesSet: set[str] = set(recipes)
        suppliesSet: set[str] = set(supplies)
        ingredientsMap: dict[str, set[str]] = {}
        for recipe, ingredients in zip(recipes, ingredients):
            ingredientsMap[recipe] = set(ingredients)
        
        cache: dict[str, bool] = {}
        def dfs(key: str, path: set[str]) -> bool:
            if key in cache:
                return cache[key]
            if key in path:
                return False
            if key in supplies:
                cache[key] = True
                return True
            if key in recipesSet:
                result = all(
                    dfs(k, path | {key})
                    for k in ingredientsMap[key]
                )
                cache[key] = result
                return result
            return False
        
        return [key for key in recipes if dfs(key, set())]

   
# @lc code=end

print(Solution().findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
print(Solution().findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))
print(Solution().findAllRecipes(recipes = ["burger","bread","sandwich"], ingredients = [["sandwich","meat","bread"],["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))