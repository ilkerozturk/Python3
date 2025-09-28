""" #encapsulation örneği


def capsule(value):
    def decorator(value):
        returning = value + 5
        print(returning)
    return decorator(value)
    
capsule(340)  # 15 döner 



#nested factorial function örneği

def factorial(n):
    def inner_factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * inner_factorial(n - 1)
    return inner_factorial(n)

print(factorial(4))  # 120 döner """


