import pandas as pd
import datetime
import random
import time

# Формирование данных для анализа. Для прототипа делалось в ручную
#start_time = time.monotonic()
id = [random.randint(1, 5) for i in range(500000)]  # 1
n = ['Фин-техникал', 'АЭС', 'Диджитал', 'Продакшн', 'Университет', 'Энергия', 'Стройбыт', 'Финанализ', 'Механики']
name = [n[i % len(n)] for i in range(500000)]
f = ['Документация', 'Проект', 'Закупка']
func = [f[i % len(f)] for i in range(500000)]  # 3

date_st = [datetime.date(2020, random.randint(1, 12), random.randint(1, 28)) for i in range(5000)]  # 4

n_fact = [random.randint(1, 12) for i in range(500000)]  # 5
# process = [0 for i in range(5000)]  # 6
dt_b = [random.randint(30000, 2000000) for i in range(500000)]  # 6
dt_a = [random.randint(30000, 2000000) for i in range(500000)]  # 7
n_plan = [random.randint(1, 150) for i in range(500000)]  # 8
# rest_dt = [0 for i in range(5000)]  # 9
v_plan = [random.randint(100, 10000) for i in range(500000)]  # 10
v_fact = [random.randint(1, 15) for i in range(500000)]  # 11
# v_rest = [0 for i in range(5000)]  # 12
# prognos_alarm = [0 for i in range(5000)]  # 13
# cost_min = [0 for i in range(5000)]
all_values = [random.randint(3000000, 20000000) for i in range(500000)]  # 15
d1 = [random.randint(-4, -1) for i in range(500000)]  # 15
d2 = [random.randint(1, 4) for i in range(500000)]  # 16
d3 = [random.randint(-4, -1) for i in range(500000)]  # 17
d4 = [random.randint(1, 4) for i in range(500000)]  # 18

#print(f'Время для генерации: {time.monotonic() - start_time}')
class Main:
    def __init__(self, id, name, func, date_st, n_fact, n_plan, dt_b, dt_a,
                 v_plan, v_fact,
                 all_values, d1, d2, d3, d4, prognos_alarm='green'):
        self.id = id
        self.name = name  # имя
        self.func = func  # уровень доверия который виден
        self.date_st = date_st  # дата старта
        self.n_fact = n_fact  # фактическое время работ
        # self.process = "%.0f%%" % (100 * (n_fact/n_plan)) #процент
        # self.process = None  # процент
        self.dt_b = dt_b  # сдвиг влево
        self.dt_a = dt_a  # сдвиг вправо
        self.n_plan = n_plan  # плановое выполнение
        # self.min_dt = ((1 - (n_fact/n_plan)) * (n_plan-n_fact) #тут используется левый вектор, сценарий идеального
        # контракта
        self.v_plan = v_plan  # весь объём работы
        # остаток дней по плану try with None
        self.rest_dt = [1 - self.n_fact[i] / self.n_plan[i] for i in range(len(self.n_fact))]
        self.process = ["%.0f%%" % (100 * (self.n_fact[i] / self.n_plan[i])) for i in range(len(self.n_fact))]
        # self.procces = ["%.0f%%" % (100 * x/i) for x, i in n_fact, n_plan]
        self.v_fact = v_fact  # текущий фактический выполненный объем работ
        self.v_rest = [1 - (v_fact[i] / v_plan[i]) for i in range(len(v_fact))]  # остаток от объема работ в %
        self.prognos_alarm = ['red' if (self.rest_dt[i] / self.v_rest[i]) < 1 else 'green' for i in
                              range(len(self.id))]  # если < 1   то alarm = "red"] # если < 1#   то alarm = "red"
        td = datetime.date.today().day
        self.actuall_work = [
            'Завершено' if datetime.date.today() > self.date_st[i] + datetime.timedelta(days=n_plan[i]) else 'Не начато'
            if datetime.date.today() < self.date_st[i] + datetime.timedelta(days=self.n_plan[i]) else
            self.date_st[i] + datetime.timedelta(days=td) for i in range(len(self.date_st))]
        self.all_values = all_values  #
        # self.din_values = din_values + (#создание прогнозируемого события на основе 2 векторов: (dt_b - dt_a)) + ()
        # бюджет + (True or False * дни для завершения * cost_b) + ((dop_d if > 0)  * cost_a)
        self.alarm = prognos_alarm  #
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4

    # self.process = "%.0f%%" % (100 * (n_fact/n_plan)) #процент

    def process(self):
        # self.process = ["%.0f%%" % (100 * (self.n_fact[i] / self.n_plan[i])) for i in range(len(n_fact))]
        return self.process

    # self.rest_dt = [lambda x, y: 1 - x / y, (n_fact, n_plan)]  # остаток дней по плану

    def rest_dt(self):
        # self.rest_dt = [1 - n_fact[i] / n_plan[i] for i in range(len(n_fact))]
        return self.rest_dt

    # self.v_rest = [lambda x, y: 1 - x, (v_fact / v_plan)]  # остаток от объема работ в %

    def v_rest(self):
        # self.v_rest = [1 - (v_fact[i] / v_plan[i]) for i in range(len(v_fact))]  # остаток от объема работ в %
        return self.v_rest

    #  self.prognos_alarm = lambda x, y: 'red' * (x / y < 1)(rest_dt, v_rest)  # если < 1   то alarm = "red"

    def prohnos_alarm(self):
        # self.prognos_alarm = ['red' if (self.rest_dt[i] / self.v_rest[i]) < 1 else 'green' for i in
        #                      range(len(id))]  # если < 1   то alarm = "red"]
        return self.prognos_alarm

    # lambda: 'Завершен' if datetime.date.today() > date_st + datetime.timedelta(days=n_plan) else f'В процессе'

    def actuall_work(self):
        # td = datetime.date.today().day
        # self.actuall_work = [
        #  'Завершено' if datetime.date.today() > self.date_st[i] + datetime.timedelta(days=n_plan[i]) else 'Не начато'
        #     if datetime.date.today() < self.date_st[i] + datetime.timedelta(days=self.n_plan[i]) else
        #     self.date_st[i] + datetime.timedelta(days=datetime.date.today().day()) for i in range(len(self.date_st))]
        return self.actuall_work

    def picnic(self):
        d_full = {
            'id': pd.Series(self.id), 'name': pd.Series(self.name),
            'func': pd.Series(self.func),
            'date_st': pd.Series(self.date_st),
            'n_fact': pd.Series(self.n_fact),
            'process': pd.Series(self.process),
            'dt_b': pd.Series(self.dt_b),
            'dt_a': pd.Series(self.dt_a),
            'n_plan': pd.Series(self.n_plan),
            'rest_dt': pd.Series(self.rest_dt),
            'v_plan': pd.Series(self.v_plan),
            'v_fact': pd.Series(self.v_fact),
            'v_rest': pd.Series(self.v_rest),
            'prognos_alarm': pd.Series(self.prognos_alarm),
            'actuall_works': pd.Series(self.actuall_work),
            'all_values': pd.Series(self.all_values),
            'd1': pd.Series(self.d1),
            'd2': pd.Series(self.d2),
            'd3': pd.Series(self.d3),
            'd4': pd.Series(self.d4)
        }
        return d_full


a = Main(id, name, func, date_st, n_fact, n_plan, dt_b, dt_a, v_plan, v_fact, all_values, d1, d2, d3, d4)
# вызов для демонстрации бд
df = pd.DataFrame(a.picnic())
# Можно увеличить функционал и добавить new, add для вех
# связать фронтенд и бэкенд и строить в динамике
# уведомлять и задать новые поля
# функции
# запись файла по названию проекта/дате_времени и отправка для отчетности
# в данном случае задача выполняется через класс и он служит огромным хэш накопителем информации,
# также быстро обрабатывающий данные. Если использовать numpy, то работа проходит ещё быстрее
