# Метод оценки простоты числа методом перебора всех целых (как вариант: простых) чисел от 2 до квадратного корня из факторизуемого числа n
# и в вычислении остатка от деления n на каждое из этих чисел. Если остаток от деления на некоторое число i равен 0, то i является делителем n.
# В этом случае либо n объявляется составным, и алгоритм заканчивает работу
def prime_check(n):
    p = 2
    check = False
    if n<=3:
        check = True
    else:
        while p*p<=n:
            if n%p!=0:
                p+=1
            else:
                break
                check = False
        else:
            check = True
    return check
# print(prime_check(1000))

# вывод списк постых чисел в интервале от 1 до n
def prime_list(n):
    prime_list = []
    for i in range(2,n+1):
        if prime_check(i) == True:
            prime_list.append(i)
    return prime_list
# print(prime_list(47))
# Вывести весь список простых делителей числа (каноническое разложение числа)
def divisor_master(n):
    divisor_list=[]
    p_l = prime_list(n)
    i = 0
    n1 = n
    if prime_check(n) == True:
        divisor_list.append(n)
    else:
        while n!=1:
            if n%p_l[i] == 0:
                divisor_list.append(p_l[i])
                n = n/p_l[i]
            else:
                i+=1
    return divisor_list
if __name__ == '__main__':
    print('Вывести весь список простых делителей числа (каноническое разложение числа')
    print(divisor_master(10))

# вывести самый большой простой делитель числа
def divisor_max(n):
    d_m = divisor_master(n)
    d_m.sort(reverse=True)
    max = d_m[0]
    return max
if __name__ == '__main__':
    print('самый большой простой делитель числа')
    print(divisor_max(10))

# вывести все делители числа.
def divisor_list_full(n):
    divisor_list=[]
    for i in range(1,int(n//2)+1):
        if n%i == 0:
            divisor_list.append(i)
            i+=1
        else:
            i+=1
    # divisor_list.append(n) # Эта строка добавляет в список делителей само число.
    return divisor_list
if __name__ == '__main__':
    print('все делители числа')
    print(divisor_list_full((12)))

# вывод максимального делителя числа
def divisor_full_max(n):
    d_m = divisor_list_full(n)
    d_m.sort(reverse=True)
    max = d_m[0]
    return max
if __name__ == '__main__':
    print('вывод максимального делителя числа')
    print(divisor_full_max((1000)))



