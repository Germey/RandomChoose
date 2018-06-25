import random
import math

names = ['A', 'B', 'C', 'D', 'E']
weights = [100, 200, 30, 260, 2]
sum = sum(weights)
weights = list(map(lambda x: x / sum, weights))
number = 2

print('Names:', names)
print('Weights:', weights)
print('Choose %d from list' % number)

result = []


def choose(names, weights, number):
    for i in range(len(names)):
        k = math.pow(random.random(), 1 / weights[i])
        print(k)
        if len(result) < number:
            result.append((names[i], k))
        else:
            print(result)
            min_element = min(result, key=lambda x: x[1])
            print('min', min_element)
            if k > min_element[1]:
                result.remove(min_element)
                result.append((names[i], k))
    return list(map(lambda x: x[0], result))


if __name__ == '__main__':
    result = choose(names, weights, number)
    print(result)
    # print(random.random())
