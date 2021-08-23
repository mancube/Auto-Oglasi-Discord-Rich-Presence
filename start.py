from threading import Thread
import subprocess

t1 = Thread(target=subprocess.run, args=(["python", "getter.py"],))
t2 = Thread(target=subprocess.run, args=(["python", "main.py"],))

t1.start()
t2.start()

t1.join()
t2.join()