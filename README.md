Autonomous-Truck-Vision-System

An autonomous truck prototype powered by Raspberry Pi 3B+ and Arduino. It combines computer vision (via OpenCV), ultrasonic sensors, and an H-bridge motor controller for real-time STOP sign detection, distance measurement, and motor control. Data is stored in a MariaDB database and displayed via an iOS app.

Table of Contents:
  Project Overview
  Features
  System Architecture
  Technologies Used
  Hardware Components
  Software Components
  Installation and Setup
  Usage
  Future Improvements
  Contributors
  
*Project Overview*
This project demonstrates a Raspberry Pi and Arduino-based autonomous truck system designed to improve safety and logistics. The truck:
- Detects STOP signs in real-time using OpenCV.
- Measures distances with an ultrasonic sensor.
- Controls motor directions through an H-bridge motor controller.
- Logs data in a MariaDB database hosted on the Raspberry Pi.
- Displays real-time sensor data on a custom-built iOS app developed in Swift.
  
*Features*
- STOP Sign Detection: Recognizes STOP signs using computer vision (OpenCV).
- Distance Measurement: Monitors distances in front of the truck using an ultrasonic sensor connected to an Arduino.
- Motor Control: Manages motor operations via an H-bridge, controlled by Arduino.
- Database Logging: Stores sensor readings and detection events in MariaDB.
- iOS App Monitoring: Displays truck status, distance, and STOP detection on an iPhone.
- Autonomous Operation: Coordinates vision and sensors for real-time decision-making.
  
*System Architecture*
Components:
- Raspberry Pi 3B+: Processes video for STOP sign detection and coordinates with the Arduino for motor control.
- Arduino: Interfaces with the ultrasonic sensor and controls motors via an H-bridge.
- Webcam: Captures video for STOP sign detection.
- H-Bridge Motor Controller: Manages motor voltage direction (forward/reverse) based on commands from the Arduino.
- Ultrasonic Sensor: Measures distance to obstacles.
- Flask Server: Handles data updates and communication with the iOS app.
- MariaDB Database: Stores sensor data and detection events.
- iOS App: Displays real-time truck data and status.
  
*Data Flow*
- Webcam → Raspberry Pi → Processes video frames for STOP signs (via OpenCV).
- Ultrasonic Sensor → Arduino → Sends distance readings to Raspberry Pi.
- H-Bridge → Controls motor voltage direction (forward/reverse) based on Raspberry Pi commands.
- Flask Server → Updates data in the MariaDB database and shares it with the iOS app.
- iOS App → Displays live data to the user.
- Technologies Used

*Hardware*
- Raspberry Pi 3B+
- Arduino (MEGA 2560 R3)
- Webcam
- Ultrasonic Sensor (HC-SR04)
- H-Bridge Motor Controller (L298N)
  
*Software*
- Languages: Python, Arduino C++, Swift
- Frameworks/Tools: Flask, OpenCV
- Database: MariaDB
- Operating System: Raspberry Pi OS
  
*Hardware Components*
- Raspberry Pi 3B+: Central processing unit for vision and communication.
- Arduino: Controls sensors and motor commands.
- Webcam: Captures live video for vision-based STOP sign detection.
- Ultrasonic Sensor: Measures distances to obstacles.
- H-Bridge Motor Controller: Controls motor voltage direction for forward/reverse movement.
- Motors: Drive the truck and respond to commands from the H-bridge.
- Power Supply: LiPo batteries to power the Raspberry Pi, Arduino, and motors.
  
*Software Components*
- Python Scripts (on Raspberry Pi):
- main.py: Manages truck logic, combining distance measurement, STOP detection, and motor control.
- detectores.py: Uses OpenCV to process webcam frames and detect STOP signs.
- sensores.py: Receives ultrasonic sensor data from the Arduino.
- database.py: Interfaces with the MariaDB database to store sensor data and events.
  
*Arduino Sketch*
Manages:
- Distance measurement with the ultrasonic sensor.
- Motor voltage direction via the H-bridge.
- Communication with the Raspberry Pi.
  
*iOS App*
- Developed in Swift.
Displays:
- Distance detected by the ultrasonic sensor.
- Truck movement status (moving/stopped).
- STOP sign detection alerts.
  
*Installation and Setup*
1. Hardware Setup:
- Connect the ultrasonic sensor to the Arduino.
- Attach the webcam to a USB port on the Raspberry Pi.
- Wire the motors to the H-bridge and connect the H-bridge to the Arduino.
Ensure the Arduino and Raspberry Pi communicate via serial connection.
2. Software Setup:
On the Raspberry Pi:
Install required libraries:
----------------------------------------------------------------------------------------------------
sudo apt update
sudo apt install python3-pip mariadb-server
pip3 install flask opencv-python mysql-connector-python
-----------------------------------------------------------------------------------------------------

*Clone the repository*
------------------------------------------------------------------------------------------------------
git clone https://github.com/<your-username>/Autonomous-Truck-Vision-System.git
cd Autonomous-Truck-Vision-System
------------------------------------------------------------------------------------------------------

*Set up the MariaDB database*
Start the database server:
-------------------------------------------------------------------------------------------------------
sudo service mysql start
Create a database and table:
sql
CREATE DATABASE truck_data;
USE truck_data;
CREATE TABLE sensor_data (id INT AUTO_INCREMENT PRIMARY KEY, distance FLOAT, stop_detected BOOLEAN);
--------------------------------------------------------------------------------------------------------

On the Arduino:
- Upload the Arduino sketch to control the ultrasonic sensor and H-bridge.
- Ensure the serial communication between Arduino and Raspberry Pi is functioning.
  
On the iPhone:
- Open the Swift project for the iOS app.
- Configure the backend URL in the app to point to the Raspberry Pi’s IP address.
- Build and run the app on the iPhone.
- Usage
- Power on the Raspberry Pi and Arduino.
  
*Start the main program on the Raspberry Pi*
-----------------------------------------------------------------------------------------------
python3 app/main.py
-----------------------------------------------------------------------------------------------

The system will:
- Detect STOP signs in real-time using OpenCV.
- Measure distance using the ultrasonic sensor via Arduino.
- Control motor directions via the H-bridge based on commands from the Raspberry Pi.
- Update the database and display real-time data on the iOS app.

*Future Improvements*
- Enhance motor control logic for smoother movement.
- Add more advanced AI vision algorithms.
- Expand iOS app functionality for detailed historical data and analytics.
- Improve the hardware setup with more efficient H-bridge and motor components.
  
*Contributors*

Project Lead: Luis Andres Casillas

Development Team: 
- Luis Andres Casillas
- Braulio Fernando Antero Díaz
- Paulina Mendez Lopez
- Bernardo Santiago Marin

iOS Development: Bernardo Santiago Marin

Database and Backend: 
- Luis Andres Casillas
- Paulina Mendez Lopez
  
Arduino Integration:
- Luis Andres Casillas
- Braulio Fernando Antero Díaz
  
H-Bridge Integration:
- Luis Andres Casillas
- Braulio Fernando Antero Díaz

  
For questions or contributions, contact kuiscasillas@gmail.com
