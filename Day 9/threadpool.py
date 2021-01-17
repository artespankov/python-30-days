import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done {seconds} sec sleeping...'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 3, 2, 1]
    # # schedules function and returns feature
    # results = [executor.submit(do_something, sec) for sec in secs]
    # # yield results of threads when done execution
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # or return results directly
    results = executor.map(do_something, secs)
    for result in results:
        print(result)


finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")
