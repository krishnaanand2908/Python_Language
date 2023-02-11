from functools import reduce
import math
class Mathematics():
    class InvalidListInputError(Exception):
        "Raised when the given argument is not a list"
        
    class InvalidNumberInputError(Exception):
        "Raised when the given argument is not a whole number"
        
    def hcf(self, a, b):
        """This function calculates the HCF(Highest Common Multiple) or GCD(Greatest Common Divisor) of two numbers.
        
        Args:
            a (_integer_): _Argument a must be an integer because calculating the HCF or GCD of a non-integer number is not possible_
            b (_integer_): _Argument b must be an integer because calculating the HCF or GCD of a non-integer number is not possible_

        Returns:
            _integer_: _This function returns the HCF or GCD of the arguments a and b as an integer_
        """
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
        """This function calculates the LCM(Lowest Common Multiple) of two numbers.
        
        Args:
            a (integer): Argument a must be an integer because calculating the LCM of a non-integer number is not 
            b (integer): Argument b must be an integer because calculating the LCM of a non-integer number is not 

        Returns:
            : This function returns the LCM of the arguments a and b as an 
        """
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
        """This function calculates the facorial of a whole number n 

        Args:
            n (integer(greater than or equals to 0)): The factorial of a whole number n is the product of all the integers from n to 1. For example !n = n*(n-1)*(n-2)...*1
            Therefore n must be a whole number which greater than or equals to 0.

        Raises:
            Mathematics.GivenArgumentIsNotAWholeNumber: If the given argument is a whole number then this function raise an error because we can only calculate the factorial of whole number. In this cause instead of returning the wrong value this function raises an error.
            
        Returns:
            integer(greater than or equals to 0): This means that the return value is a whole number because the factorial of a number n must be a whole number.
        """
        self.n = n
        if self.n < 0:
            raise Mathematics.InvalidNumberInputError("factorial() function requires 1 argument n which must be a whole number!")
        if self.n == 1:
            return 1
        elif self.n == 0:
            return 1
        else:
            return self.n*Mathematics.factorial(self, self.n-1)
    def list_hcf(self, list_with_numbers):
        """This function is made to calculate the HCF or GCD of integers in a list so that you can find the hcf or gcd of numbers in a list and get a single return value.

        Args:
            list_with_numbers (list): the argument list_with_number must be of type list

        Raises:
            Mathematics.InvalidListInputError: If the given argument is not of a list type then this function raise an error

        Returns:
            integer: This function returns the hcf of all the number in the given list 
        """
        self.listhcf = list_with_numbers
        if type(self.listhcf) == list:
            listHcfValue = reduce(lambda x, y: self.hcf(x, y), self.listhcf)
            return listHcfValue
        else:
            raise Mathematics.InvalidListInputError("list_hcf() function requires a list argument.")
    def list_lcm(self, list_with_numbers):
        """This function is made to calculate the LCM of integers in a list so that you can find the lcm of numbers in a list and get a single return value.

        Args:
            list_with_numbers (list): the argument list_with_number must be of type list

        Raises:
            Mathematics.InvalidListInputError: If the given argument is not of a list type then this function raise an error

        Returns:
            integer: This function returns the hcf of all the number in the given list 
        """
        self.listlcm = list_with_numbers
        if type(self.listlcm) == list:
            listLcmValue = reduce(lambda x, y: self.lcm(x, y), self.listlcm)
            return listLcmValue
        else:
            raise Mathematics.InvalidListInputError("list_lcm() function requires a list argument.")
    def list_factorial(self, list_with_numbers):
        """This function inputs a list containing integers as an argument and appends the factorial of all the integers to a list named listFactValue. The factorial is calculated by using the Mathematics.factorial() function.

        Args:
            list_with_numbers (list): This function inputs a list containing integers as an argument

        Raises:
            Mathematics.InvalidListInputError: This error is raised when the given argument is not of a list data type

        Returns:
            list: This function returns a list containing the factorial of all the integers in the argument list
        """
        self.listfact = list_with_numbers
        if type(self.listfact) == list:
            listFactValue = list(map(lambda n: self.factorial(n), self.listfact))
            return listFactValue
        else:
            raise Mathematics.InvalidListInputError("list_factorial() function requires a list argument.")
    def sqr(self, number):
        """Returns the square of passed argument

        Args:
            number (int or float): number argument is the number to be squared

        Returns:
            int or float:
                square of the passed argument
        """
        return number**2
    
    def list_sqr(self, list_with_numbers):
        """Returns a list of squared numbers in the list passed as an argument

        Args:
            list_with_numbers (list):
                List of numbers which are to be squared

        Raises:
            Mathematics.InvalidListInputError: Raised when the provided input is not of a list type

        Returns:
            list: The list of squared numbers in the list passed as the argument
        """
        if type(list_with_numbers) != list:
            raise Mathematics.InvalidListInputError("list_factorial() function requires a list argument.")
        else:
            return list(map(lambda n: self.sqr(n), list_with_numbers))
        
    def cube(self, number):
        """Returns the cube of passed argument

        Args:
            number (int or float): number argument is the number to be cubed

        Returns:
            int or float:
                cube of the passed argument
        """
        return number**3
    
    def list_cube(self, list_with_numbers):
        """Returns a list of cubed numbers in the list passed as an argument

        Args:
            list_with_numbers (list):
                List of numbers which are to be cubed

        Raises:
            Mathematics.InvalidListInputError: Raised when the provided input is not of a list type

        Returns:
            list: The list of cubed numbers in the list passed as the argument
        """
        if type(list_with_numbers) != list:
            raise Mathematics.InvalidListInputError("list_factorial() function requires a list argument.")
        else:
            return list(map(lambda n: self.cube(n), list_with_numbers))
        
    def sqrt(self, x):
        """Returns the square root of the given number x

        Args:
            x (int or float):
                The number of which you want to calculate the square root

        Returns:
            int or float: 
                Returns the square root of x
        """
        return math.sqrt(x)
    
    def list_sqrt(self, list_with_numbers):
        """Returns a list containing the square roots of the number present in the list passed as the argument

        Args:
            list_with_numbers (list):
                list contaning the ints or floats or both to find the their square roots.

        Raises:
            Mathematics.InvalidListInputError: raises when the given argument is not of list type

        Returns:
            list:
                this list containts the squaree roots of all the numerical items present in the argument list 
        """
        if type(list_with_numbers) != list:
            raise Mathematics.InvalidListInputError("list_sqrt() function requires a list argument.")
        else:
            return list(map(lambda x: self.sqrt(x), list_with_numbers))
    
    def cbrt(self, x):
        """Returns the cube root of the given number x

        Args:
            x (int or float):
                The number of which you want to calculate the cube root

        Returns:
            int or float: 
                Returns the cube root of x
        """
        return math.cbrt(x)
    
    def list_cbrt(self, list_with_numbers):
        """Returns a list containing the cube roots of the number present in the list passed as the argument

        Args:
            list_with_numbers (list):
                list contaning the ints or floats or both to find the their cube roots.

        Raises:
            Mathematics.InvalidListInputError: raises when the given argument is not of list type

        Returns:
            list:
                this list containts the cube roots of all the numerical items present in the argument list 
        """
        if type(list_with_numbers) != list:
            raise Mathematics.InvalidListInputError("list_cbrt() function requires a list argument.")
        else:
            return list(map(lambda x: self.cbrt(x), list_with_numbers))
    
    def expo(base, power):
        """This function returns the value of 'base' to the 'power' 

        Args:
            base (int or float): base value of exponent
            power (int or float): power value of exponent

        Returns:
            int or float: base^power
        """
        return base**power
methods = Mathematics() # Must import the object methods if you want to use all the function of this Mathematics class. Use "from mathematics import methods" to import it.

if __name__ == '__main__':
    pass