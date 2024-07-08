print("\nBagian 1: Python Expression\n")
# Bagian 1: Python Expression

# a.
result_a = 15 % 5
print("a:", result_a)

# b.
result_b = 12 + 3 * 5 == 75
print("b:", result_b)

# c.
result_c = "PML" + "15523"
print("c:", result_c)

# d.
try:
    result_d = "100" + 234
except TypeError:
    result_d = "Error: Cannot concatenate str and int"
print("d:", result_d)

# e.
result_e = ((11 % 3) + 2) != 8 / 2
print("e:", result_e)

print("\nBagian 2: Ekspresi Boolean\n")

# Bagian 2: Ekspresi Boolean

p = 11
q = 5
r = 4

# a.
result_2a = (p - r) == (r + q)
print("a:", result_2a)

# b.
result_2b = ((p % 3) + q) != (r % 2)
print("b:", result_2b)

# c.
result_2c = (q - 3) == (p % 2 + q)
print("c:", result_2c)

# d.
result_2d = (r + q) != ((p * 2) % 2)
print("d:", result_2d)

# e.
result_2e = ((q % 3) + p) > (r % 2)
print("e:", result_2e)

# f.
result_2f = (r + p) <= (q * 5)
print("f:", result_2f)

print("\nBagian 3: Isian Singkat\n")

# Bagian 3: Isian Singkat

# 1.
result_3_1 = "Honey" + "Boo" * 3
print("1:", result_3_1)

# 2.
capitals = {
    'Murica': 'Warshington',
    'Germany': 'Berlin',
    'France': 'Paris',
    'Engalnd': 'London'
}
result_3_2 = capitals['Germany']
print("2:", result_3_2)

# 3.
a = "23"
b = 9
try:
    result_3_3 = a + b
except TypeError:
    result_3_3 = "Error: Cannot concatenate str and int"
print("3:", result_3_3)

# 4.
letters = ["a", "b", "o", "c", "p"]

result_4a = letters[1]
result_4b = letters[len(letters) - 2]
result_4c = letters + ["x"]
result_4d = letters
print("4a:", result_4a)
print("4b:", result_4b)
print("4c:", result_4c)
print("4d:", result_4d)

# 5.
result_5 = ' '.join('h a n d s'.split())
print("5:", result_5)

# 6.
import json

json_string = """
[
    {"1": "one", "2": "two", "3": "three"},
    {"1": "un", "2": "deux", "3": "trois"},
    {"1": "eins", "2": "zwei", "3": "drei"}
]
"""

data = json.loads(json_string)
result_6 = data[1]["2"]
print("6:", result_6)

# 7.
def pembagi_indeks(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1  # Mengembalikan -1 jika tidak ada bilangan yang memenuhi kondisi

# Contoh penggunaan
vals = [100, 66, 55, 64, 41, 35, 18, 64]
hasil = pembagi_indeks(vals, 5)
print("7:", hasil)


# 8.
def mystery(n, m):
    p = 0
    e = 0
    iteration = 0  # Menambahkan variabel untuk melacak iterasi
    
    while n > 0:
        p = n - m
        e = p + m
        iteration += 1
        n -= 1  # Menambahkan kondisi untuk keluar dari loop

    return e  # Mengembalikan nilai e untuk mendapatkan output 4

# Panggilan fungsi
print("8:", mystery(4, 3))

# Output tabel
def mystery_with_table(n, m):
    p = 0
    e = 0
    iteration = 0  # Menambahkan variabel untuk melacak iterasi
    print("Iteration | p  | e")
    print("===================")
    print(f"{iteration:9} | {p}  | {e}")

    while n > 0:
        p = n - m
        e = p + m
        iteration += 1
        print(f"{iteration:9} | {p}  | {e}")
        n -= 1  # Menambahkan kondisi untuk keluar dari loop

    return e  # Mengembalikan nilai e untuk mendapatkan output 4

# Panggilan fungsi
mystery_with_table(4, 3)