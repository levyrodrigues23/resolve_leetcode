class Solution {
  int reverseDegree(String s) {
 
    List<String> alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');
    List<String> novoAlfabeto = [];
    for(final elemento in alfabeto){
        novoAlfabeto.add(elemento.toLowerCase());
    }
    List<String> alfabeto_invertido = novoAlfabeto.reversed.toList();
    List<String> elementos = s.split('');
    int soma = 0;
    for(var i = 0; i < elementos.length; i++){
        int posicaoIndex = alfabeto_invertido.indexOf(elementos[i]) +1;
        int posicaoString = i + 1;

        soma += posicaoString * posicaoIndex;
    }

    return soma;
}
}