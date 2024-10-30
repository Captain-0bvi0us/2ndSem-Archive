def sortArray(array):
    for i in range( len(array)-1):
        for j in range( len(array)-i-1):
            if abs(array[j]) < abs(array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array

sort = lambda array: sorted(array, key=abs, reverse=True)

def main():
    from random import randint
    array = [randint(-100, 100) for _ in range(10)]
    result = sortArray(array)
    resultWithLambda = sort(array)

    print("Without Lambda: ")
    print(result)
    print("With Lambda: ")
    print(resultWithLambda)

main()