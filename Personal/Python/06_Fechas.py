from datetime import datetime

now = datetime.now()
print(f"La fecha actual es {now.year}/{now.month}/{now.day} y la hora actual es {now.hour}:{now.minute}:{now.second}")

timestamp = now.timestamp()
print(timestamp)
                                
#El formato siempre sera Año Mes Dia Hora Minuto y Segundo 
year_2023 = datetime(2023, 1, 1)
print(year_2023)

from datetime import time

current_time = time(21,6, 30)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time)

from datetime import date 

current_date = date(2023, 3, 12)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date)

current_date = date.today()
print(current_date)

#Resta de fechas
diff = now - year_2023
print(diff)
