# Drone Object Avoidance Project

This project is a drone navigation system that incorporates object avoidance using the LDROBOT LD06 LiDAR sensor. It leverages multiple Python scripts, DroneKit for drone communication, and Mission Planner for coordination. The system is part of a broader drone competition requiring autonomous navigation and collision avoidance.

---

## Features
- **Object Avoidance**: Uses the LDROBOT LD06 LiDAR sensor for obstacle detection and avoidance.
- **Autonomous Navigation**: Implements waypoint navigation using DroneKit.
- **Real-Time Data Processing**: Integrates Python scripts for data capture and processing from the LiDAR sensor.
- **Multi-Terminal Execution**: Supports multiple processes (SITL, MAVProxy, Python scripts) to operate concurrently.

---

## Project Structure

```plaintext
.
├── calc_lidar_data.py      # Processes raw LiDAR data into usable formats
├── listen_to_lidar.py      # Listens to the LD06 LiDAR for real-time data
├── object_avoidance.py     # Integrates obstacle avoidance with drone navigation
├── simple_goto.py          # Demonstrates simple waypoint navigation
├── requirements.txt        # Python dependencies for the project
├── LD06 setup.pdf          # Manufacturer-provided setup guide for LD06
├── dronestuff-env39/       # Local virtual environment (excluded from GitHub)
└── README.md               # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
# Clone the repository
https://github.com/abhmulla/DroneObjectAvoidance.git
cd DroneObjectAvoidance
```

### 2. Install Dependencies

#### Create and Activate a Virtual Environment
```bash
# Create virtual environment
python -m venv dronestuff-env39

# Activate environment
# Windows
.\dronestuff-env39\Scripts\activate
# macOS/Linux
source dronestuff-env39/bin/activate
```

#### Install Required Python Packages
```bash
pip install -r requirements.txt
```

---

## Running the Project

### Overview of the Multi-Terminal Setup
To run the project, three terminals are required:

1. **Terminal 1**: Start SITL (Software-In-The-Loop simulator).
2. **Terminal 2**: Run MAVProxy for communication.
3. **Terminal 3**: Execute the Python script for object avoidance.

### Detailed Procedure

#### Terminal 1: Run SITL
1. Open a terminal and activate the SITL environment.
2. Run SITL:
   ```bash
   dronekit-sitl copter --home=53.280707,-9.031534,0,180
   ```

#### Terminal 2: Start MAVProxy
1. Open a second terminal and activate the MAVProxy environment.
2. Run MAVProxy:
   ```bash
   mavproxy.py --master tcp:127.0.0.1:5760 --out udp:172.17.208.1:14550 --nowait
   ```

#### Terminal 3: Run the Object Avoidance Script
1. Open a third terminal and activate the Python environment.
2. Execute the object avoidance script:
   ```bash
   python object_avoidance.py
   ```

---

## Explanation of Python Scripts

### 1. **calc_lidar_data.py**
Processes raw LiDAR data packets into usable formats such as distances, angles, and signal confidence values.

### 2. **listen_to_lidar.py**
Continuously listens to the LD06 LiDAR and provides real-time distance and angle data for obstacle detection.

### 3. **object_avoidance.py**
Combines data from the LiDAR with DroneKit navigation to perform object avoidance. It uses MAVLink messages to update the drone's flight path dynamically.

### 4. **simple_goto.py**
A basic waypoint navigation script that demonstrates DroneKit's capabilities to move the drone to specific GPS coordinates.

---

## Hardware Requirements
- **LDROBOT LD06 LiDAR Sensor**: For object detection.
- **Raspberry Pi or Compatible Board**: Optional, if used for hardware interfacing.
- **Computer with Mission Planner Installed**: For manual coordination and monitoring.

---

## Key Dependencies
- **Python 3**: Windows Terminal
- **Python 2**: Ubuntu Terminal
- **DroneKit**: For drone communication.
- **MAVProxy**: Middleware for drone control.
- **numpy**: For numerical operations.
- **apscheduler**: For scheduling periodic tasks.

To install all dependencies, use:
```bash
pip install -r requirements.txt
```

---

## References and Acknowledgments

### Code Repositories
- **MAVLink Messages**: Based on code from [rasheeddo/ATCart-AP-lidar](https://github.com/rasheeddo/ATCart-AP-lidar?tab=readme-ov-file).
- **LD06 Data Parsing**: Inspired by [drinking-code/ldrobot-ld06-lidar-python-driver](https://github.com/drinking-code/ldrobot-ld06-lidar-python-driver/blob/master/listen_to_lidar.py).

### Documentation and Guides
- **Copter Object Avoidance**: [ArduPilot Code Overview](https://ardupilot.org/dev/docs/code-overview-object-avoidance.html).
- **Simple Object Avoidance**: [ArduPilot Documentation](https://ardupilot.org/copter/docs/common-simple-object-avoidance.html).
- **Bendy Ruler Algorithm**: [Overview](https://ardupilot.org/copter/docs/common-oa-bendyruler.html), [C++ Implementation](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AC_Avoidance/AP_OABendyRuler.cpp).
- **MAVLink Messages**: [MAVLink Obstacle Distance](https://mavlink.io/en/messages/common.html#OBSTACLE_DISTANCE).

---

## Future Work
- Create a simulation for testing object avoidance 
