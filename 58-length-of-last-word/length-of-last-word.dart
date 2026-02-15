class Solution {
  int lengthOfLastWord(String s) {
    List<String> palavras = s.split(RegExp(r'\s+'));
    
    if(palavras.last == ''){
        int penultimo = palavras.reversed.elementAt(1).length;
        return penultimo;
    } else{
        return palavras.last.length;
    }
    
   // eu tenho s
   // eu tenho que pegar a ultima palavra
   // eu tenho que pegar o tamanho da ultima palavra 
  }
}