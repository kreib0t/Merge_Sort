#! /usr/bin/env python3

import argparse

def init_parser():
	parser = argparse.ArgumentParser()

	## Выбор сортировки
	group2 = parser.add_mutually_exclusive_group()
	group2.add_argument('-a', '--ascending', default = False, action = 'store_true', help = 'сортировка по возрастанию')
	group2.add_argument('-d', '--descending', default = False, action = 'store_true', help = 'сортировка по убываниюнию')

	# Выбор данных для сортировки
	group1 = parser.add_mutually_exclusive_group(required=True)
	group1.add_argument('-s', '--string', default = False, action = 'store_true', help = 'для строк')
	group1.add_argument('-i', '--integer', default = False, action = 'store_true', help = 'для целых чисел')

	# Файлы
	parser.add_argument('output', type = argparse.FileType('w'), nargs = 1)
	parser.add_argument('input', type = argparse.FileType('r'), nargs = '+')

	return parser

# Слияние
def merge(left, right):
	result = []
	i = 0
	j = 0
	while i < len (left) and j < len (right):
		if args.ascending:
			if left[i] <= right [j]:
				result.append(left[i])
				i+=1
			else:
				result.append(right[j])
				j+=1
		else:
			if left[i] >= right [j]:
				result.append(left[i])
				i+=1
			else:
				result.append(right[j])
				j+=1

# Добавление оставшихся элементов
	result += left[i:]
	result += right[j:]
	return result


# Разделение 
def mergesort(lst):
	if len(lst) <= 1:
		return lst
	middle = int(len(lst) / 2)
	left = mergesort(lst[:middle])
	right = mergesort(lst[middle:])
	return merge(left, right)

if __name__ == '__main__':
	
	args = init_parser().parse_args()

	# Если не выбран ни один режим, то режим по умолчанию сортировка по возрастанию
	if not args.ascending and not args.descending:
		args.ascending = True

	alist = []

	for infile in args.input:
		for line in infile:
			if args.integer:
				alist.append(int(line))
			else:
				line = line.rstrip('\n') # Удаляем символ перехода на след строку
				alist.append(line)
		infile.close()

	alist = (mergesort(alist))

	for outfile in args.output:
		for item in alist:
			if args.integer:
				outfile.write('%s\n' % item)
			else:
				outfile.write('%s\n' % item)
		outfile.close()