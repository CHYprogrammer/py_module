def ft_harvest_total():
    total = 0
    for i in range(3):
        each_day = input(f"Day {i + 1} harvest: ")
        total += int(each_day)
    print(f"Total harvest: {total}")
