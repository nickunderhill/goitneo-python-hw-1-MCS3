from datetime import datetime
from util.birthday_generator import generate_fake_birthdays


def get_birthdays_per_week(users_list):
    congrats_per_day = {"Monday": [], "Tuesday": [],
                        "Wednesday": [], "Thursday": [], "Friday": [], }

    today = datetime.today().date()

    for user in users_list:
        name = user["name"]

        birthday = user["birthday"]
        birthday_this_year = get_birthday_this_year(today, birthday)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            if birthday_this_year.weekday() == 1:
                congrats_per_day["Tuesday"].append(name)
            elif birthday_this_year.weekday() == 2:
                congrats_per_day["Wednesday"].append(name)
            elif birthday_this_year.weekday() == 3:
                congrats_per_day["Thursday"].append(name)
            elif birthday_this_year.weekday() == 4:
                congrats_per_day["Friday"].append(name)
            else:
                congrats_per_day["Monday"].append(name)

    print_week_birthdays(congrats_per_day)


def get_birthday_this_year(today, birthday):
    try:
        birthday_this_year = birthday.replace(year=today.year)
    # handle leap year exception
    except ValueError:
        birthday_this_year = birthday.replace(day=birthday.day - 1)
        birthday_this_year = birthday_this_year.replace(year=today.year)

    if birthday_this_year < today:
        birthday_this_year = birthday.replace(year=today.year + 1)
    return birthday_this_year


def print_week_birthdays(congrats_per_day):
    for weekday, names in congrats_per_day.items():
        print(f"{weekday}: {', '.join(names)}")


def main():
    users_birthdays = generate_fake_birthdays(1000)
    get_birthdays_per_week(users_birthdays)


if __name__ == '__main__':
    main()
