def find_min_slice_sum(data, elements_in_slice):
    count = 0 
    cycle_flag = 0
    window_sum = sum(data[0:elements_in_slice])
    
    if window_sum >= platform_capaciti:
        count += 1
        for index in range(elements_in_slice, len(data)):
            window_sum += data[index] - data[index - elements_in_slice]
            if window_sum >= platform_capaciti:
                count += 1
            cycle_flag = 1
        

    if cycle_flag ==1:
        window_sum = window_sum - platform_capaciti
        if window_sum <= platform_capaciti:
            count +=1
            
    return count

if __name__ == '__main__':
    
    data  = input()
    for i in data:
        data = list(data.split())
        print(data)
    elements_in_slice = 2
    platform_capaciti = input() 
    platform_capaciti = int(platform_capaciti)
    print(find_min_slice_sum(data, elements_in_slice))
    