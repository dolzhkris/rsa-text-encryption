# rsa-text-encryption
Python implementation of the RSA public-key encryption algorithm for text data.

## About

The program accepts two prime numbers, generates an RSA key pair, encrypts the entered text character by character, and immediately decrypts each encrypted character. 

The project was developed as part of university work during the fourth year of university.


## Key Generation

The program generates two keys.

1. Public Key

```text
(e, n)
```

The public key is displayed as:

```text
Открытый ключ: (e, n)
```

2. Private Key

```text
(d, n)
```

The private key is displayed as:

```text
Закрытый ключ: (d, n)
```

## Key Variables

* p - first input prime number;
* q - second input prime number;
* n - RSA modulus;
* phi - Euler's totient function value;
* e - public exponent;
* d - private exponent;
* text - input text;
* encrypted - list containing encrypted numerical values;
* decrypted - resulting decrypted text;
* char - current character being processed;
* m - numerical code of the current character;
* c - encrypted numerical value;
* m_dec - decrypted numerical value;
* char_dec - restored character.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dolzhkris/rsa-text-encryption.git
```

2. Install the required library:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
python main.py
```

Enter two prime numbers. Then enter the text.


GitHub: [@dolzhkris](https://github.com/dolzhkris)
