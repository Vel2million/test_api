x = ["a", "a", "b", "c", "c", "c", "d", "e", "e"]
b = ["a", "b"]


def check_duplicates(x):
    result = []
    for i in x:
        if not i in x:
            result.append(i)
        else:
            return True
    return False

print(check_duplicates(b))


def count_people(person_age):
    # group_a >= 20, group_b < 20
    group_a = []
    group_b = []
    for age in person_age:
        age = int(age)
        if age >= 20:
            group_a.append(age)
        else:
            group_b.append(age)
    
    return len(group_a) if len(group_a) <2 else group_b


class Person:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

person_1 = Person('John', 'Eod', 30, 'Male')
person_2 = Person('Henry', 'Doe', 28, 'Male')
person_3 = Person('Marry', 'Ode', 17, 'Female')
person_4 = Person('Keith', 'Doe', 50, 'Male')

person_lst = [person_1, person_2, person_3, person_4]

def find_familily_names(person_lst):
    fam_lst = []
    for p in person_lst:
        if not p.lastname in fam_lst:
            fam_lst.append(p.lastname)
    return fam_lst



def find_familily_names_complex(person_lst):
    fam_lst = []
    cnt = 0
    for p in person_lst:
        cnt += 1
        if cnt == 3:
            p.lastname = 'rose'
        if not p.lastname in fam_lst:
            fam_lst.append(p.lastname)
    return fam_lst

def calculate_saving_money(monthly_salary, monthly_expense, projection_year, desired_saving_amount):
    calculation = ((monthly_salary - monthly_expense) * 12) * projection_year
    if calculation > desired_saving_amount:
        return 'saving projection in the positive'
    else:
        return calculation