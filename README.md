<div align="center">

# MysticMotion

### Gesture-Controlled Augmented Reality Effects System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-FF6F00?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![AR](https://img.shields.io/badge/Augmented%20Reality-Interactive-8A2BE2?style=for-the-badge)

</div>

---

<div align="center">

**Turn hand gestures into real-time superpowers.**

</div>
MysticMotion is a real-time gesture-controlled augmented reality project built with Python, OpenCV, MediaPipe, and NumPy.

The project uses a webcam to track hand movements, recognize predefined gestures, and trigger superhero-inspired visual effects in real time.

The idea behind MysticMotion was to build something fun that could be explored and played with my nephew, Nafiu, while also making technology and programming more interesting and engaging for him.

## Features

### Doctor Strange Portal

A specific Doctor Strange-inspired hand pose is detected using MediaPipe hand landmarks.

The system then tracks the movement of the index finger. When the required motion is detected, a portal animation is triggered and rendered over the live camera feed.

### Spider-Man Web Shooter

A Spider-Man-inspired hand pose is detected using the hand landmarks.

When the gesture is recognized, a web animation is triggered from the wrist area and rendered onto the webcam feed.

## How It Works

```text
Webcam
   |
   v
Video Frame Capture
   |
   v
Hand Detection
   |
   v
21 Hand Landmarks
   |
   v
Gesture Recognition
   |
   +----------------------+
   |                      |
   v                      v
Doctor Strange        Spider-Man
Gesture               Gesture
   |                      |
   v                      v
Motion Detection      Web Trigger
   |                      |
   v                      v
Portal Animation      Web Animation
   |                      |
   +----------+-----------+
              |
              v
       AR Overlay Rendering
              |
              v
        Final Camera Feed
```

## Animation Processing Pipeline

The visual effects are prepared separately before being used during real-time rendering.

```text
AI Generated Video
        |
        v
      MP4
        |
        v
Frame Extraction
        |
        v
PNG Sequence
        |
        v
Background Removal
        |
        v
Transparent PNG
        |
        v
Real-Time Animation
```

This approach allows the application to play the effects frame by frame and provides control over transparency and animation playback.

## Project Structure

```text
MysticMotion/
│
├── main.py
│
├── assets/
│   ├── videos/
│   │   ├── portal.mp4
│   │   └── web.mp4
│   │
│   ├── frames/
│   │   ├── portal/
│   │   └── web/
│   │
│   └── transparent/
│       ├── portal/
│       └── web/
│
├── gesture/
│   ├── hand_tracker.py
│   ├── strange_pose.py
│   ├── strange_circle.py
│   └── spider_pose.py
│
├── effects/
│   ├── overlay.py
│   ├── portal_player.py
│   └── web_player.py
│
├── scripts/
│   ├── extract_frames.py
│   └── remove_green.py
│
└── README.md
```

## Technologies

* Python
* OpenCV
* MediaPipe
* NumPy

## Core Concepts

* Computer Vision
* Hand Tracking
* Gesture Recognition
* Motion Analysis
* Augmented Reality
* Real-Time Video Processing
* Image Compositing
* Alpha Blending
* Animation Rendering

## Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
cd MysticMotion
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows Git Bash:

```bash
source .venv/Scripts/activate
```

Install the dependencies:

```bash
pip install opencv-python opencv-contrib-python mediapipe numpy
```

## Running the Project

Make sure your webcam is connected and the required animation assets are available.

Then run:

```bash
python main.py
```

Press `ESC` to exit the application.

## MediaPipe

MysticMotion uses MediaPipe Hands to detect and track hand landmarks.

Each detected hand provides 21 landmarks that are used to determine finger positions and recognize the predefined gestures.

## Project Motivation

This project started as a fun experiment rather than a production application.

The goal was to create something interactive that could be enjoyed with my nephew, Nafiu, while using it as an opportunity to introduce him to the possibilities of programming, computer vision, and technology.

Building something that can respond to your own movements makes the underlying concepts much easier to see and understand.

## Status

The core real-time AR system is functional, including hand tracking, gesture recognition, portal animation, and web animation.

## License

This project is intended for educational and experimental purposes.
