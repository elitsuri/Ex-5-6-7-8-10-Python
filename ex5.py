# =======================================================
# Ex5_Class_EliyhoTsuri
# Name: Eliyho Tsuri
# Id: 201610672
# Login: eliyhots
# --------------------- Qustion 1 -----------------------
#import product
# ---------------------- Main ---------------------------
class Product:
    pass
    
Bread = Product()
Bread.name = "Bread"
Bread.code = 100001  
Bread.amount = 10
Bread.minAmount = 10
Bread.price = 5.90

Milk = Product()
Milk.name = "Milk"
Milk.code = 100002  
Milk.amount = 20
Milk.minAmount = 14
Milk.price = 7.30

OrangeJuice = Product()
OrangeJuice.name = "Orange Juice"
OrangeJuice.code = 100003  
OrangeJuice.amount = 8
OrangeJuice.minAmount = 5
OrangeJuice.price = 6.60

Cigarettes = Product()
Cigarettes.name = "Orange Juice"
Cigarettes.code = 100004  
Cigarettes.amount = 20
Cigarettes.minAmount = 20
Cigarettes.price = 21.50

Rice = Product()
Rice.name = "Rice"
Rice.code = 100005  
Rice.amount = 5
Rice.minAmount = 3
Rice.price = 7.00
        
Chocolate = Product()
Chocolate.name = "Dark Chocolate"
Chocolate.code = 100006  
Chocolate.amount = 10
Chocolate.minAmount = 7
Chocolate.price = 4.90
 

Pasta = Product()
Pasta.name =  "Pasta"
Pasta.code = 100007  
Pasta.amount = 10
Pasta.minAmount = 8
Pasta.price = 10.50


Cottage = Product()
Cottage.name = "Cottage"
Cottage.code = 100008  
Cottage.amount = 7
Cottage.minAmount = 15
Cottage.price = 100.00


def printProducts(arr):
    for i in range(len(arr)):
        print(arr[i].name,arr[i].code,arr[i].amount,arr[i].minAmount,arr[i].price)

def printMin(arr):
    for i in range(len(arr)):
        if arr[i].amount < arr[i].minAmount:
            print(arr[i].name,arr[i].code,arr[i].amount,arr[i].minAmount,arr[i].price)

def setOrder(name,code):    
    product = Product()
    product.name = name  
    product.code = code
    product.amount = input("Enter amount: ")
    product.minAmount = input("Enter min amount: ")
    product.price = input("Enter price: ")
    return product
def sellOrder(name,amount):
    for i in range(len(arr)):
        if arr[i].name == name:
            if amount > 0:
                print(name,"can be sold and this price is",arr[i].price)
            
arr = [Bread,Milk,OrangeJuice,Cigarettes,Rice,Chocolate,Pasta,Cottage]
printProducts(arr)
print("")
printMin(arr)
print("")
for i in range(len(arr)):
    setOrder(arr[i].name,arr[i].code)
sellOrder(arr[i].name,arr[i].amount)
   