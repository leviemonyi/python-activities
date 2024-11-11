class Temperature:
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    
    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")

# Create an instance of the Temperature class
temp = Temperature()

# Convert Celsius to Fahrenheit
temp.convertFahrenheit(25)  # Example: 25°C to Fahrenheit

# Convert Fahrenheit to Celsius
temp.convertCelsius(77)     # Example: 77°F to Celsius
