import itertools


def main():
    count = 0
    for i in itertools.product('012', repeat=5):
        if not '00' in ''.join(i):
            count += 1
    print(count)

if __name__ == '__main__':
    main()

