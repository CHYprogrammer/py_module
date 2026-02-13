def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_down(day):
        if (day > days):
            print("Harvest time!")
            return
        print(f"Day {day}")
        count_down(day + 1)

    count_down(1)
