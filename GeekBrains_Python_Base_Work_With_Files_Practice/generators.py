from random import randint
from faker import Faker


def ex2_gen(filename, lines = 10):
    Faker.seed(0)
    fake = Faker()
    with open(filename, 'w') as f:
        for i in range(0, lines):
            print(f'{fake.text()}', file=f)


def ex3_gen(filename, size=10, salary_base=20000):
    Faker.seed(0)
    fake = Faker()
    with open(filename, 'w') as f:
        for i in range(0, size):
            print(f'{fake.last_name()} {randint(salary_base / 2, salary_base * 1.5)}', file=f)


