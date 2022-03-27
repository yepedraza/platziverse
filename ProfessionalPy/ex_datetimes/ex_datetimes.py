from datetime import datetime
import pytz

my_datetime = datetime.now()
print(my_datetime)

utc_datetime = datetime.utcnow()
print(utc_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'LATAM format: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'USA format: {my_str}')

my_str = my_datetime.strftime('This is the year %Y')
print(f'What year is?: {my_str}')

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))


mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("México: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))


madrid_timezone = pytz.timezone("Europe/Madrid")
madrid_date = datetime.now(madrid_timezone)
print("Madrid: ", madrid_date.strftime("%d/%m/%Y, %H:%M:%S"))