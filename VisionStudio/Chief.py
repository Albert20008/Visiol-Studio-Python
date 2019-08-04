from .Employee import Employee
from random import randint
from .Commission import Commission
from typing import Union


class Chief(Employee):
	"""Класс-наследник класса Employee(начальник), может поручает заказ сотруднику"""
	def __init__(self):
		super().__init__()


	def orderAcceptance(self, workings:list, commission:Commission) -> Union[list, bool]:
		"""
		Метод, который поручает заказ одному из незанятых сотрудников
		Если заказ был кому-то поручен, возращается True
		Иначе возращается False

		:param: workings - список экземпляров класса Employee
		commission - экземпляр класса Commission
		:return: list или False

		"""
		for i in range(len(workings)):
			if not workings[i].getStatus():
				workings[i].Accept(commission)
				return [i, commission]

		return False


	def SalaryChief(self, answer:bool):
		poins = self.getPoins()
		if not answer:
			poins += 1

		else:
			poins -= 1

		self.setPoins(poins)
