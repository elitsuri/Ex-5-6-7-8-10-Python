# =======================================================
# Ex6_Class_EliyhoTsuri
# Name: Eliyho Tsuri
# Id: 201610672
# Login: eliyhots
# =======================================================
import re
#--------------------------------------------------------
def printFromFile():
    file = open("us_postal_codes.csv",'r')
    rows = (input("Enter an number rows to print: "))
    print("")
    index = 0
    file.__next__()
    while (index < int(rows)):
        index += 1
        c = file.readlines(3)
        print(c)
    file.close()
#--------------------------------------------------------
def checkCity():
    file = open("us_postal_codes.csv",'r')
    city = (input("Enter city to check on file: "))
    next(file)
    flag = False
    for line in file:
        res = re.search(r"((\d+),([\w\s'/-]+),,?([\w\s]+).*)*", line)
        try:
            check = res.group(4)
            if check == city:
                print("The city is on the file")
                flag = True
                break
        except:
            pass
    if flag == False:
        print("The city is ont on the file")
    file.close()
#--------------------------------------------------------
def checkPostal():
    file = open("us_postal_codes.csv",'r')
    code = (input("Enter Postal code to check on file: "))
    next(file)
    flag = False
    for line in file:
        res = re.search(r"((\d+),([\w\s'/-]+),,?([\w\s]+).*)*", line)
        try:
            check = res.group(2)
            if check == code:
                print("The Postal code is on the file")
                flag = True
                break
        except:
            pass
    if flag == False:
        print("The Postal code is ont on the file")
        file.close()
#--------------------------------------------------------
def writeState():
    read_file = open("us_postal_codes.csv",'r')
    next(read_file)
    index = 0
    state_list = {}
    for line in read_file:
        res = re.search(r"((\d+),([\w\s'/-]+),,?([\w\s]+).*)*", line)
        try:
            state = res.group(4)
            if checkOnlist(state_list,state) == True:
                state_list[index] = state
                index += 1
        except:
            pass
    sorted(str(state_list.values()))    
    write_file = open("unique_names.txt",'w')
    for index in range(len(state_list)-1):
        write_file.write(state_list[index])
        write_file.write("\n")
    read_file.close()
    write_file.close()
#--------------------------------------------------------
def checkOnlist(state_list,state):
    for x in range(len(state_list)):
        if state_list[x] == state:
            return False
    return True        
#----------------------- Main ---------------------------
printFromFile()
checkCity()
checkPostal()
writeState()