import time
import concurrent.futures


def sleep(secs):
    print(f'Sleeping {secs} second(s)...')
    time.sleep(secs)
    return f'Done Sleeping...{secs}'

if __name__ == '__main__':
    
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(sleep, sec) for sec in secs]
    
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} second(s)')