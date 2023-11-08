def bisection_method(func, a, b, tol, max_iter):
    if func(a) * func(b) >= 0:
        raise ValueError("Fungsi pada interval [a, b] tidak memenuhi syarat metode biseksi.")

    iter_count = 0

    while (b - a) / 2.0 > tol and iter_count < max_iter:
        c = (a + b) / 2.0
        if func(c) == 0.0001:
            break

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iter_count += 1

    return (a + b) / 2.0

# Contoh penggunaan metode biseksi untuk mencari akar fungsi x^3 - x^2 + 2
def func(x):
    return  x**4 - x**3 + 2*x**2 - 2*x -12

a = -2.0  # Batas bawah interval
b = 0.0   # Batas atas interval
tolerance = 0.0001
max_iterations = 15

root = bisection_method(func, a, b, tolerance, max_iterations)
print("Akar fungsi: ", root)
