import multiprocessing
import time

def sleep(secs):
    print(f'Sleeping {secs} second(s)...')
    time.sleep(secs)
    print('Done Sleeping...')

if __name__ == '__main__':
    
    start = time.perf_counter()
    processes = []
    
    for _ in range(10):
       
        p = multiprocessing.Process(target=sleep, args=[1])
        p.start()
        processes.append(p)

    for process in processes:
        process.join() 

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')
