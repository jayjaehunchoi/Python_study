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


def make_work():
    for employee in company.employees:
        employee.work()


def add_employees():
    jay = Developer()
    roy = Designer()
    koi = Analyst()
    return [jay, roy, koi]


if __name__ == '__main__':
    company = Company(add_employees())
    make_work()
