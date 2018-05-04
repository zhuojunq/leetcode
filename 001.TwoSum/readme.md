# 描述
Given an array of integers, return indices of the two numbers such that they add up to a specific target.<br>
You may assume that each input would have exactly one solution, and you may not use the same element twice.<br>
Given nums = [2, 7, 11, 15], target = 9,<br>
Because nums[0] + nums[1] = 2 + 7 = 9,<br>
return [0, 1].<br>
<br>
# 思路
应该要遍历这个array，找到两两相加等于target的两个元素，再取他们的index返回。
