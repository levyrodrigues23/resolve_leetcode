

class Solution {
  String intToRoman(int num) {
    final Map<int, String> romanMap = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
    };

    String result = '';

  for(MapEntry<int, String> entry in romanMap.entries){
    var key = entry.key;
    var value = entry.value;
    while(num >= key){
        result += value;
        num = num - key;
    }
  
    

  }

     return result;
  }

}