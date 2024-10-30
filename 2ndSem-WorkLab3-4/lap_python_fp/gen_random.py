def gen_random(numCount, begin, end):
    import random
    result = []
    for _ in range(numCount):
        result.append(random.randint(begin, end))
    return(result)

def main():
    result = gen_random(10, 1, 3)
    for i in result:
        print(i, end=' ')
main()