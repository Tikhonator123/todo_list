# todo_list.py




todo_list = [['' for _ in range(3)] for _ in range(7)]


days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
time = ['утро', 'день', 'вечер']


print('Заполняем ежедневник')
for i in range(7):
for j in range(3):
print(f"{i+1}. {days[i]} — {j+1}. {time[j]}")
task = input('Введите дело (или нажмите Enter, чтобы оставить пустым): ').strip()
todo_list[i][j] = task


print('\nТекущий список дел:')
for i in range(7):
print(f"{i+1}. {days[i]}")
for j in range(3):
print(f" {j+1}. {time[j]}: {todo_list[i][j] if todo_list[i][j] else '-'}")
print()


# Удаление: очищаем слот (ставим пустую строку)
print('Удаляем запись:')
day_idx = get_int('Введите номер дня (1-7): ', 1, 7) - 1
time_idx = get_int('Введите номер времени дня (1-3): ', 1, 3) - 1
if todo_list[day_idx][time_idx]:
todo_list[day_idx][time_idx] = ''
print('Запись удалена.')
else:
print('Этот слот уже пуст.')


# Добавление: ищем первый свободный слот в выбранном дне, если нет — предлагаем перезаписать
print('\nДобавляем запись:')
day_idx = get_int('Введите номер дня для добавления (1-7): ', 1, 7) - 1
# ищем пустой слот
try:
free_j = todo_list[day_idx].index('')
task = input('Введите дело для добавления: ').strip()
todo_list[day_idx][free_j] = task
print(f'Добавлено в слот {free_j+1} ({time[free_j]}).')
except ValueError:
print('Свободных слотов нет. Выберите слот для перезаписи:')
time_idx = get_int('Введите номер времени дня (1-3): ', 1, 3) - 1
task = input('Введите новое дело: ').strip()
todo_list[day_idx][time_idx] = task
print('Слот перезаписан.')


print('\nИтоговый список дел:')
for i in range(7):
print(f"{i+1}. {days[i]}")
for j in range(3):
print(f" {j+1}. {time[j]}: {todo_list[i][j] if todo_list[i][j] else '-'}")
print()


if __name__ == '__main__':
pass
