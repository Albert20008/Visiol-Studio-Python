from random import randint
from .Commission import Commission
from typing import Union


class Head:
	"""Класс(руководитель), который генерирует и возращает 10 экземпляры класса Commission"""
	def __init__(self):
		"""Генерируется 10 заказов"""
		self.__commissions = []

		for i in range(10):
			time = randint(1, 5)
			commission = Commission(time)
			self.__commissions.append(commission)


	def StartOrder(self) -> Union[Commission, bool]:
		"""
		Метод, который возращает первый по списку заказ, если он есть,
		Иначе возращает False

		:return: обьект класса Commission или False

		"""
		if self.__commissions:
			return [self.__commissions.pop(0)]
		return False
