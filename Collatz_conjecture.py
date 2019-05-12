def find_steps_collatz_conjecture(number):
    count = 0
    while(number>1):
        print(number, end=' ')
        if number%2 == 0:
            number = number//2
        else:
            number = number*3 + 1
        count += 1
    print(f'{1}','\n')
    return count


def find_positive_int():
    i = 2
    while(True):
        if find_steps_collatz_conjecture(i):
            i += 1
            print(f'True {i}')
        else:
            print(f'Positive number for which collatz fail: {i}')
            break
    return None


if __name__ == '__main__':
    num = int(input('Enter the number to reach to 1\n'))
    print('Steps it takes to reach to 1:',find_steps_collatz_conjecture(num))
    #find_positive_int()