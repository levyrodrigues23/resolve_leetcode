class Solution {
  String trimTrailingVowels(String s) {
    List<String> vowels = ['a','e','i', 'o', 'u'];


    for(int i = s.length - 1; i>=0;i--){
            if(vowels.contains(s[i].toLowerCase())){
                continue;
            } else{
                return s.substring(0, i+1);
            }
        }
    return "";
  }
}

