# prototype_rosatom
В df_dt_gen.py находится сгенерированные данные для датасета и формирование фреймворка, с помощью pandas
существует класс Main. он принимает ряд елементов (см ниже, написаны в порядке ввода), сам по себе является огромным накопителем и словарём
id - Уникальный идендификатор для каждой работы, существует
name - Наименование работы 
func - Тип работы (в первой версии уровень доверия)
date_st - Дата начала работы, существует
n_fact - Фактическое время работы, существует, формат для записи: День (даже если более 30)
n_plan - Плановое выполнение, Срок который был заявлен при согласовывании работы, формат для записи: День (даже если более 30)
dt_b- Стоимость отклонения в днях назад. Отрицательный фектор, не всегда положительный. (Переработана формула расчёта для динамики в версии 2)
dt_a -Стоимость отклонения в днях вперед. Отрицательный фектор, но может быть положительным. (Переработана формула расчёта для динамики в версии 2)
v_plan - Запланированный объем работы (появился во второй версии)
v_fact - Фактически выполненный объем работы/Текущий объем работы
all_values - Бюджет (рассматривалось внесение динамичного эффекта и даже реализовывалось. Отказались из-за малоколичества факторов)
d1 - Графа с коэффициентом негатива (Используется в дальнейшем, на этой стадии она просто есть. Также планируется внедрение в динамике)
d2 - Графа с коэффициентом позитива (Используется в дальнейшем, на этой стадии она просто есть. Также планируется внедрение в динамике)
d3 - Графа с коэффициентом негатива (Используется в дальнейшем, на этой стадии она просто есть. Также планируется внедрение в динамике)
d4 - Графа с коэффициентом позитива (Используется в дальнейшем, на этой стадии она просто есть. Также планируется внедрение в динамике)

# Эти данные уже формируются
prognos_alarm(='green') - Один из ветвей защиты и предупреждения. Рассчитывается с помощью формулы, данные создаются на основе уже имеющихся данных (Появилось во второй версии)
rest_dt - Остаток дней по плану. Рассчитывается с помощью формулы, данные создаются на основе уже имеющихся данных (Появилось во второй версии)
process - Реальный процесс. Рассчитывается с помощью формулы, данные создаются на основе уже имеющихся данных, присваивается в динамике (Появилось во второй версии)
v_rest - Остаток от работ в процентах. Рассчитывается с помощью формулы, данные создаются на основе уже имеющихся данных, присваивается в динамике (Появилось во второй версии)
actuall_work - Статус работы. Может быть 3 значения: Завершен, Не начато, или числовое значение в днях. Рассчитывается с помощью формулы, данные создаются на основе уже имеющихся данных, присваивается в динамике (Появилось во второй версии)



в df_dt_gen.py находится прототип, который не имеет связи с фронтедом и выполняет, только числовую и распределяющую функции.
Для вывода информации, которую он генерирует достаточно прописать print(df) или скопипастить.
Также класс имеет ряд функций, но из-за сроков от них отказались. Функции планировались, как ускоритель рассчётной части класса.
