import json
from abc import ABC

import requests

from src.abstract_class import Job_Search


class SuperJob(Job_Search):
    """класс, в котором осуществляется работа с платформой Super Job"""

    def __init__(self, keyword, count):
        self.count = count
        self.url = "https://api.superjob.ru/2.0/vacancies"
        self.params = {
            "count": self.count,
            "page": None,
            "keyword": keyword,
            "archive": False}
        self.headers = {
            "X-Api-App-Id":"v3.r.137668112.790ab2086b3eb66622cb60534757bd8270a95340.f7126288b5d72863a7eecff21930451fe762d670"
        }
        self.vacancies = []

    def get_request(self):
        """делаем реквест к апи"""
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise Exception(f"Ошибка получения вакансий! Статус: {response.status_code}")
        return response

    def get_vacancy(self):
        """получаем список вакансий"""
        global salary_min
        vacancy_list = []
        data = self.get_request().json()
        for item in data['objects']:
            job_name = item['profession']
            emp_name = item['firm_name']
            description = item['candidat']
            try:
                if item['payment_from']:
                    salary_min = item['payment_from']
            except Exception:
                salary_min = None


            job = {"job_name": job_name,
                    "emp_name": emp_name,
                    "description": description,
                    "salary_min": salary_min}
            vacancy_list.append(job)

        sort_vac = sorted(vacancy_list, key=lambda x: x["salary_min"])

        self.write_data_to_file(sort_vac)
        return sort_vac



    def write_data_to_file(self, jobs):
        """записываем вакансии в файл"""
        with open("../src/sj_vacancy.json", "w", encoding="utf-8") as file:
            json.dump(jobs, file, sort_keys=False, indent=4, ensure_ascii=False)


