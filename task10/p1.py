class Solution:
    "NOT MY SOLUTION + it works, its from leet code"
    #All prints are because i needed to understand what happens
    def trap(self, height: List[int]) -> int:
        h_len = len(height)
        biggest_left: list[int] = [height[0]] * h_len
        biggest_right: list[int] = [height[-1]] * h_len
        # print(biggest_left, biggest_right, "\n")
        # print(height)

        for i in range(1, h_len):
            biggest_left[i] = max(biggest_left[i-1], height[i])
            biggest_right[-i-1] = max(biggest_right[-i], height[-i-1])
            # print(biggest_left, biggest_right)
            
        # print("\n", biggest_left, biggest_right)
        # print(sum(min(biggest_left[i], biggest_right[i]) - height[i] for i in range(h_len)))
        
        for i in range(h_len):
            mini = min(biggest_left[i], biggest_right[i]) - height[i]
            # print(biggest_left[i], biggest_right[i], height[i])


"""WAS MY SOLUTION, ONLY SOLVES the 2 test cases"""
# def trap(self, height: list[int]) -> int:
#     water = 0
#     index = 0
#     for i in range(len(height)-1):
#         if height[i] == 0 and i == 0:
#             index += 1
#             continue
#         if i != index: continue
#         print(height[index])
#         print("height: " , height[i])
#         for j in range(i, len(height)):
#             # print(height[j])
#             if height[j] - height[i] != 0 and height[j] != 0:
#                 if j - i < 2: 
#                     continue
#                 print("J Loop: " , height[j])
#                 for k in range(i, j):
#                     water += height[i] - height[k]
#                     print("K Loop: ", height[k], end = " || ")
#                     print("Water = : ", water)
#                 index = j
#                 break
#             else:
#                 index = i + 1
                
#         print(water)
        
#     return water