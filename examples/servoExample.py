from pyduino import *
import servo

#Main saftey for windows
if __name__ == '__main__':
    
	a = Arduino()
	# if your arduino was running on a serial port other than '/dev/ttyACM0/'
	# declare: a = Arduino(serial_port='/dev/ttyXXXX')

	time.sleep(3)
	# sleep to ensure ample time for computer to make serial connection 

	pos = 0
	# initialize the digital pin as output

#Update loop
while True:
	angle = input();
	# Ask for an angle each update
	print(servo.write(angle));
	#shows the microsecond output of the angle
	a.analog_write(9,servo.write(angle))
	#writes the data to pin 9
