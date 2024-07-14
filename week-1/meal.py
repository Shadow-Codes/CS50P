def main():
    time = input("What time is it? ")

    hours = convert(time)

    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    new_time = round((hours * 60 + minutes) / 60, 2)

    return new_time


if __name__ == "__main__":
    main()
