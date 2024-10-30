import time
from contextlib import contextmanager
class cm_timer_1:
    def __enter__(self):
        self.startTime = time.time()
        return self
    
    def __exit__(self, type, value, trecaback):
        self.endTime = time.time()
        self.elapsedTime = self.endTime - self.startTime
        print(f'Elapsed time: {self.elapsedTime} секунд')

@contextmanager
def cm_timer_2():
    startTime = time.time()
    try:
        yield
    finally:
        endTime = time.time()
        elapsedTime = endTime - startTime
        print(f'Elapsed time: {elapsedTime} секунд')
"""       
def main():
    with cm_timer_1():
        print('Hello, world!')
        
        print('Блок кода выполнен')
        
    with cm_timer_2():
        print('Hello, world!')
        print('Блок кода выполнен')

main()
"""