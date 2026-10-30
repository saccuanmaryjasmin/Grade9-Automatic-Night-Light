
# Grade9-Automatic-Night-Light

## Project Description
The Automatic Night Light is an Arduino-based project that automatically controls an LED using a photoresistor (LDR) sensor. It detects the surrounding light intensity and turns the LED ON or OFF depending on the detected brightness.

## Objectives
- To create an automatic lighting system using an LDR sensor.
- To control an LED based on the surrounding light intensity.
- To demonstrate the use of Arduino and a Streamlit dashboard.

## Input
The LDR sensor detects the surrounding light intensity and sends analog readings to the Arduino through pin A0.

## Process
The Arduino reads the analog sensor value and compares it with the threshold value of 600.
- If the reading is greater than 600, the LED turns ON.
- If the reading is 600 or below, the LED turns OFF.

## Output
The LED automatically turns ON in dark conditions and turns OFF in bright conditions.

## Components Used
- Arduino Uno
- Photoresistor (LDR) Sensor Module
- LED
- 220-ohm Resistor
- Jumper Wires

## Project Files
- `sketch.ino` – Modified Arduino program
- `app.py` – Modified Streamlit dashboard
- `requirements.txt` – Required Python libraries
- `README.md` – Project description

## Wokwi Simulation
https://wokwi.com/projects/479263057093989377

## Streamlit Dashboard
The Streamlit dashboard allows users to simulate analog sensor readings and observe the corresponding LED status.
