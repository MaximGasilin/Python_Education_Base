from random import randint
from faker import Faker
from num2words import num2words


def ex2_gen(filename, max_lines=10):
    Faker.seed(0)
    fake = Faker()
    with open(filename, 'w') as f:
        for i in range(0, randint(1, max_lines)):
            print(f'{fake.text()}', file=f)


def ex3_gen(filename, size=10, salary_base=20000):
    Faker.seed(0)
    fake = Faker()
    with open(filename, 'w') as f:
        for i in range(0, size):
            print(f'{fake.last_name()} {randint(salary_base * 0.5, salary_base * 1.5)}', file=f)


def ex4_gen(filename, count=20):
    with open(filename, 'w') as f:
        for digit in range(0, count):
            print(f'{num2words(digit)}-{digit}', file=f)


LIST_OF_SUBJECTS = ('Математика', 'Русский язык', 'Литература', 'Физика', 'Химия', 'Биология', 'Иностранный язык',
                    'Труд', 'Физкультура', 'География', 'Черчение', 'Астрономия', 'ОБЖ', 'Информатика')


def ex6_gen(filename):
    with open(filename, 'w', encoding='utf-8') as file_obj:
        for el in LIST_OF_SUBJECTS:
            plan_le = randint(0, 101)
            plan_pr = randint(0, 21)
            plan_lb = randint(0, 11)

            print(f'{el}: {f"{plan_le}(л) " if plan_le > 0 else "-"}'
                  f'{f"{plan_pr}(пр) " if plan_pr > 0 else "-"}'
                  f'{f"{plan_lb}(лаб)" if plan_lb > 0 else "-"}', file=file_obj)