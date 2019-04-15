import threading
import time


class SleepingThread(threading.Thread):
    def run(self):
        for x in range(1, 5):
            print(threading.current_thread())
            time.sleep(1)


class WorkingThread(threading.Thread):
    def run(self):
        for x in range(1, 5):
            print(threading.current_thread())
            time.sleep(1)


def main():
    t1 = SleepingThread()
    t2 = WorkingThread()

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
