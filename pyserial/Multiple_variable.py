import serial

ser = serial.Serial('/dev/serial0',38400) #GPIO14 = Tx , GPIO15 = Rx

#def json(var):
#	x = var.split(":")
#	s ='{"c'
#	b = '":''
#	c = '',"c'
#	d = ''}''
#	for i range(len(x)):
#		s = s+str(i)+b+

def send_json_object():
	c1 = 9
	c2 = 2
	c3 = 7
	c4 = 8
	#json_object = json(c1:c2:c3:c4)
	json_object = '{"c1":'+str(c1)+',"c2":'+str(c2)+',"c3":'+str(c3)+',"c4":'+str(c4)+'}' 
	ser.write(json_object.encode())
	# Uncomment below code if the above code is not working 
	#if (ser.is_open() == True):
	#	ser.write(json_object.encode())
		#ser.write(b'hii')
	#else: 
	#	ser.open()
	#	ser.write(json_object.encode())
	ser.close()

send_json_object()
