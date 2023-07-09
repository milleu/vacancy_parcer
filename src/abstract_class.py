from abc import ABC, abstractmethod


class Job_Search(ABC):
    """создаем абстрактный класс"""

    @abstractmethod
    def get_request(self):
        pass

    def get_vacancy(self):
        pass

    def write_data_to_file(self, jobs):
        pass

