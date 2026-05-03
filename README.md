
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
=======
# **Smart Digital Monitoring System for Operational Efficiency at PRASA**

---

## **📌 Project Overview**

The Smart Digital Monitoring System is a proposed digital platform designed to improve the operational efficiency of railway services managed by the Passenger Rail Agency of South Africa (PRASA). The system provides real-time monitoring of train movement, railway infrastructure conditions, and operational performance across the railway network.

The system integrates real-time sensor data, operational dashboards, and automated alert systems to support railway administrators in monitoring and managing rail services effectively.

The platform enables proactive decision-making by detecting operational disruptions, equipment failures, and train delays early.

---

## **🌍 Project Domain**

**Transportation Systems and Railway Operations Management**

---

## **🎯 Objectives**

The main objectives of the system are:

* Improve operational visibility across the railway network
* Monitor train movement in real time
* Detect infrastructure faults and operational disruptions
* Provide alerts and notifications to railway administrators
* Support data-driven decision making
* Improve passenger service reliability

---

## **⚙️ Key Features**

* Real-time train tracking
* Railway infrastructure monitoring
* Operational performance dashboard
* Automated incident detection
* Maintenance alerts
* Historical data analysis

---

## **👥 System Users**

The system supports the following users:

* Railway Operations Administrators
* Control Room Operators
* Infrastructure Maintenance Teams
* System Administrators

---

## **📚 Project Documents**

### **📄 Assignment 4: System Requirements**

Contains functional requirements (**FR1–FR11**) defining system capabilities.

---

### **📄 Assignment 5: Use Case Modeling**

Includes:

* Use Case Diagram
* Use Case Specifications
* Actor interactions

---

### **📄 Assignment 6: Agile Planning**

Includes:

* User Stories (**US-001 to US-012**)
* Product Backlog
* Sprint Planning
* Traceability mapping

---

### **📄 Assignment 7: Kanban Workflow**

A GitHub Project Kanban board was created to manage development using Agile principles.

#### **🔧 Customization of the Kanban Board**

Additional workflow columns:

* **Testing** – Ensures tasks are verified before completion
* **Blocked** – Identifies tasks that cannot proceed

Workflow stages:

* To Do
* In Progress
* Testing
* Blocked
* Done

---

## **🆕 📊 Assignment 8: System Modeling**

This assignment focuses on modeling the **dynamic behavior of the system** using:

### **🔷 1. State Transition Diagrams**

These diagrams show how system objects change over time.

* [State Transition Diagrams](State_Transition_Diagrams.md)


Includes:

* Train lifecycle (Idle → In Service → Maintenance)
* Alert processing states
* Maintenance request lifecycle
* User account states
* Notification flow
* Sensor data processing
* System logging

Each diagram is clearly linked to:

* **Functional Requirements (e.g., FR1: Real-time train monitoring)**
* **User Stories (e.g., US-001: View real-time alerts)**

---

### **🔷 2. Activity Diagrams**

These diagrams show system workflows and processes.

* [Activity Diagrams](Activity_Diagrams.md)

Includes:

* View real-time alerts workflow
* Train monitoring process
* Intrusion detection workflow
* Maintenance process
* User authentication
* Report generation
* Notification process
* Incident reporting

Each workflow includes:

* Start/End points
* Decision logic
* System actions
* Mapping to requirements and user stories

---

### **🔷 3. Reflection**


* [PRASA Reflection](PRASA_reflection.md)


Covers:

* Challenges in system modeling
* Alignment with Agile and requirements
* Differences between state and activity diagrams
* Lessons learned across all assignments

---

## **🔗 Traceability and Integration**

All diagrams and workflows are aligned with:

### **Functional Requirements (Assignment 4)**

Examples:

* **FR1:** Monitor train locations in real time
* **FR5:** Generate operational alerts
* **FR8:** Predictive maintenance alerts
* **FR9:** User management

---
## **🆕 📊 Assignment 9:  Domain Modeling and Class Diagram Development**
## Domain Model

Includes Train, Track, Sensor, Alert, Operator, and Maintenance
entities.

## Class Diagram

See Mermaid diagram in project files.

### **User Stories (Assignment 6)**

Examples:

* **US-001:** View real-time alerts
* **US-004:** Maintenance alerts
* **US-006:** Manage users
* **US-009:** Receive notifications

This ensures **full traceability** between requirements, design, and implementation.

---

## **🛠️ Proposed Technologies**

* Web-based dashboard
* Backend API services
* Railway sensor integration
* Data storage and analytics
* Cloud or on-premise infrastructure

---

## **📌 Conclusion**

This repository contains the full system specification, design, and Agile project management implementation for the Smart Digital Monitoring System.

It demonstrates:

* Application of software engineering principles
* System analysis and design techniques
* UML modeling (state and activity diagrams)
* Agile project management using Kanban

The project provides a comprehensive approach to improving railway operational efficiency through digital transformation.
>>>>>>> 3bb1b49dea49a1d0bbf2664b35e5e811aeec573e
