# coding: utf-8
# divisor 約数列挙


def make_divisor_list(num):
    if num < 1:
        return []
    elif num == 1:
        return [1]
    else:
        divisor_list = []
        divisor_list.append(1)
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                divisor_list.append(i)
        divisor_list.append(num)

        return divisor_list


print(make_divisor_list(28))

# prime 素数列挙
import math


def is_prime(num):
    if num < 2:
        return False
    else:
        num_sqrt = int(math.floor(math.sqrt(num)))
        for prime in range(2, num_sqrt + 1):
            if num % prime == 0:
                return False
        return True


def make_prime_list(num):
    if num < 2:
        return []

    prime_list = []
    for prime in range(2, num + 1):
        if is_prime(prime):
            prime_list.append(prime)
    return prime_list


print(make_prime_list(28))
