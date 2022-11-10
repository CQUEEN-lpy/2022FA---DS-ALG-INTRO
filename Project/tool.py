import math

def exp_mod(x,y,N):
    if y == 0:
        return 1
    tmp_y = int(math.floor(y/2))
    z = exp_mod(x, tmp_y, N)

    if y % 2 == 1:
        return x * (z ** 2) % N
    else:
        return (z ** 2) % N

if __name__ == '__main__':
    print(exp_mod(2, 6, 10))
