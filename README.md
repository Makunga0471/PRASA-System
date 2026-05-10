# PRASA Smart Digital Monitoring System

## Assignment 11 — Persistence Repository Layer

### Project Description

This project implements a repository layer for the PRASA Smart Digital Monitoring System using Python.

The repository layer separates business logic from storage logic using the Repository Pattern.

---

## Features

- Generic Repository Interface
- CRUD Operations
- In-Memory Storage using Dictionary
- Factory Pattern for storage abstraction
- Future Database Repository Support
- Unit Testing
- UML Class Diagram

---

## Why Generics Were Used

Generics were used to make the repository reusable for multiple entities such as Train, Station, and MaintenanceReport while reducing code duplication.

---

## Why Factory Pattern Was Used

The Factory Pattern was used to allow easy switching between storage implementations such as in-memory repositories and future database repositories without changing business logic.

---

## Future-Proofing

The repository layer was designed to support future storage implementations including:

- MySQL Databases
- MongoDB
- JSON/XML File Storage
- REST APIs

---

## Running the Project

Run the following command:

```bash
python main.py