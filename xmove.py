import sys
import RPi.GPIO as GPIO
import time

# vertical pinout = 7
# horizontal pinout = 11

argv = 0
lateral = 0

# argument filtering : lateral
try:
  argv+=1
  if str(sys.argv[1]) == "h" or str(sys.argv[1]) == "v":
    lateral = str(sys.argv[1])
  else:
    print " invalid lateral arguments, use h for horizontal or v for vertical"
except:
 argv+=1
 print "lateral argument empty"

# argument filtering : cycleDuty to go
try:
  sys.argv[2]
  if float(sys.argv[2]) >= 0.5 and float(sys.argv[2]) <= 15:
    goto = float(sys.argv[2])
  else:
    print "parameter offset or no parameter inserted, RPi go to position 7.5"
    goto = 7.5
except:
  argv+=1
  print "pwm cycle argument empty"

if argv == 2:
  sys.exit("please insert argument to execute, h or v for lateral and 2.5 to 12.5 for changeDutyCylce")
if lateral == "h":
  pin = 11
elif lateral == "v":
  pin = 7

# execute move servo
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
print "pin configured"
p = GPIO.PWM(pin,50)
p.start(goto)
print "servo moving"
time.sleep(0.05)
p.stop()
print "program execution end"
#try:
# while True:
#p.ChangeDutyCycle(goto)
#time.sleep(1.25)
#p.ChangeDutyCycle(10.5)
#time.sleep(1.25)
#p.ChangeDutyCycle(6.5)
#time.sleep(1.25)

#except KeyboardInterrupt:
GPIO.cleanup()