def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def sum_of_primes(n):
    total = 0
    for i in range(2, n):
        if is_prime(i):
            total += i
    return total

# Nhập giá trị từ người dùng
n = int(input("Nhập số nguyên n: "))
print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {sum_of_primes(n)}")
