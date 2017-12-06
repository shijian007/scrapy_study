from threading import Thread
from queue import Queue

global my_queue
my_queue = Queue()


class MyThread1(Thread):
    def __init__(self):
        Thread.__init__(self)
        # super(MyThread1, self).__init__()

    def run(self):
        put_data = "you producer data"
        my_queue.put(put_data)
        # write this thread task
        pass


class MyThread2(Thread):
    def __init__(self):
        Thread.__init__(self)
        # super(MyThread2, self).__init__()

    def run(self):
        get_data = my_queue.get()
        # write this thread task
        pass


if __name__ == '__main__':
    thread1 = MyThread1()
    thread2 = MyThread2()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()  