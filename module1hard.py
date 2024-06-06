# список чисел
numbers = [5, 3, 3, 5, 4]
# сумма всех чисел
sum_numbers = sum(numbers)
# количество чисел
count_numbers = len(numbers)
# среднее арифметическое
Aaron = sum_numbers / count_numbers
students = {'Aaron': [5, 3, 3, 5, 4]}
students['Aaron'] = Aaron

numbers = [2, 2, 2, 3]
sum_numbers = sum(numbers)
count_numbers = len(numbers)
Bilbo = sum_numbers / count_numbers
students['Bilbo'] = Bilbo

numbers = [4, 5, 5, 2]
sum_numbers = sum(numbers)
count_numbers = len(numbers)
Johhny = sum_numbers / count_numbers
students['Johhny'] = Johhny

numbers = [4, 4, 3]
sum_numbers = sum(numbers)
count_numbers = len(numbers)
Khendrik = sum_numbers / count_numbers
students['Khendrik'] = Khendrik

numbers = [5, 5, 5, 4, 5]
sum_numbers = sum(numbers)
count_numbers = len(numbers)
Steve = sum_numbers / count_numbers
students['Steve'] = Steve
print(students)