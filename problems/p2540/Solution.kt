/*
 * @lc app=leetcode id=2540 lang=kotlin
 *
 * [2540] Minimum Common Value
 *
 * https://leetcode.com/problems/minimum-common-value/description/
 *
 * algorithms
 * Easy (58.02%)
 * Likes:    1254
 * Dislikes: 43
 * Total Accepted:    320.4K
 * Total Submissions: 550.1K
 * Testcase Example:  '[1,2,3]\n[2,4]'
 *
 * Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
 * return the minimum integer common to both arrays. If there is no common
 * integer amongst nums1 and nums2, return -1.
 * 
 * Note that an integer is said to be common to nums1 and nums2 if both arrays
 * have at least one occurrence of that integer.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [1,2,3], nums2 = [2,4]
 * Output: 2
 * Explanation: The smallest element common to both arrays is 2, so we return
 * 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
 * Output: 2
 * Explanation: There are two common elements in the array 2 and 3 out of which
 * 2 is the smallest, so 2 is returned.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums1.length, nums2.length <= 10^5
 * 1 <= nums1[i], nums2[j] <= 10^9
 * Both nums1 and nums2 are sorted in non-decreasing order.
 * 
 * 
 */
package p2540
// @lc code=start
class Solution {
    fun getCommon1(nums1: IntArray, nums2: IntArray): Int {
        val iter1 = nums1.iterator()
        val iter2 = nums2.iterator()
        var num1 = iter1.next()
        var num2 = iter2.next()
        while(num1 != num2) {
            if(num1<num2) {
                if(iter1.hasNext().not()) return -1
                num1 = iter1.next()
            } else {
                if(iter2.hasNext().not()) return -1
                num2 = iter2.next()
            }
        }
        return num1
    }
    fun getCommon(nums1: IntArray, nums2: IntArray): Int {
        return nums1.toSet().intersect(nums2.toSet()).minOrNull() ?: -1
    }
}
// @lc code=end

