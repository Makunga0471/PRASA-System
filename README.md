# PRASA Smart Passenger System

## Overview
This project simulates a PRASA railway system including booking, scheduling, payment, and monitoring functionalities.

## Language Used
Python (chosen for simplicity and compatibility with VS Code)

## Features
- User Login System
- Train Schedule (departure, arrival, platform, frequency)
- Train Search Module
- Booking System
- Payment Simulation
- Notification System (delays)
- GUI Interface (Tkinter)

## Creational Design Patterns
- Simple Factory → Sensor creation
- Factory Method → Alert types
- Abstract Factory → Train types
- Builder → Train construction
- Prototype → Object cloning
- Singleton → Database connection

## System Modules
- Search Module
- Booking Module
- Tracking Module
- Notification System
- User Profile Module
- Admin Dashboard (future)

## How to Run
1. Open project in VS Code
2. Run CLI version:
   python main.py
3. Run GUI version:
   python gui_app.py

## Testing
Run:
pytest