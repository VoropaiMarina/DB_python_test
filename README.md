# DB_python_test
В файлах выполнено тестовое задание. ТЗ:
Создать приложение Python, в котором генерятся табличные данные за период с 2022-10-01 по 2022-11-01. Схема таблицы:
- автоинкрементный столбец id
- дата ts в формате YYYY-MM-DD
- рандомное число number от 0 до 1000

Данные должны заливаться в Postgres. Далее на основе данных должно считаться среднее значение AVG по дням и логироваться в stdout. 

Также:
- приложение Python и Postgres должны быть подняты в docker-compose и объединены в одну локальную сеть
- контейнер на Python должен содержать версию 3.10
- база данных Postgres в контейнере должна инициализироваться при сборке (необходимо приложить файл init.sql)
- контейнер Postgres должен иметь volume, куда бы складывались данные
- в контейнере с Python должно буть реализовано логирование в stdout
