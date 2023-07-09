
from src.utils import hh_search, sj_search


def main():

    print("Привет! Ты готов к поиску работы?")
    keyword = input("Введи ключевое слово ")
    count = int(input("Сколько вакансий ты хочешь посмотреть? "))
    choice = int(input("Введите 1, если хотите искать работу на Head Hunter \nВведите 2, если хотите искать работу на Super Job "
                     "\nВаш выбор:"))
    if choice == 1:
        print(hh_search(keyword, count))
    elif choice == 2:
        print(sj_search(keyword, count))
    else:
        print("Вы ввели неправильное значение")





if __name__ == '__main__':
    main()