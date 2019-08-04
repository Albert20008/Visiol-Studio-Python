from .Employee import Employee
from .Commission import Commission
from .Chief import Chief
from random import randint
from typing import Union



class Department:
	"""Класс(отдел), в котором хранятся сотрудники и заказы этого отдела, а также методы для заказов"""
	def __init__(self):
		"""
		:param: self.__workings - список, в котором будут хранится сотрудники, первым элементом списка будет начальник
		self.__ready_orders - список, в котором будут хранится заказы, которые надо отдать, и индексы сотрудников, которые делали эти заказы
		self.__active_orders - список заказов, разрабатывающиеся в данный момент, и индексы сотрудников, которые делают эти заказы
		self.__commissions - список заказов, которые надо распределить

		"""
		self.__workings = [Chief()]
		for i in range(randint(5, 10)):
			self.__workings.append(Employee())

		self.__active_orders = []
		self.__ready_orders = []
		self.__commissions = []


	def listFilter(self):
		def funcFilter(thing:list):
			if thing:
				return 1

			else:
				return 0

		a = filter(funcFilter, self.__commissions)
		self.__commissions = list(a)

		a = filter(funcFilter, self.__active_orders)
		self.__active_orders = list(a)

		a = filter(funcFilter, self.__ready_orders)
		self.__ready_orders = list(a)


	def takeAnOrder(self, commission:list):
		"""
		Метод, получающий заказ

		:param: commission: 
		:return: то, что возращает

		"""
		self.__commissions.extend(commission)


	def chargeAnOrder(self) -> bool:
		"""Метод, распределяющий заказы"""
		if self.__commissions:
			for i in range(len(self.__commissions)):
				data = self.__workings[0].orderAcceptance(self.__workings, self.__commissions[i])
				if data:
					self.__active_orders.append(data)
					self.__commissions[i] = 0

			self.listFilter()
			return True

		else:
			return False


	def giveOrders(self) -> bool:
		"""Метод, который начисляет баллы сотрудникам""" 
		if self.__ready_orders:
			for i in range(len(self.__ready_orders)):
				item = self.__ready_orders[i][0]
				if item != 0:
					self.__workings[item].Salary()

					fail = self.__workings[item].getFail()
					self.__workings[0].SalaryChief(fail)

				else:
					self.__workings[0].Salary()

			return True

		else:
			return False


	def SubmitProject(self):
		projects = []

		for i in range(len(self.__ready_orders)):
			projects.append(self.__ready_orders[i][1])
		
		self.__ready_orders = []

		self.listFilter()
		return projects


	def workingDay(self):
		for i in range(len(self.__active_orders)):
			if self.__workings[self.__active_orders[i][0]].Performance():
				self.__ready_orders.append(self.__active_orders[i].copy())
				self.__active_orders[i] = []

		self.listFilter()


	def getWorkings(self) -> list:
		"""
		Метод, возвращающий список сотрудников

		:return: список экземпляров класса Employee

		"""
		return self.__workings


	def bestWorking(self) -> list:
		workingsDesignPoints = []

		for i in range(len(self.__workings)):
			workingsDesignPoints.append(self.__workings[i].getPoins())


		best_working = 0
		for i in range(1, len(workingsDesignPoints)):
			if workingsDesignPoints[best_working] < workingsDesignPoints[i]:
				best_working = i

		return [best_working, workingsDesignPoints[best_working]]

