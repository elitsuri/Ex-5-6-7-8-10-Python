# =======================================================
# Ex7_Class_EliyhoTsuri
# Name: Eliyho Tsuri
# Id: 201610672
# Login: eliyhots
# ===================== Qustion 1 =======================
# The function returns true or false if the array 
# is an array of symmetric amounts
print("Qustion 1")
#--------------------------------------------------------
def readInput(myList):
    for index in range(100):
        try:
            num = input("Please enter number 'end' to finish: " )
            if num == 'end': 
                break
            if not num.isdigit():
                raise ValueError('{} is not a number. Please try again..."'.format(index))
        except ValueError as e:
            print(e)
        else:
            myList.append(num)
#--------------------------------------------------------
def checkSum(myList):
    sum = 0
    fin = 0
    for start in myList:
        try:
            if len(myList) % 2 != 0:
                raise ValueError('ValueError : length of list is not even!')
            sum = int(start) + int(myList[fin-1])
            if fin == 0:
                tempSum = sum
            elif sum != tempSum:
                raise ValueError('ValueError : {} is not equal to {}'.format(sum, tempSum))
        except ValueError as e:
            print(e)
            return False
        else:
            fin = fin - 1
    print("Successfuly creating symmetric array amounts!")
    return True
#======================== Main ==========================
myList = []
readInput(myList)
print(checkSum(myList))
# =======================================================
print("\nQustion 2")
#--------------------------------------------------------
#The program receives a decimal number and a sum accuracy
# number and calculates the values ​​of the series as long 
# as the added number is not less than the accuracy level
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
#--------------------------------------------------------
from math import factorial
def calculate_exp(index, x, d, sum):
    try:
        if not is_float(x) or not is_float(d):
            raise ValueError ('x or d is not a float!')
        x = float(x)
        d = float(d)
        if x**index / factorial(index) < d:
            raise Exception ('{} ^ {} is smaller than d = {} so cannot be added'.format(x, index, d))
        print(x**index / factorial(index))
    except ValueError as x:
        print(x)
    except Exception as d:
        print(d)
        print('e^x = {}, number of elements in this serial: {}'.format(sum, index))
        return 0
    else:
        sum +=  x**index / factorial(index)
        return calculate_exp(index + 1, x, d, sum)     
#======================== Main ==========================
while (1):
    x = input('Please enter decimal number: ')  
    d = input('Please enter precision number: ') 
    calculate_exp(1, x, d, 0)
# =======================================================