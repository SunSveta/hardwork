import csv
import pandas as pd



def like_a_cache(func):  # декоратор для сохранения кеша
  cache = {}
  def wrapper(**kwargs):
    if tuple(kwargs) in cache:
      return cache[tuple(kwargs)]
    else:
      cache[tuple(kwargs)] = func(**kwargs)
      return cache[tuple(kwargs)]

  return wrapper

@like_a_cache
def select_sorted(sort_columns=['high'], limit=5, group_by_name=False, order='desc', filename='dump.csv'):
  df = pd.read_csv('all_stocks_5yr.csv')
  if order == 'desc':
    df_sorted = df.sort_values(by=sort_columns, ignore_index=True, ascending=False)
    df_sorted.head(limit).to_csv(r'C:\Users\Светлана\PycharmProjects\pythonProject8\dump.csv', index=False, sep='|')
  else:
    df_sorted = df.sort_values(by=sort_columns, ignore_index=True)
    df_sorted.head(limit).to_csv(r'C:\Users\Светлана\PycharmProjects\pythonProject8\dump.csv', index=False, sep='|')

def get_sorted():
    price = input(f"""Выберете параметры сортировки. Сортировать по цене:
    открытия - 1
    закрытия - 2
    максимум - 3
    минимум - 4
    объем - 5
        """)

    dict = {1:'open', 2:'close', 3:'high', 4:'low', 5:'volume'}

    order = input(f"""Выберете порядок сортировки:
    по убыванию - 1
    по возрастанию - 2
        """)

    number = input(f"Ограничение выборки:  ")
    name = input("Введите название файла для сохранение результатов:  ")

    column = ['high']
    direction = 'desc'
    num = 10
    f_name = 'dump.csv'

    if price != '':
      column = [dict[int(price)]]

    if order == '' or order == '1':
      direction = 'desc'
    else:
      direction = str('asc')

    if number == '':
      num = 10
    else:
      num = int(number)

    if name == '':
      f_name = 'dump.csv'
    else:
      f_name = name

    select_sorted(sort_columns=column, limit=num, group_by_name=False, order='direction', filename='f_name')
    #результат все равно записывается в файл dump.csv, не разобралась еще как это исправить
    return select_sorted

@like_a_cache
def get_by_date(date="2017-08-08", name="PCLN", filename='dump2.csv'):
    with open("all_stocks_5yr.csv") as r_file:
        reader = csv.DictReader(r_file)
        for row in reader:
            for i in row:
                if row['date'] == date:
                    if row['Name'] == name:
                        with open(filename, 'a',newline="") as w_file:
                            writer = csv.DictWriter(w_file, fieldnames=row.keys())
                            writer.writerow(row)

def get_banch():
    day = input("Введите дату в формате yyyy-mm-dd:   ")
    t_name = input("Тикер: ")
    name = input("Введите название файла для сохранение результатов:  ")

    with open("all_stocks_5yr.csv") as r_file:
        reader = csv.DictReader(r_file)
        if day == '':
            for row in reader:
                for i in row:
                    if row['Name'] == t_name:
                        with open(name, 'a', newline="") as w_file:
                            writer = csv.DictWriter(w_file, fieldnames=row.keys())
                            writer.writerow(row)
        if t_name == '':
            for row in reader:
                for i in row:
                    if row['date'] == day:
                        with open(name, 'a', newline="") as w_file:
                            writer = csv.DictWriter(w_file, fieldnames=row.keys())
                            writer.writerow(row)

        if name == '':
            ticker_name = t_name
            period = day
            fi_name = "dump2.csv"
            get_by_date(date=period, name=ticker_name, filename=fi_name)
            return get_by_date

        else:
            ticker_name = t_name
            period = day
            fi_name = name
        get_by_date(date=period, name=ticker_name, filename=fi_name)
        return get_by_date

get_banch()

