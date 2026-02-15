class Solution {
  bool isSubsequence(String s, String t) {
    int posT = 0;  // ponteiro posição em t
    for (var i = 0; i < s.length; i++) {
      bool found = false;
      for (var j = posT; j < t.length; j++) {  // continua de onde parou!
        if (s[i] == t[j]) {
          found = true;
          posT = j + 1;  // próxima busca após esse match
          break;
        }
      }
      if (!found) return false;
    }
    return true;
  }
}
