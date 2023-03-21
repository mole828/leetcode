from typing import List


class Solution:
    def convertTemperature(self, 摄氏度: float) -> List[float]:
        开氏度 = 摄氏度 + 273.15
        华氏度 = 摄氏度 * 1.80 + 32.00
        return [开氏度, 华氏度]