import time

def print_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 的执行时间为: {end_time - start_time} 秒")
        return result
    return wrapper

all0 = ['0' for _ in range(10**8)]
all1 = ['1' for _ in range(10**8)]

@print_time
def a():
    a0 = [int(x) for x in all0]
    a1 = [int(x) for x in all1]

@print_time
def b():
    b0 = [1 if x=='1' else 0 for x in all0]
    b1 = [1 if x=='1' else 0 for x in all1]


'''
函数 a 的执行时间为: 14.713196039199829 秒
函数 b 的执行时间为: 4.6136860847473145 秒
'''

if __name__ == '__main__':
    a() 
    b() 