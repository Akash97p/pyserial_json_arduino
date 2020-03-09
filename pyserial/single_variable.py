import serial
ser =serial.Serial('/dev/serial0',38400) 
c1 = 22

string1 = '{"c1":'+str(c1)+'}#'
ser.write(string1.encode())
ser.close()
