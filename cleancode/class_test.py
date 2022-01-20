import abc
from typing import List


# OCP
# abstract class
class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def work(self):
        ...


class Developer(Employee):
    def work(self):
        print("do coding")


class Designer(Employee):
    def work(self):
        print("do design")


class Analyst(Employee):
    def work(self):
        print("do analyzing")


class Company:
    def __init__(self, employees: List[Employee]):
        self.employees = employees


if __name__ == '__main__':
    jay = Developer()
    roy = Designer()
    koi = Analyst()

    employees = [jay, roy, koi]
    company = Company(employees)

    for employee in company.employees:
        employee.work()
