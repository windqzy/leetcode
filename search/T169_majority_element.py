"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""
"""
摩尔投票算法思路（对立抵消思想）
核心概念：
多数元素的个数 > 所有其他元素的总和
→ 所以互相抵消之后，多数元素一定会剩下
输入：[2, 2, 1, 1, 1, 2, 2]

步骤	当前值 i	候选人 current	票数 flag	说明
1	2	2	1	初始化
2	2	2	2	支持票
3	1	2	1	反对票
4	1	2	0	反对票
5	1	1	1	替换候选人
6	2	1	0	反对票
7	2	2	1	替换候选人

"""

class Solution:
    def majorityElement(self, nums) -> int:
        candidate = count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    print(solution.majorityElement(nums))  # 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(solution.majorityElement(nums))  # 2
