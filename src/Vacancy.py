class Vacancy:
    """создает экземпляры класса вакансий"""

    all_vacancies = []

    def __init__(self, job_name, emp_name, description, salary_min):
        self.job_name = job_name
        self.emp_name = emp_name
        self.description = description
        self.salary_min = salary_min

        Vacancy.all_vacancies.append(self)

    def __gt__(self, other):
        return int(self.salary_min) > int(other.salary_min)

    def __ge__(self, other):
        return int(self.salary_min) >= int(other.salary_min)

    def __lt__(self, other):
        return int(self.salary_min) < int(other.salary_min)

    def __le__(self, other):
        return int(self.salary_min) <= int(other.salary_min)

    def __eq__(self, other):
        return int(self.salary_min) == int(other.salary_min)

    def __str__(self):
        """возвращаем описание вакансии"""

        return f"""
        Название вакансии: \"{self.job_name}\"
        Работодатель: \"{self.emp_name}\"
        Описание вакансии: \"{self.description}\"
        Заработная плата: от {self.salary_min}"""

    def sort_vac(self):
        sort_vacancy = sorted(self.all_vacancies, key=lambda x: x[self.salary_min])
        return sort_vacancy

    @classmethod
    def class_vacancy(cls, reader):
        """создает экземпляры класса"""
        for row in reader:
            cls(row['job_name'], row['emp_name'], row['description'], row['salary_min'])