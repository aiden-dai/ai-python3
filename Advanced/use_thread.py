import concurrent.futures
import threading
import time


def do_something(seconds, name):
    print(f"Start {name}")
    time.sleep(seconds)
    print(f"{name} is completed.")


start = time.time()

t1 = threading.Thread(target=do_something, args=[1, 't1'])
t2 = threading.Thread(target=do_something, args=[2, 't2'])
t1.start()
t2.start()

t1.join()
t2.join()


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(do_something, 1, 't3')


end = time.time()


print(f'Complete in {end-start} seconds')
