import multiprocessing
import time

def sleep(secs):
   
    print(f'Sleeping {secs} second(s)...')
    time.sleep(secs)
    print('Done Sleeping...')

if __name__ == '__main__':
    
    start = time.perf_counter()
    
    p1 = multiprocessing.Process(target=sleep, args=[1])
    p2 = multiprocessing.Process(target=sleep, args=[1])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')
