class Solution {
  List<double> convertTemperature(double celsius) {
    final double kelvin = celsius + 273.15;
    final double fahrenheit = celsius * 1.80 + 32.00;
    final novaLista = [kelvin, fahrenheit];
    return novaLista;

  }
}