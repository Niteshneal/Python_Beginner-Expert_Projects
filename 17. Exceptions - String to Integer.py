n = input(":")
try:
    int_val = int(n)
    print(int_val)
except ValueError:
    print("bad string")
