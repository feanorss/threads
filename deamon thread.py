import threading
import time

def backround_task():
    while True:
    # for i in range(3):
        print("deamon thread is running...")
        time.sleep(1)

daemon_thread = threading.Thread(target=backround_task, args=(), daemon=True)
daemon_thread.start()

print("Zacni program")
time.sleep(11)
print("Ukonci program")