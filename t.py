from datetime import datetime, timedelta
import time
import pytz


#retourne l'heure suisse sous la form d'un nombre float
def S_time():
    suisse_timezone = pytz.timezone('Europe/Zurich')
    return datetime.now(suisse_timezone).timestamp()
    #1711401372.501738
#retourne le nombre float d'une heure donnée
def to_stamp(date: list):
    return datetime(date[0],date[1],date[2],date[3],date[4]).timestamp()

def speed(nb_pixels: int, start_time: float, end_time : float):
    time = end_time - start_time
    rate = 0
    fps = 1
    while rate < 1:
        rate = nb_pixels/(time/fps)
        if rate < 1:
            fps += 1
    print(rate)
    decimal = rate - int(rate)
    rate = int(rate)
    return rate, decimal , fps

def add_pixel(notfull : float, decimal: float):
    if (notfull + decimal) >= 1:
        return 1
    return 0
