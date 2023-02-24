def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    n = 16
    print("The Fibonacci series for", n)
    for i in range(n):
        print(fib(i), end=", ")
    print("...")

if __name__ == "__main__":
    main()
