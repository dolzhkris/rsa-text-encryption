from sympy import isprime

p = int(input("Введите простое число p: "))
q = int(input("Введите простое число q: "))

if not isprime(p) or not isprime(q):
    print("Ошибка: p и q должны быть простыми числами")
    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q: "))

n = p * q
phi = (p - 1) * (q - 1)

# взаимно простое с phi
e = 3
while True:
    if e < phi and phi % e != 0:
        break
    e += 2
d = 1
while (d * e) % phi != 1:
    d += 1

print(f"\nОткрытый ключ: ({e}, {n})")
print(f"Закрытый ключ: ({d}, {n})")

text = input("\nВведите текст: ")

encrypted = []
decrypted = ""
for char in text:
    m = ord(char)  # код символа
    
    # шифрование C = m^e mod n
    c = pow(m, e, n)
    encrypted.append(c)
    # дешифрование m = C^d mod n
    m_dec = pow(c, d, n)
    char_dec = chr(m_dec)
    decrypted += char_dec
    
print(f"\nСимвол: '{char}\tКод (m): {m}\tШифрование: C = {m}^{e} mod {n} = {c}\tДешифрование: m = {c}^{d} mod {n} = {m_dec} = '{char_dec}'")
print("\nЗашифрованный текст:", encrypted)
print("Расшифрованный текст:", decrypted)
