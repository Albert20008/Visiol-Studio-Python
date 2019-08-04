from VisionStudio.Head import Head
from VisionStudio.Department import Department
from time import sleep


head = Head()

design = Department()
frontend = Department()
backend = Department()

day = 0
ready_orders = []

run = True
while run:
	day += 1

	print(f'{day} день')

	projects = head.StartOrder()
	if projects:
		design.takeAnOrder(projects)
		print('Руководитель дал заказ Дизайну')

	else:
		print('Заказов у Руководителя нет')

	if design.chargeAnOrder():
		print('Распределение заказов в Дизайне')

	else:
		print('Заказов для Распределение в Дизайне нет')


	print('Начало работы в Дизайне')
	design.workingDay()


	projects = design.giveOrders()
	if projects:
		print('Дизайн распределил баллы сотрудникам, которые выполнили заказы')
		frontend.takeAnOrder(design.SubmitProject())
		print('Дизайн передаёт Фронтенду заказ')

	else:
		print('Готовых заказов у Дизайна нет')


	if frontend.chargeAnOrder():
		print('Распределение заказов в Фронтенде')

	else:
		print('Заказов для Распределение в Фронтенде нет')


	print('Начало работы во Фронтенде')
	frontend.workingDay()


	projects = frontend.giveOrders()
	if projects:
		print('Фронтенд отдал баллы сотрудникам, которые выполнили заказы')
		backend.takeAnOrder(frontend.SubmitProject())
		print('Фронтенд отдал заказы Бэкенду')

	else:
		print('У Фронтенда нет готовых заказов')


	if backend.chargeAnOrder():
		print('Распределение заказов в Бэкенде')

	else:
		print('Заказов для Распределение в Бэкенде нет')


	print('Начало работы в Бэкенде')
	backend.workingDay()

	projects = backend.giveOrders()
	if projects:
		print('Бэкенд отдал баллы сотрудникам, которые выполнили заказы')
		ready_orders.extend(backend.SubmitProject())
		print('Бэкенд сдал заказ заказчику')

	else:
		print('У Бэкенда нет готовых заказов')

	print()

	if len(ready_orders) == 10:
		point = []

		final = [design.bestWorking(), frontend.bestWorking(), backend.bestWorking()]

		best = 0
		for i in range(1, len(final)):
			if final[best][1] < final[i][1]:
				best = i

		print('\nИ самым полезным сотрудником этой программы считается\n*барабанная дробь*\n')

		sleep(5)

		if best == 0:
			print(f'Чувак из Дизайна под номером {final[best][0] + 1}({final[best][1]} кол-во очков)')

		elif best == 1:
			print(f'Чувак из Фронтенда под номером {final[best][0] + 1}({final[best][1]} кол-во очков)')

		elif best == 2:
			print(f'Чувак из Бэкенда под номером {final[best][0] + 1}({final[best][1]} кол-во очков)')

		run = False
