#
# @lc app=leetcode id=2353 lang=python3
#
# [2353] Design a Food Rating System
#

# @lc code=start
from collections import Counter, defaultdict
from typing import List

from sortedcontainers import SortedList


class FoodRatings:
    __food2cuisine: dict[str, str]
    __food2rating: dict[str, int]
    __cuisine2foods: dict[str, SortedList]

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.__food2cuisine = dict()
        self.__food2rating = dict() 
        self.__cuisine2foods = defaultdict(SortedList)
        for cuisine,food,rating in zip(cuisines,foods,ratings):
            self.__food2cuisine[food] = cuisine
            self.__food2rating[food] = rating
            self.__cuisine2foods[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.__food2rating[food]
        self.__food2rating[food] = newRating
        cuisine = self.__food2cuisine[food]
        self.__cuisine2foods[cuisine].remove((-oldRating, food))
        self.__cuisine2foods[cuisine].add((-newRating, food))
        return 

    def highestRated(self, cuisine: str) -> str:
        return self.__cuisine2foods[cuisine][0][1]

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end

