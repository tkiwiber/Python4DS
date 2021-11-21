students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def data_form_dict(user_dict):
    interests_value = list()
    length_value = 0

    for stud in user_dict.values():
        for interest in stud.get('interests', {}):
            interests_value.append(interest)
        length_value += len(stud.get('surname')) if stud.get('surname') is not None else 0
    return interests_value, length_value


def main():
    interests, length = data_form_dict(students)

    print('ID - возраст:')
    for student_id, student in students.items():
        print('{id} - {age}'.format(id=student_id, age=student.get('age', 0)))

    print('\nСписок интересов:', interests)
    print('Общая длина всех фамилий студентов:', length)


main()
