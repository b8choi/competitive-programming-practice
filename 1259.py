while True:
    n = input()
    if n == '0':
        break
    else:
        n_ori = n[:]
        n_rev = list(n)
        n_rev.reverse()
        n_rev = ''.join(n_rev)
        if n_ori == n_rev:
            print('yes')
        else:
            print('no')
