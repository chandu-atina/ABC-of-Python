from modules import fibo
fibo.fib(10)

if __name__ == "__main__":
    import sys
    fibo.fib(int(sys.argv[1]))