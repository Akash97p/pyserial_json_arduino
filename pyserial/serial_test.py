import serial

ser = serial.Serial('/dev/serial0',38400)
def send_data():
	c1 = 9
	c2 = 2
	c3 = 7
	c4 = 8
	string = '{"c1":'+str(c1)+',"c2":'+str(c2)+',"c3":'+str(c3)+',"c4":'+str(c4)+'}#'
	ser.write(string.encode())
	#if ser.is_open():
	#	ser.write(string.encode())
		#ser.write(b'hii')
	#else: 
	#	ser.open()
	#	ser.write(string.encode())
	#ser.close()

send_data()
