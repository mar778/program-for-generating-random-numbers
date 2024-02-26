import random

start_range = int(input("Введите начало диапазона: "))
end_range = int(input("Введите конец диапазона: "))

random_number = random.randint(start_range, end_range)
print(f"Случайное число в диапазоне от {start_range} до {end_range}: {random_number}")
