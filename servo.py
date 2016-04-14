#Written by Aaron Kelly with help from the arduino library, experimental
#tested with the arduino UNO on windows 10 with a Tower Pro SG90 servo
#change values as needed.

MIN_PULSE_WIDTH = 544;
TRIM_DURATION = 5;

def write(value):
	
	if value < 544:
	
		if value < 0:
			value = 0;
		elif value > 180:
			value = 180;
		
		value = mapfunc(value, 0, 180, SERVO_MIN(), SERVO_MAX());
	
	return writeMicroseconds(value);

def writeMicroseconds(value):
	value = value;
	value = usToTicks(value);
	
	return (value/5);


def usToTicks(us):
	return ((clockCyclesPerMicrosecond()* us) / 16);

#TO-DO: CHANGE FOR OVERCLOCKING OR NON-UNO
def clockCyclesPerMicrosecond():
	return 16;

def mapfunc(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
	
def SERVO_MIN():
	return 544
	
def SERVO_MAX():
	return 2400
