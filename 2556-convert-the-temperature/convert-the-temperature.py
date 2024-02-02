class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Convert Celsius to Kelvin
        kelvin = round(celsius + 273.15, 5)

        # Convert Celsius to Fahrenheit
        fahrenheit = round(celsius * 1.80 + 32.00, 5)

        # Return the results as an array
        ans = [kelvin, fahrenheit]
    
        return ans
        