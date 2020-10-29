import board
import busio
import adafruit_lsm9ds1
import time

i2c = busio.I2C(board.SCL, board.SDA)
imu = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

while (1):
	ax,ay,az = imu.acceleration
	gx,gy,gz = imu.gyro
	t = imu.temperature
	
	x = f"accel: ({ax},{ay},{az})"
	print(x, end='\r', flush=True)
	time.sleep(0.2)
