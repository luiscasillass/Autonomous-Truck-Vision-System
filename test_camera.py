import cv2
from detectores import detect_red, detect_stop_sign  # Usa tus funciones de detección

def main():
    # Inicia la cámara
    cap = cv2.VideoCapture(0)  # Asegúrate de que sea el índice correcto de tu cámara
    print("Presiona 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al acceder a la cámara.")
            break

        # Detectar áreas rojas
        mask, red_output = detect_red(frame)

        # Detectar forma octagonal en las áreas rojas
        stop_detected = detect_stop_sign(mask, frame)

        if stop_detected:
            print("¡Señal de STOP detectada!")
        else:
            print("Avanzando...")

        # Mostrar imágenes para depuración
        cv2.imshow("Frame", frame)  # Muestra el video original con la detección
        cv2.imshow("Red Mask", red_output)  # Muestra las áreas rojas detectadas

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
