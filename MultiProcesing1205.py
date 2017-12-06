#--coding='utf-8'--

import multiprocessing

def process(num):
    print("Number is {0}".format(num))


if __name__ == "__main__":
    process(7)
    for i in range(3):
        p = multiprocessing.Process(target=process,args=(i,))
        p.start()