class Commission:
	"""Класс(заказ)"""
	def __init__(self, time:int):
		"""
		:param: time - целочисленное число

		self.__time - поле, в котором хранится число, за которое должны сделать заказ

		"""
		self.__time = time


	def getTime(self) -> int:
		"""
		Возращает срок заказа
		
		:return: целочисленное число

		"""
		return self.__time
