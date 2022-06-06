import random
import time


def nask(amin=20, amax=1000):
   if amin < 20 and amax > 1000:
      amin = 20
      amax = 1000
   elif amin < 20:
      amin = 20
   elif amax > 1000:
      amax = 1000
   while True:
      x = input(f"Введите значение, в диапазоне между {amin} и {amax}, числа точек для сортировки: ")
      if not x.isnumeric():
         print("Некорректный ввод. Введите целое положительное число!")
         continue
      if x.isnumeric():
         x = int(x)
         if x < amin or x > amax:
            print(f"Введите число в диапазоне между {amin} и {amax}!")
         else:
            break
      else:
         break
   return x


c = []
for i in range(nask()):
   c.append(random.randint(10000, 99999))
print("Количество чисел в списке:", len(c))




def bub_sort(c):
   start_time = time.process_time()
   n = len(c)
   for i in range(n - 1):
      for j in range(n - 2, i - 1, -1):
         if c[j + 1] < c[j]:
            c[j], c[j + 1] = c[j + 1], c[j]
   finish_time = time.process_time()
   print("Количество чисел в списке:", c)
   print('Процессорное время, затраченное на сортировку: {:3.3f}'.format(finish_time - start_time), "сек")
   # return c #По условию, функция ничего не возвращает и сортирует список на месте

bub_sort(c)


sum_10_max = 0
sum_10_min = 0
for i in range(10):
   max(c)
   min(c)
   sum_10_max += max(c)
   sum_10_min += min(c)
   c.remove(max(c))
   c.remove(min(c))
print(f"Сумма 10 минимальных чисел {sum_10_min} и сумма 10 максимальных чисел {sum_10_max} отсортированного списка.")


