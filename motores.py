import serial
import time

arduino = serial.Serial('/dev/ttyUSB0', 9600)

"""
Comandos:
    0: Detener
    1: Mover hacia adelante
"""
def send_command(command):
    arduino.write(command.encode())
    time.sleep(0.1)

def stop_car():
    send_command('0')

def forward():
    send_command('1')
