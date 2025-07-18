class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        altitude_maxima = 0

        for elemento in gain:
            altitude += elemento
            altitude_maxima = max(altitude_maxima, altitude)
        return altitude_maxima

        


            
        