import serial

arduino = serial.Serial('/dev/ttyUSB0', 9600)

def processUltrasonicRead() -> float:
    data = arduino.readline().decode('utf-8').strip()
    print(f"Distancia: {data} cm")
    return float(data)

