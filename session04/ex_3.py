import time

secs = time.time()

def time():
  mins = secs / 60
  hours = mins / 60
  days = hours/24
  print ('The minutes:',mins,'The hours:' ,hours, 'The days:',days)

time()
print ('The seconds:', secs)
