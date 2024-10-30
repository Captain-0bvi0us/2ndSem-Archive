import json
import random
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique 

path = "C:/Users/123/Documents/Work/Programs/2ndSem-WorkLab3-4/lap_python_fp/data_light.json"
with open(path, encoding = 'utf-8') as f:
    data = json.load(f)

@print_result
def f1(data):
    jobNames = [items['job-name'] for items in data]
    unique = Unique(jobNames)
    return sorted(unique)
    


@print_result
def f2(data):
    return list(filter(lambda items: items.startswith('программист'), data))


@print_result
def f3(data):
    return list(map(lambda items: items + ' с опытом Python', data))
    

@print_result
def f4(data):
    salaries = [random.randint(100000, 200000) for _ in data]
    result = [f"{spec}, зарплата {salary} руб." for spec, salary in zip(data, salaries)]
    return result

def main():
    with cm_timer_1():
        f4(f3(f2(f1(data))))

main()
