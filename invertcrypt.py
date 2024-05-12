import sys
x = []
for letter in sys.argv[1]:
    x.append(chr(122-(ord(letter)-97)))
v = lambda v: print(v, end="")
list(map(v, x))
print()

with open(sys.argv[2], "r") as f:
    for line in f:
        x = []
        for letter in line:
            if letter.isalpha():
                print(letter, end="")
                print(" ", end="")
                x.append(chr(122-(ord(letter)-97)))
        print("==> ", end="")
        list(map(v, x))
        print()