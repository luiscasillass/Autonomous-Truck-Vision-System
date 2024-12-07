from detectores import detect_red, detect_stop_sign
from motores import stop_car, forward
from sensores import processUltrasonicRead
import threading
import cv2
from database import saveToDatabase, startApp

distance = -1 
stop_detected = True
lock = threading.Lock()

def vision():
    global stop_detected
    cap = cv2.VideoCapture(0)
    
    with lock:
        while True:
            ret, frame = cap.read()
            # Detectar áreas rojas
            mask, red_output = detect_red(frame)
            if not ret:
                break
            # Detectar forma octagonal
            stop_detected = detect_stop_sign(mask, frame)

def main():
    global distance
    while True:
        try:
            distance = processUltrasonicRead()
            saveToDatabase(distance)
		    # Detener el carro si se detecta una señal de STOP
            if distance < 30 or stop_detected:
                print("Señal de STOP detectada. Deteniendo...")    
                stop_car()
            else:
                print("Moviendo hacia adelante")
                forward()
			    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            stop_car()
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
	vision_thread = threading.Thread(target=vision, daemon= True)
	sql_thread = threading.Thread(target= startApp, daemon= True)
	vision_thread.start()
	sql_thread.start()
	main()
