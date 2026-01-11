# Colonoscope System Redesign

An engineering-focused redesign of a colonoscope angulation system combining embedded motor control, a custom 3D-printed mechanical interface, and a Python-based simulation environment for testing and iteration.

## Motivation
Conventional colonoscope angulation mechanisms are mechanically complex and difficult to prototype or modify without extensive physical testing. This project explores a modular approach where actuation, control logic, and simulation are developed together to better understand system behavior and design trade-offs.

## System Overview
The project consists of a physically implemented motor-driven angulation mechanism and a software simulation used to model and test motion behavior.

### Physical Implementation
- A motor-driven system controls **vertical (up/down) angulation** of the colonoscope tip
- A **custom 3D-printed coupling** connects the motor to chain-driven ropes that actuate the angulation tip
- The mechanical design translates motor rotation into controlled rope tension
- Left/right angulation is not yet implemented

### Embedded Control (Arduino)
- Arduino code handles motor control logic
- Designed to drive the motor in a controlled and repeatable manner
- Structured to allow future expansion to additional degrees of freedom

### Simulation Environment (Python)
- A Python-based simulator models colonoscope segments and tip motion
- Used to visualize and reason about system behavior
- Enables testing of control logic concepts without relying solely on hardware

## Project Structure
- Colonoscope  
  - Colonoscope_Arduino  
    - colonoscope_control  
      - colonoscope_control.ino  
  - Colonoscope_Simulator  
    - requirements.txt  
    - src  
      - main.py  
      - controller.py  
      - scene.py  
      - segments.py  
  - README.md

## Technologies Used
- Arduino (motor control)
- Python (simulation)
- 3D printing (mechanical coupling)
- Chain-and-rope actuation mechanism

## Current Capabilities
- Physical motor-driven **up/down angulation**
- Custom mechanical interface between motor and actuation chains
- Software simulation aligned with the physical control logic

## Limitations & Future Work
- Add left/right angulation (additional motor and control channel)
- Integrate feedback for closed-loop control
- Improve physical modeling accuracy in simulation
- Hardware–software co-validation


