from functools import reduce
class GivenArgumentIsNotAlistError(Exception):
    "Raised when the given argument is not a list"
    pass
class Mathematics():
    def hcf(self, a, b):
        self.num1 = a
        self.num2 = b
        if self.num1 > self.num2:
            smaller = self.num2
        else:
            smaller = self.num1
        for i in range(1, smaller+1):
            if self.num1 % i == 0 and self.num2 % i == 0:
                hcfValue = i
        return hcfValue
    def lcm(self, a, b):
        self.num1 = a
        self.num2 = b
        if self.num1 > self.num2:
            greater = self.num1
        else:
            greater = self.num2
        while True:
            if greater%self.num1 == 0 and greater%self.num2 == 0:
                return greater
            greater+=1
    def factorial(self, n):
        self.n = n
        if self.n == 1:
            return 1
        elif self.n == 0:
            return 1
        else:
            return self.n*Mathematics.factorial(self, self.n-1)
    def list_hcf(self, list_with_numbers):
        self.listhcf = list_with_numbers
        if type(self.listhcf) == list:
            listHcfValue = reduce(lambda x, y: self.hcf(x, y), self.listhcf)
            return listHcfValue
        else:
            raise GivenArgumentIsNotAlistError("list_hcf() function requires a list argument.")
    def list_lcm(self, list_with_numbers):
        self.listlcm = list_with_numbers
        if type(self.listlcm) == list:
            listLcmValue = reduce(lambda x, y: self.lcm(x, y), self.listlcm)
            return listLcmValue
        else:
            raise GivenArgumentIsNotAlistError("list_lcm() function requires a list argument.")
    def list_factorial(self, list_with_numbers):
        self.listfact = list_with_numbers
        if type(self.listfact) == list:
            listFactValue = list(map(lambda n: self.factorial(n), self.listfact))
            return listFactValue
        else:
            raise GivenArgumentIsNotAlistError("list_factorial() function requires a list argument.")
methods = Mathematics() 
if __name__ == '__main__':   
    mylist = [10, 15, 20, 25]
    mylist2 = [0, 1, 2, 3, 4, 5]
    methods = Mathematics()
    print(methods.hcf(5, 10))
    print(methods.lcm(5, 10))
    print(methods.factorial(3))
    print(methods.list_hcf(mylist))
    print(methods.list_lcm(mylist))
    print(methods.list_factorial(mylist2))