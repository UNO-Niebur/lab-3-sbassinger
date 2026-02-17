#ApproxPi.py
#Name:Scott Bassinger
#Date:02/16/2026
#Assignment:Lab3-ApproxPi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  evalto = int(input("How many decimals should I evaluate pi to? (Up to ten, don't be mean) "))
  start = time.time()
  #calculate pi using the approximation technique
  piapprox = 4/1
  sign = -1
  denom = 3
  #Loop until the level of precision is reached
  loopcount = 0
  if evalto <= 10:
    while round(piapprox,evalto) != round(realPi,evalto):
      piapprox = piapprox + (4 * sign / denom)
      sign = sign * -1
      denom = denom + 2
      loopcount = loopcount + 1
    end = time.time()
    elapsedTime = round(end - start,5)
    print(round(piapprox,evalto))
    print("I completed this operation in",elapsedTime,"seconds")
    print("This took",loopcount,"loops")
    if elapsedTime > 5:
      print("Why must you work me so?")
  else: print("Sorry, that value is too high!")
if __name__ == '__main__':
  main()
