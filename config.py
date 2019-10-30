from serial import *

chip_baudrate = 9600
chip_channel  = "001"
transmit_mode = "FU3"
transmit_pow  = 8 # Goes form 1 to 8
serial_mode   = "8N1" # 8bit / no parity / 1 stop bit

def readline(sp,endline=''):
	t = ""
	while True:
		c = sp.read()
		if c == endline:
			return t
		t += c

def send_command(cmd):
	sp_port.write(cmd)
	resp = readline(sp_port,endline='\n').replace("\r","")
	if "OK" not in resp:
		print("[*] Chip didn't respond porperly to the "+cmd+" command. Check wiring. (Response: \""+resp+"\")")
		return False
	print("[*] Chip>Computer / "+cmd+" > "+resp)
	return True


sp_port = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1, writeTimeout=1)
if not sp_port.isOpen():
	print("[-] Serial port can not be opened")
	exit()
print("[*] Serial port succesfuly opened")


if(send_command("AT")):
	send_command("AT+B"+str(chip_baudrate))
	send_command("AT+C"+str(chip_channel))
	send_command("AT+"+str(transmit_mode))
	send_command("AT+P"+str(transmit_pow))
	send_command("AT+U"+str(serial_mode))
