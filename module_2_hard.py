def password(n):
    pass_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_

print('Введите число: ')
print(password(int(input())))