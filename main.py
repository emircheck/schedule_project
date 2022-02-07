# 1. Будильник. Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, 
# с методами для включения и выключения будильника. Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. 
# Добавьте к нему метод для установки будильника, при вызове которого должен включатся будильник.

# from datetime import time 


# class Clock:
#   def curent_time(self):
#     return time.now()
# class Alarm:
#   def on(self):
#     return  'Alarm ON'
#   def off(self):
#     return 'Alarm OFF'
# class AlarmClock(Clock, Alarm):
#   def instal(self):
#     self.on()


# obj = AlarmClock()
# print(obj.time.now())

# class Clock:
#     def current_time(self):
#         from datetime import time
#         return time.now()
# class Alarm:
#   def on(self):
#     return 'ALARM BUZZING...'

#   def off(self):
#     return 'Alarm turned off'

# class AlarmClock(Clock, Alarm):
#   def alarm(self):
#     self.on()

# alarm = AlarmClock()
# print(alarm.current_time()


from dataclasses import dataclass
import schedule
import csv
import time

   

def write_csv():
    name = input('Enter your name: ')
    age = int(input('Enter your age:  '))
    with open('users.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow(
            (name, age)
        )
    answ = input('Continue? y or n:')
    if answ == 'y':
        write_csv()
    else:
        print('Stop!')

def mailing():
    with open('users.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('\n','')for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >= 18:
                print(f'Скидки сегодня! {name[0]}')

schedule.every(3).seconds.do(mailing)
while True:
    schedule.run_pending()
    time.sleep(1)

# mailing()
# write_csv()




