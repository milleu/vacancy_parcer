import json
from abc import ABC

import requests

from src.abstract_class import Job_Search


class HeadHunter(Job_Search, ABC):
    """класс, в котором осуществляется работа с платформой Head Hunter"""
    def __init__(self, keyword, count):
        self.count = count
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "per_page": self.count,
            "page": None,
            "text": keyword,
            "archived": False}
        self.headers = {
             "User-Agent": "50355527"
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
        vacancy_list = []
        data = self.get_request().json()
        for item in data['items']:
            job_name = item['name']
            emp_name = item['employer']['name']
            description = item['snippet']['requirement'] if item['snippet'] and 'requirement' in item[
                    'snippet'] else None
            try:
                if item['salary']:
                    salary_min = item['salary']["from"]
            except Exception:
                    salary_min = None


            job = {"job_name": job_name,
                    "emp_name": emp_name,
                    "description": description,
                    "salary_min": salary_min}
            vacancy_list.append(job)

        self.write_data_to_file(vacancy_list)
        return vacancy_list



    def write_data_to_file(self, jobs):
        """записываем вакансии в файл"""
        with open("../src/hh_vacancy.json", "w") as file:
            json.dump(jobs, file, sort_keys=False, indent=4, ensure_ascii=False)


