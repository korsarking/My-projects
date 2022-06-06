def nfib(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1



print("Проверка через функцию 'list':", list(nfib(20)), ";")



gen_sp = [n for n in nfib(20)]
print("Проверка через генератор списка:", gen_sp, ".")



fn = nfib(20)
for i in range(20):
    print(next(fn), end=' ', )
print("- Проверка с помощью цикла 'for';")



gen_mnoj = {n for n in nfib(20)}
print("Проверка через генератор множества:", gen_mnoj,".")
