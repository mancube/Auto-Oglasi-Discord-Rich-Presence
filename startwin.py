from threading import Thread
import subprocess

t1 = Thread(target=subprocess.run, args=('main.exe',))
t2 = Thread(target=subprocess.run, args=('getter.exe',))

t1.start()
t2.start()

t1.join()
t2.join()