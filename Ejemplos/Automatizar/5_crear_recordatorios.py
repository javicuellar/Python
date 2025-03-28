import schedule
import time



def recordatorio():
    print("Recuerda que debes hacer la tarea de matemáticas")


schedule.every().day.at("09:10").do(recordatorio)


while True:
    schedule.run_pending()
    time.sleep(60)
