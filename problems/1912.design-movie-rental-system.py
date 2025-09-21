#
# @lc app=leetcode id=1912 lang=python3
# @lcpr version=30204
#
# [1912] Design Movie Rental System
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList, SortedSet
from collections import defaultdict
from typing import List


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # self.entries = entries
        # self.hasRent = [False] * len(entries)

        # self.shop_movie_to_index = {}
        # self.movie_to_index_list = defaultdict(list)
        # self.movie_to_sorted_index = SortedList(key=lambda x: (x[2], x[0], x[1]))
        self.movie_index_by_price_shop = defaultdict(SortedSet)
        self.rented_index = SortedSet()
        self.movie_shop_to_pricing: dict[tuple[int, int], int] = {}
        for (shop, movie, price) in entries:
            self.movie_index_by_price_shop[movie].add((price, shop))
            self.movie_shop_to_pricing[(movie, shop)] = price
            # self.shop_movie_to_index[(shop, movie)] = i
            # self.movie_to_index_list[movie].append((i,entry))
            # self.movie_to_sorted_index.add((i,entry))

    def search(self, _movie: int) -> List[int]:
        # res = []
        # for entry in self.movie_to_sorted_index:
        #     (shop, movie, price) = entry
        #     if not self.hasRent[i]:
        #         res.append(entry)
        # res.sort(key=lambda x: (x[2], x[0]))
        # res = res[:5]
        # return [x[0] for x in res]
        return [shop for (price, shop) in self.movie_index_by_price_shop[_movie][:5]]

    def rent(self, _shop: int, _movie: int) -> None:
        # for i, entry in enumerate(self.entries):
        #     (shop, movie, price) = entry
        #     if shop == _shop and movie == _movie:
        #         self.hasRent[i] = True
        #         break
        # i = self.shop_movie_to_index[(_shop, _movie)]
        # self.hasRent[i] = True
        price = self.movie_shop_to_pricing[(_movie, _shop)]
        self.rented_index.add((price, _shop, _movie))
        self.movie_index_by_price_shop[_movie].remove((price, _shop))

    def drop(self, _shop: int, _movie: int) -> None:
        # for i, entry in enumerate(self.entries):
        #     (shop, movie, price) = entry
        #     if shop == _shop and movie == _movie:
        #         self.hasRent[i] = False
        #         break
        # i = self.shop_movie_to_index[(_shop, _movie)]
        # self.hasRent[i] = False
        price = self.movie_shop_to_pricing[(_movie, _shop)]
        self.rented_index.remove((price, _shop, _movie))
        self.movie_index_by_price_shop[_movie].add((price, _shop))

    def report(self) -> List[List[int]]:
        # res = [
        #     (price, shop, movie)
        #     for (price, shop, movie) in self.rented_index
        # ]
        # for i, entry in enumerate(self.entries):
        #     if self.hasRent[i]:
        #         res.append(entry)
        # res.sort(key=lambda x: (x[2], x[0], x[1]))
        # res = res[:5]
        # print(f"report: {res}")
        # return [[shop, movie] for (shop, movie, price) in res]
        return [[shop, movie] for (price, shop, movie) in self.rented_index[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
# @lc code=end


sys = MovieRentingSystem(
    3, [
        [0, 1, 3], 
        [0, 5, 3], 
        [0, 7, 3], 
        [0, 6, 3], 
        [0, 2, 3], 
        [0, 3, 3],
        [0, 4, 3],
        [0, 8, 3]
    ]
)

print(sys.rent(0, 1))
print(sys.report())
print(sys.rent(0, 4))
print(sys.report())
print(sys.rent(0, 3))
print(sys.report())
print(sys.rent(0, 2))
print(sys.rent(0, 6))
print(sys.rent(0, 7))
print(sys.report())

