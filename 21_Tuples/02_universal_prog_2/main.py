def is_prime(num):
    if num <= 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_elements(seq):
    return [value for i, value in enumerate(seq) if is_prime(i)]

