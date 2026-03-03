class Solution {
  int differenceOfSums(int n, int m) {
    int somaDivisiveis = 0;
    int somaNdivisiveis = 0;
    for(var i = 1; i < n + 1; i++ ){
        if(i % m != 0){
            somaDivisiveis += i;
        } else{
            somaNdivisiveis += i;
        }
        
    
    }
    return somaDivisiveis - somaNdivisiveis;
  }
}