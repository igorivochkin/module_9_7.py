#module_9_7.py

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        iter_ = 0
        for i in range(2, result - 1):
            if result % i == 0:
                iter_ += 1
        if iter_ == 0:
            print("Простое")
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    sum_ = a+b+c
    return sum_

result = sum_three(2, 3, 6)
print(result)

