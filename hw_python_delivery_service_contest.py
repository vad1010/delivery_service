# ID 103117220: Test ok.
def min_transport_platforms(robots_weight, platform_capaticity) -> int:
    # Преобразуем входящие данные из сторчного формата в числовой
    robots_weight: int = [int(i) for i in robots_weight.split()]
    # Сортируем роботов по убыванию веса
    sorted_weights: list = sorted(robots_weight, reverse = True)
    # Объявляем счетчик платформ
    count: int = 0
    
    while sorted_weights:
        count += 1
        # Перевозим на первой платформе самого тяжелого робота
        # и удалям из списка
        current_weight: list = sorted_weights.pop(0)
        # Ищем для второй платформы робота, суммарный вес которого с первым 
        # не превышает лимит
        for i in range(len(sorted_weights)):
            # Если суммарный вес двух роботов меньше или равен
            # грузоподъёмности платформы: удаляем из списка найденного робота
            if current_weight + sorted_weights[i] <= platform_capaticity:
                sorted_weights.pop(i)
                break
    return count

if __name__ == '__main__':
    robots_weight: str  = input()
    platform_capaticity: int = int(input())
    print(min_transport_platforms(robots_weight, platform_capaticity))
