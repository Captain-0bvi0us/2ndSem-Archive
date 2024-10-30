import sys

def getCoefficient(index, text):
    try:
        coefStr=sys.argv[index]
    except:
        print(text)
        coefStr=input()
        for i in coefStr:
            if i.isdigit() is not True and i!="-":
                print("Только цифры")
                print(text)
                coefStr=input()
                if i.isdigit() is True or i=="-": 
                    break;    
    coefs = float(coefStr)
    return coefs

def getRoots(a, b, c):
    result = []
    discr=pow(b,2)-4*a*c
    if discr<0:
        pass
    elif discr==0.0:
        root = -b/(2.0*a)
        result.append(root)
        if(root>0):
            rootAdd=pow(root,(1/2))
            result.clear()
            result.append(rootAdd)
            result.append(-rootAdd)
    else:
        sqrtDiscr=pow(discr,(1/2))
        root1 = (-b + sqrtDiscr) / (2.0*a)
        root2 = (-b - sqrtDiscr) / (2.0*a)
        result.append(root1)
        result.append(root2) 
        for item in result[::]:
            if item>0:
                item = pow(item,(1/2))
                result.append(item)
                result.append(-item)
                result.pop(0)             
    return result
        
def main():
    a=getCoefficient(1,"Введите коэффициент А:")
    b=getCoefficient(2,"Введите коэффициент B:")
    c=getCoefficient(3,"Введите коэффициент C:")

    roots=getRoots(a,b,c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} | {} | {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} | {} | {} | {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()


    
