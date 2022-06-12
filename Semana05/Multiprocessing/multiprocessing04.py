import time
import concurrent.futures


def sleep(secs):
    print(f'Sleeping {secs} second(s)...')
    time.sleep(secs)
    return 'Done Sleeping...'

if __name__ == '__main__':
    
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(sleep, 1)
        f2 = executor.submit(sleep, 1)
        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()


    print(f'Finished in {round(finish-start,2)} second(s)')