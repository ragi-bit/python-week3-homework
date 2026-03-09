def capitalize(text):
    """Padara pirmo burtu lielu."""
    return text.capitalize()


def truncate(text, max_len=20):
    """Saīsina tekstu."""
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."


def count_words(text):
    """Saskaita vārdus."""
    return len(text.split())


def clamp(num, low, high):
    """Ierobežo skaitli."""
    return max(low, min(num, high))


def is_prime(num):
    """Pārbauda vai skaitlis ir pirmskaitlis."""
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def factorial(n):
    """Aprēķina faktoriālu."""
    if n < 0:
        raise ValueError("n nevar būt negatīvs")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def total(numbers):
    """Saraksta summa."""
    s = 0

    for n in numbers:
        s += n

    return s


def average(numbers):
    """Vidējais."""
    return total(numbers) / len(numbers)


if __name__ == "__main__":
    print(capitalize("hello"))
    print(truncate("This is a long text", 10))
    print(count_words("Python is awesome"))
    