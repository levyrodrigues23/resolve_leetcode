class Solution {
  List<int> plusOne(List<int> digits) {
   int size = digits.length;
   for(int i = size - 1; i >= 0; i--){
    if(digits[i] < 9){
        digits[i]++;
        return digits;
    }

    digits[i] = 0;
   }

   digits.insert(0, 1);
   return digits;
  }
}