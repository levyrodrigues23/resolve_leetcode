class Solution {
  bool? canConstruct(String ransomNote, String magazine) {
    List<String> letras = magazine.split('');
    String valorFinal = '';
   
    
    for(var i = 0; i < ransomNote.length; i++){
        bool encontrou = false;
        for(var j = 0; j < letras.length; j++){
            if(ransomNote[i] == letras[j]){
                valorFinal += letras[j];
                letras[j] = '#';
                encontrou = true;
                break;
    
            }



        }
                    if(!encontrou) return false;
   
    }
        return true;
  }
}