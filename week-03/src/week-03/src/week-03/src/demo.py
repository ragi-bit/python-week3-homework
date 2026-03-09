from utils import capitalize, clamp, is_prime, average, factorial
from validators import is_email, is_strong_password


print("=== Utils demonstrācija ===")

print(capitalize("hello"))
print(clamp(15, 0, 10))
print(is_prime(17))
print(average([10, 20, 30]))

try:
    print(factorial(-1))
except ValueError as e:
    print("Error:", e)


print("\n=== Validators ===")

print(is_email("test@test.lv"))
print(is_strong_password("abc12345"))
