# programme to increase the value of funtion by 2
def myfunction(function1):  # myfuntion is decorator name and function1 is another function
    def inner():
        value = function1()
        result = value + 2
        return result

    return inner  # return inner function


@myfunction
def number():
    return 10


print(number)