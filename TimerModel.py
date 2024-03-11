import threading
import time

class TimerModel():
   """Implements a countdown timer."""

   def __init__(self, seconds):
       self.startTime = seconds
       self.currentTime = 0
       self.running = False
       self.thread = threading.Thread(target=self._thread_function) 

   def _thread_function(self):
       while self.running and self.currentTime > 0:
           time.sleep(1)
           self.currentTime -= 1
           print(self.currentTime)

   def start(self):
       self.running = True
       self.currentTime = self.startTime
       self.thread.start()

   def stop(self):
       self.running = False
       self.thread.join()

if __name__ == '__main__':
    timer = TimerModel(10)
    timer.start()
    print("Liftoff!")
    timer.stop()
