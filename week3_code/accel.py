import board
import busio
import adafruit_lsm9ds1
import time

i2c = busio.I2C(board.SCL, board.SDA)
imu = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

def movement(_ax,_ay,_az,_gx,_gy,_gz):
	acc = " "
	rot = "\n "
	if _ax < -0.8:
                acc += "forward, "
	if _ax > 0.8:
		acc += "back, "
	if _ay < -0.8:
		acc += "right, "
	if _ay > 0.8:
		acc += "left, "
	if _az > 10.6:
		acc += "up, "
	if _az < 9.0:
		acc += "down, "
	if _gx > 30:
		rot += "rroll, "
	if _gx < -30:
		rot += "lroll, "
	if _gy > 30:
		rot += "upitch, "
	if _gy < -30:
		rot += "dpitch, "
	if _gz > 30:
		rot += "lrot, "
	if _gz < -30:
		rot += "rrot, "
	return acc + rot


while (1):
	ax,ay,az = imu.acceleration
	gx,gy,gz = imu.gyro
	t = imu.temperature
	
	x = f"accel: ({ax:.3f},{ay:.3f},{az:.3f})\n gyro: ({gx:.3f},{gy:.3f},{gz:.3f})\n temp: {t:.2f}\n"
	y = movement(ax,ay,az,gx,gy,gz)
	print(x+y, end='\n', flush=True)
	time.sleep(0.2)

