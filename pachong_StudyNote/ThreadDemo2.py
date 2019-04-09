import threading
import time

# 使用线程锁解决不同步的问题.
VALUE = 0

lock = threading.Lock()

def add_value():
    global VALUE
    # 开启线程锁
    lock.acquire()
    for x in range(10000000):
        VALUE += 1
    # 释放线程锁
    lock.release()
    print("VALUE=%d" % VALUE)


def main():
    for x in range(3):
        t = threading.Thread(target=add_value)
        t.start()
        # time.sleep(1)


if __name__ == '__main__':
    main()
