from datetime import datetime, timedelta
import pytz
from config import *

# Loan


# retourne l'heure suisse sous la form d'un nombre "float"
def S_time():
    suisse_timezone = pytz.timezone("Europe/Zurich")
    return datetime.now(suisse_timezone).timestamp()
    # 1711401372.501738


# retourne le nombre "float" d'une heure donnée
def to_stamp(date: list):
    dt_object = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    timestamp = dt_object.timestamp()
    return timestamp


# permet de calculer le nombre de pixels que le programme doit changer par seconde
# retourne un nombre int et un float
def speed(tt, etape):
    time = to_stamp(Config.end) - tt
    rate = 0
    fps = 1
    while rate < 1:
        rate = (Config.SCREEN_HEIGHT * Config.SCREEN_WIDTH - etape) / (time / fps)
        if rate < 1:
            fps += 1
    print(rate)
    decimal = rate - int(rate)
    rate = int(rate)
    return rate, decimal, fps
