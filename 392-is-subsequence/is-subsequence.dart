class Solution {
  bool isSubsequence(String s, String t) {
    int posT = 0; 
    for (var i = 0; i < s.length; i++) {
      bool found = false;
      for (var j = posT; j < t.length; j++) {  
        if (s[i] == t[j]) {
          found = true;
          posT = j + 1;  
          break;
        }
      }
      if (!found) return false;
    }
    return true;
  }
}
