'''
Array pair sum. Given an integer array, output all the unique parts that sum up to a specific value k
So the input pair sum ([1,3,2,2],4) would return (1,3) (2,2)
'''


def pair_sum(array, k):
    if len(array) < 2:
        print('Array is too small')

    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))

pair_sum([1,3,2,2], 4)
