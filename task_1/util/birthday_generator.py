from faker import Faker


def generate_fake_birthdays(quantity):
    fake = Faker()

    birthday_list = [
        {
            'name': fake.name(),
            'birthday': fake.date_of_birth(minimum_age=18, maximum_age=65)
        }
        for _ in range(quantity)
    ]

    return birthday_list


if __name__ == '__main__':
    generate_fake_birthdays(100)
