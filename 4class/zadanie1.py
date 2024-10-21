sentence = "apple banana apple orange banana kiwi"
words = sentence.split()
#Split() в Python — это функция для разделения строки
#на несколько частей на основе указанного разделителя
sort = sorted(set(words))
print(sort)