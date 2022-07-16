from collections import Counter

# функция для получения множителей числа
def get_factors(num):
	i = 2
	factors = [1]
	while i*i <= num:
		while num % i == 0:
			factors.append(i)
			num = num / i
		i += 1
	if num > 1:
		factors.append(int(num))
	return factors

def get_friend(x):
	# Получим словарь конфет и их количества 
	candies_list = Counter(x)

	# Извлечем количество каждой конфеты
	nums_candies = []
	for i in candies_list:
		nums_candies.append(candies_list[i])

	# Создадим список множителей для каждой конфеты
	factors = []
	for i in nums_candies:
		factors.append(get_factors(i))

	# Найдем одинаковые множители
	for i, _ in enumerate(factors):
		try:
			factors[i + 1] = list((Counter(factors[i]) & Counter(factors[i + 1])).elements())
			i += 1
		except IndexError:
			pass

	result = max(factors[-1:][0])
	
	return result # вывод результата работы вашей функции

# candys = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']
# candys = ['a', 'b', 'c', 'a', 'b', 'c', 'c', 'c']

print(get_friend(candies))