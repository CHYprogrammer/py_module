def ft_water_reminder():
    while True:
        last_watering = input("Days since last watering: ")
        try:
            days = int(last_watering)
            break
        except ValueError:
            print("Please enter number")
    if days > 2:
        print("Water plants!")
    else:
        print("Plants are fine")
