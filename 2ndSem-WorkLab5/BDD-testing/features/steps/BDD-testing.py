from behave import given, when, then

def sortArray(array):
    for i in range( len(array)-1):
        for j in range( len(array)-i-1):
            if abs(array[j]) < abs(array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array



'''First test case'''
@given('I have the array')
def step_impl_start1(context):
    context.array = [4, 5, 7, 34, 3, 1, 32, 782]

@when('the array is sorting')
def step_impl_do1(context):
    context.sortedArray = sortArray(context.array)

@then('the array is sorted')
def step_impl_end1(context):
    assert context.sortedArray == [782, 34, 32, 7, 5, 4, 3, 1]



'''Second test case'''
@given('I have the array with some same numbers')
def step_impl_start2(context):
    context.array = [782, 34, 32, 34, 5, 4, 3, 52, 34, 1, 1]

@when('the array with same same numbers is sorting')
def step_impl_do2(context):
    context.sortedArray = sortArray(context.array)

@then('the array with same same numbers is sorted')
def step_impl_end2(context):
    assert context.sortedArray == [782, 52, 34, 34, 34, 32, 5, 4, 3, 1, 1]



'''Third test case'''
@given('I have the empty array')
def step_impl_start3(context):
    context.array = []

@when('the empty array is sorting')
def step_impl_do3(context):
    context.sortedArray = sortArray(context.array)

@then('the empty array is sorted')
def stap_impl_end3(context):
    assert context.array == context.sortedArray
    