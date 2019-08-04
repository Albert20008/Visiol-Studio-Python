from .Commission import Commission
from random import randint
from typing import Union



class Employee:
	"""Класс для разработки заказов(сотрудник)"""
	def __init__(self):
		"""
		self.__status - поле, в котором хранится заказ, если его там нет, оно False(Commission или False)
		self.__poins - поле, в котором хранятся баллы сотрудника(int)
		self.__efficiency - поле, в котором хранится эффективность сотрудника(int)
		self.__fail - поле, которое показывает, сделал ли сотрудник заказ в срок(bool)
		"""
		self.__status = False
		self.__order = None
		self.__poins = 0
		self.__efficiency = randint(70, 95)
		self.__time = 0
		self.__fail = False


	def Salary(self):
		"""Начисляет балл сотруднику за успешно сделанный заказ"""
		if not self.__fail:
			self.__poins += 1

		else:
			self.__poins -= 1


	def Accept(self, commission:Commission):
		"""
		Принимает заказ

		:param: commission - экземпляр класса Commission

		"""
		self.__status = True
		self.__fail = False
		self.__order = commission
		self.__time = commission.getTime()


	def IsTheFail(self) -> bool:
		"""
		Анализирует заказ на ошибки
		Если заказ без ошибок, то возращает True
		Иначе возращает False

		:return: булевые значения

		"""
		fail = randint(1, 100)

		if fail > self.__efficiency:
			self.__fail = True
			self.__order = False
			return True

		return False


	def Performance(self) -> bool:
		"""
		Разрабатывает заказ, когда он будет сделан, возращает его
		Иначе возращает False

		:return: экземпляр класса Commission или False

		"""
		self.__time -= 1 

		if self.__time <= 0 and not self.IsTheFail():
			self.__status = False
			return True

		return False


	def getStatus(self) -> Union[bool, Commission]:
		"""
		Возращает поле self.__status

		:return: False или Commission

		"""
		return self.__status


	def getPoins(self) -> int:
		"""
		Возращает очки сотрудника

		:return: целочисленное число

		"""
		return self.__poins


	def setPoins(self, poins:int):
		self.__poins = poins


	def getFail(self) -> bool:
		return self.__fail
