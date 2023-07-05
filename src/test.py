import json

import requests

class HeadHunter:
    def __init__(self, keyword):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "per_page": 100,
            "page": None,
            "text": keyword,
            "archived": False,
        }
        self.headers = {
             "User-Agent": "50355527"
        }
        self.vacancies = []

    def get_request(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise Exception(f"Ошибка получения вакансий! Статус: {response.status_code}")
        return response

    def get_vacancy(self):
        vacancy_list = []
        data = self.get_request().json()
        for item in data['items']:
            job_name = item['name']
            emp_name = item['employer']['name']
            experience = item['experience']['name']
            if item['salary']:
                salary_min = item['salary']["from"]
            else:
                salary_min = "Нет"
            if item['salary']:
                salary_max = item['salary']['to']
            else:
                salary_max = "Нет"

            job = {"job_name": job_name,
                    "emp_name": emp_name,
                    "experience": experience,
                    "salary_min": salary_min,
                    "salary_max": salary_max}
            vacancy_list.append(job)

        self.write_data_to_file(vacancy_list)
        return vacancy_list



    def write_data_to_file(self, jobs):
        with open("../src/hh_vacancy.json", "w") as file:
            json.dump(jobs, file, sort_keys=False, indent=4, ensure_ascii=False)



h = HeadHunter("python")
print(h.get_vacancy())