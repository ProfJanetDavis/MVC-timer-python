import threading
import time
from ObserverPattern import Subject, Observer

class TimerModel(Subject):
   """Implements a countdown timer."""

   def __init__(self, seconds):
       self.startTime = seconds
       self.currentTime = 0
       self.running = False
       self.thread = threading.Thread(target=self._thread_function) 
       self.observers = []

   def _thread_function(self):
       while self.running and self.currentTime > 0:
           time.sleep(1)
           self.currentTime -= 1
           self.notify()
       self.notify()

   def start(self):
       self.running = True
       self.currentTime = self.startTime
       self.thread.start()
       self.notify()

   def stop(self):
       self.running = False
       self.thread.join()
       self.notify()
   
   def attach(self, observer):
       self.observers.append(observer)

   def detach(self, observer):
       self.observers.remove(observer)

   def notify(self):
       for o in self.observers:
           o.update(self)

if __name__ == '__main__':
    timer = TimerModel(10)
    timer.start()
    print("Liftoff!")
    timer.stop()
