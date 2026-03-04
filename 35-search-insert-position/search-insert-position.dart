class Solution {
  int? searchInsert(List<int> nums, int target) {
    for(var i = 0; i < nums.length; i++){
        if(target == nums[i]){
            return i;
        } 
    } 
    
    var incrementador = 0;
    var menor = nums.length;
    while(incrementador < nums.length){

      
       if(target <= nums[incrementador]) {
           menor = incrementador;
            break;
    }
        incrementador ++;
    } 
    
    if(target > nums.last) {
        return nums.indexOf(nums.last) + 1;
    } else{
        return menor;
    }
  }
}