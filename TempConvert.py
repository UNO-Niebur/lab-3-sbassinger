#TempConvert.py
#Name:Scott Bassinger 
#Date:02/17/2026
#Assignment:Lab3-TempConvert


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = float(input("What is the temperature in degrees Fahrenheit? (Please provide a number)"))
  

  tempC = round((tempF - 32) * (5/9),1)

  print(tempF, "degrees Fahrenheit is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
