
def sum_digits(pair):
    # Функция, которая складывает цифры пары
    return int(pair[0]) + int(pair[1])

if __name__ == '__main__':
    # Создаем словарь для подсчета количества счастливых билетов в каждом рулоне
    map = {i: 0 for i in range(10)}
    # Проходим по каждому билету
    for i in range(1000000):
        # Преобразуем номер билета в строку и дополняем до 6 цифр нулями слева
        ticket_number = f'{i:06d}'
        # Разделяем билет на три части по 2 цифры
        part1 = ticket_number[0:2]
        part2 = ticket_number[2:4]
        part3 = ticket_number[4:6]
        # Проверяем, что все части билета различны
        if part1 == part2 == part3:
            continue
        # Проверяем, что сумма цифр первой и второй части равна сумме цифр третьей части
        if sum_digits(part1) == sum_digits(part2) == sum_digits(part3):
            # Если билет счастливый, увеличиваем соответствующее значение в словаре на 1
            map[int(ticket_number[0])] += 1
    # Выводим результаты
    for k, v in map.items():
        print(f"рулон {k + 1} имеет: {v} счастливых билетов")