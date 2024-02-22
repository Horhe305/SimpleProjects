import time
import sys


def counter(t):
    while t:
        mints, secs = divmod(t, 60)
        sys.stdout.write('{:02d}:{:02d}'.format(mints, secs))
        time.sleep(1)
        sys.stdout.write('\r')
        t -= 1

    print('Timer completed')


if __name__ == '__main__':
    sec = int(input('How many seconds? '))
    counter(sec)
