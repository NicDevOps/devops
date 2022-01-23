import time

def func_timer(func):
    def inner():
        print("I got decorated")
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(end - start)
    return inner

@func_timer
def ordinary():
    time.sleep(2)
    print("I am ordinary")

def main():
    ordinary()

if __name__  ==  '__main__':
    main()