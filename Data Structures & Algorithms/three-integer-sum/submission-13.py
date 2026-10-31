class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort nums
        nums.sort()
        result = [ ]        
        #make a hash { -nums[k] : k}
        hashmap = {}
        for k in range(len(nums)):
            hashmap[-nums[k]] = k
        # consider i < j < k
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[i] + nums[j] in hashmap:
                    k = hashmap[nums[i] + nums[j]]
                    if k > j:
                        result.append([nums[i],nums[j],nums[k]])
                        #This result can contain duplicates

        final_result = [list(t) for t in {tuple(sorted(t)) for t in result}]

        return final_result
