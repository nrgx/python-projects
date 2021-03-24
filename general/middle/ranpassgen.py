import random


symbols = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "=",
    "_",
    "+",
    "{",
    "}",
    "|",
    "/",
    "\\",
    ":",
    ";",
    "'",
    '"',
    ",",
    ".",
    "<",
    ">",
    "?",
]
digits = list(range(0, 10))
uppercase = list(map(lambda i: chr(i), range(65, 91)))
lowercase = list(map(lambda i: chr(i), range(61, 123)))


def ranpassgen():
    password_length = int(input("Password length\n"))
    password = ""
    for _ in range(password_length):
        element = random.choice([symbols, digits, uppercase, lowercase])
        password += str(random.choice(element))
    return password


if __name__ == '__main__':
    print(ranpassgen())
