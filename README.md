# Queue Theory Simulation in Computer Systems

## Project Overview

This project is a Python-based application for simulating and analyzing **queue theory**, supporting both **deterministic** and **non-deterministic** queue models. Built with a PyQt5-based graphical user interface (GUI), the program enables users to compute performance metrics for various queue configurations in an interactive and user-friendly manner.

The application is suitable for students, researchers, and professionals interested in exploring and understanding queue dynamics.

---

## Features

- **Supported Queue Models**:
  - Deterministic models (e.g., D/D/1): Fixed arrival and service times.
  - Non-deterministic models (e.g., M/M/1, M/M/c): Randomized arrival and service times (e.g., exponential distribution).

- **Performance Metrics**:
  - **Utilization (\u03c1)**: Server workload.
  - **Average number in system (L)**: Tasks in queue and service.
  - **Average waiting time in queue (Wq)**.
  - **Average response time (W)**.

- **Graphical User Interface (GUI)**:
  - Built with **PyQt5** for a modern and responsive user experience.
  - Easy-to-use input forms for queue parameters.
  - Real-time calculation and visualization of results.

- **Visualization**:
  - Dynamic graphs, including queue length over time and response time distribution.
  - Comparison between deterministic and non-deterministic models.

---

## Prerequisites

Before running the application, make sure you have the following:

- **Python 3.8+**
- Required Python libraries (install using `pip`):
  ```bash
  pip install pyqt5 numpy matplotlib scipy
  ```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/queue-theory-simulation.git
cd queue-theory-simulation
```

### 2. Run the Application
Start the application by running the main script:
```bash
python main.py
```

### 3. Use the GUI
1. Select the queue type: **Deterministic** or **Non-Deterministic**.
2. Input the required parameters:
   - Arrival rate (\u03bb).
   - Service rate (\u03bc).
   - Number of servers (c) (for multi-server models).
3. Click **Simulate** to view the results.

---

## Example Usage

### Simulating a Deterministic Queue (D/D/1)
1. Launch the application.
2. Choose **Deterministic** from the queue type options.
3. Input the following:
   - **Arrival time**: 2 seconds.
   - **Service time**: 1 second.
4. Click **Graph**.

**Results**:
- Utilization (\u03c1): 0.5
- Average number in system (L): 1.
- Average waiting time in queue (Wq): 0 seconds.
![QUEUEd](https://github.com/user-attachments/assets/98842602-3b6e-48cf-80b7-adbfab8d60db)

**Graphs**:
- Deterministic queue length over time.
![GRAPH](https://github.com/user-attachments/assets/52175b07-7973-4db2-b204-6a9a8846ddea)

### Simulating a Non-Deterministic Queue (M/M/1)
1. Launch the application.
2. Choose **Non-Deterministic** from the queue type options.
3. Input the following:
   - **Arrival rate (\u03bb)**: 5 tasks/second.
   - **Service rate (\u03bc)**: 7 tasks/second.
4. Click **Simulate**.

**Results**:
- Average number in system (L): 2.5.
- Average waiting time in queue (Wq): 0.35 seconds.
![st](https://github.com/user-attachments/assets/673342b5-5fec-4807-a0d1-046579e5418d)


---


---

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to the creators of **PyQt5**, **NumPy**, **Matplotlib**, and **SciPy** for providing the essential tools to build this application. This project aims to simplify the study of queue theory for both deterministic and non-deterministic systems.
