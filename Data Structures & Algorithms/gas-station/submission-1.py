class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if we can even complete the circut
        if sum(gas) < sum(cost):
            return -1

        count = 0
        res = 0
        for i in range(len(gas)):
            # check can we even continue
            count += gas[i] - cost[i]
            if count < 0:
                count = 0
                res = i + 1
 
        return res
            
        