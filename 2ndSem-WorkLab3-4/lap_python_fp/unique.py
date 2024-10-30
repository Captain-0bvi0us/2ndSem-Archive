def gen_random(numCount, begin, end):
    import random
    result = []
    for _ in range(numCount):
        result.append(random.randint(begin, end))
    return(result)

class Unique(object):
    def __init__(self, data, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.data = data
        self.index = 0
        self.seen = set()

    def __next__(self):
        while self.index < len(self.data):
            item = self.data[self.index]
            if isinstance(item, str):
                if self.ignore_case == False:
                    key = item
                else:
                    key = item.lower()
            else:
                key = item
            if key not in self.seen:
                self.seen.add(key)
                return item
            self.index += 1
        raise StopIteration

    def __iter__(self):
        return self

 
def main():
        data = ['a', 'b', 'c', 'a', 'b', 'd', 'A', 'B', 'C', 'D']
        dataRandom = gen_random(10, 1,10)

        unique1 = Unique(data, ignore_case=True)
        unique2 = Unique(dataRandom)  
        for item in unique1:
            print(item, end=' ')
        print('\n')
        for item in unique2:
            print(item, end=' ')
main()
