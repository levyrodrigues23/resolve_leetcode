class Solution {
  void merge(List<int> nums1, int m, List<int> nums2, int n) {
    List<int> novaLista = [
        ...nums1.sublist(0, m),
        ...nums2.sublist(0, n)
    ];
    novaLista.sort();
    
    for(var i = 0; i < novaLista.length; i++ ){
        nums1[i] = novaLista[i];
    }
   
   
    
  }
}