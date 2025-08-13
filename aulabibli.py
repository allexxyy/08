from scipy.constants import zero_Celsius

temperatura_celsius = 20
# Converter Celsius para Kelvin e depois para Fahrenheit
temperatura_fahrenheit = ((temperatura_celsius + zero_Celsius - 273.15) * 9/5) + 32

print(f"{temperatura_celsius} graus Celsius é equivalente a {temperatura_fahrenheit:.2f} graus Fahrenheit.")
