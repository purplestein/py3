name = str(input('Введите имя:'))
second_name = str(input('Введите фамилию:'))
year_of_birth = str(input('Введите год рождения:'))
city = str(input('Введите город проживания:'))
email = str(input('Введите электронную почту:'))
phone_number = str(input('Введите номер телефона:'))
def my_data(name, second_name, year_of_birth, city, email, phone_number):
    return name, second_name, year_of_birth, city, email, phone_number

print(my_data(name, second_name, year_of_birth, city, email, phone_number))

