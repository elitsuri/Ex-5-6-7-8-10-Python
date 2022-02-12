# =======================================================
# Ex8_Class_EliyhoTsuri
# Name: Eliyho Tsuri
# Id: 201610672
# Login: eliyhots
# ===================== Qustion 1 =======================
# The function get list and gows from end to the start
print("Qustion 1")
# -------------------------------------------------------
class iter_reverse1(object):
    def __init__(self,n):
        self.mylst=n
        self.size=len(n)
    def __next__(self):
        if self.size>0:
            num,self.size=self.mylst[self.size-1],self.size-1
            return num
# ======================= Main =========================
list = [1, 2, 3]
list = iter_reverse1(list)
print(next(list))
print(list.__next__())
print(list.__next__())

# ===================== Qustion 2 =======================
# The function working same the enumerate  funcgtion
print("Qustion 2")
# -------------------------------------------------------
class iter_reverse2(object):
    def __init__(self,n):
        self.mylst = n
        self.size = len(n)
        self.start = 0;
    def __enumerate__(self):
        num,self.size = self.mylst[self.size-1],self.size+1
        return(num,self.start)
# ======================= Main =========================
list = [1, 2, 3]
list = iter_reverse2(list)
print(list.__enumerate__())