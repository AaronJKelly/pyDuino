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
	value = value - TRIM_DURATION;
	
	return usToTicks(value);

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
