def ft_count_harvest_recursive():
    days = input("Days until harvest: ")
    days = int(days)

    def count_down(day):
        if (day > days):
            print("Harvest time!")
            return
        print(f"Day {day}")
        count_down(day + 1)
    count_down(1)
