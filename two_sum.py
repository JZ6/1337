from typing import List

import pytest

class Solution:
    @staticmethod
    def two_sum_answer(nums: List[int], target: int) -> List[int]:
       
        seen_nums = {}
        
        for i in range(len(nums)):
            val = nums[i]
            
            target_num = target - val
            
            if(target_num in seen_nums):
                return [seen_nums[target_num],i]
            
            seen_nums[val] = i



def test_two_sum_answer():
    nums = [2, 7, 11, 15]
    target = 9   

    answer = Solution.two_sum_answer(nums,target)

    assert set(answer) == {0,1}
    
def test_two_sum_answer_two():
    nums = [2, 7, 11, 15]
    target = 18   

    answer = Solution.two_sum_answer(nums,target)

    assert set(answer) == {1,2}


pytest.main()
