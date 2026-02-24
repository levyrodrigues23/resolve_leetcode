class Solution {
  int singleNumber(List<int> nums) {
    Map<int, int> map_numbers = {};
    for(int i = 0; i < nums.length; i++){
        map_numbers[nums[i]] = (map_numbers[nums[i]] ?? 0) + 1;
        
    }
    for(var entrie in map_numbers.entries){
        if (entrie.value == 1){
            return entrie.key;
        }
        
    }
    return -1;
    }
  }
