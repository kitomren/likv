
from datetime import datetime

# import locale
# locale.setlocale(locale.LC_ALL, 'nb-NO')
# note to self: får feilmelding på denne på MacBook Pro. 
# Vet ikke om det er koden som er feil eller Macen som ikke har support for norsk. 
# må sjekke dette nærmere.

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%A%d/%B/%Y, %H:%M:%S")
print("date and time:",date_time)
