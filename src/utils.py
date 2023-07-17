
from src.Vacancy import Vacancy
from src.hh_api import HeadHunter
from src.sj_api import SuperJob


def hh_search(keyword, count):

    get_job = HeadHunter(keyword, count)
    list_of_jobs = get_job.get_vacancy()
    Vacancy.all_vacancies = []
    Vacancy.class_vacancy(list_of_jobs)
    vacancies = [vacancy for vacancy in Vacancy.all_vacancies if keyword in vacancy.job_name]
    for job in vacancies:
        print(job)



def sj_search(keyword, count):
    get_job = SuperJob(keyword, count)
    list_of_jobs = get_job.get_vacancy()
    Vacancy.all_vacancies = []
    Vacancy.class_vacancy(list_of_jobs)
    vacancies = [vacancy for vacancy in Vacancy.all_vacancies if keyword in vacancy.job_name]
    for job in vacancies:
        print(job)
