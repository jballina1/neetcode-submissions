class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        flag = False
        count = 0
        for i in range(1,len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                flag = True
                count += 1
        
        out = []
        for x in range(len(nums)):
            if count > 1:
                    out.append(0)
            elif nums[x] != 0 and flag:
                out.append(0)
            elif nums[x] == 0 and flag:
                out.append(product)
            else:
                out.append(int(product / nums[x]))
        return out