# Car-Park-In-Go - Parking Space Detection System

## Overview
This model addresses common parking challenges by providing real-time monitoring and classification of parking spaces as "Occupied" or "Vacant". By analyzing a live video feed, it eliminates the need for manual surveillance and reduces the time and fuel wasted searching for available spots. The system ensures efficient space utilization, helping drivers quickly locate parking, reducing congestion, and improving overall traffic flow. Project is integrated with API endpoint to get the current count of free and occupied spaces.  


## Techstack
- **os** - Module for interacting with operating system  
- **Flask** – Micro web framework for Python.
- **OpenCV** – real-time computer vision
- **TensorFlow/Keras** – Deep learning framework and load saved model
- **NumPy** – Library for numerical computations.
- **Pickle** – Save and load car park positions  

## Features
- **Real-time Video Processing:** Detects vehicles in real-time from a video feed.
- **Scalability**: Can be adapted to different parking lots with minor modifications.
- **Parking Space Detection:** Each frame is processed to extract regions corresponding to predefined parking spaces. The CNN model classifies these regions as either "Occupied" or "Free".  
- **Overlay Information:** The classification results are overlaid on the video frame, and the number of free and occupied spaces is counted.  
- **API for Space Count:** Provides an API endpoint to get the current count of free and occupied spaces.

## Model Performance
- **97.64% Accuracy On Train Data**  
- **93.75% Accuracy on Validation Data** 

## Setup Instructions
### 1. Clone the Repository
```sh
git clone https://github.com/21lakshh/Car-Park-In-Go.git
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required Python packages:
```sh
pip install -r requirements.txt
```

### 3. Prepare the Model and Data
- **Model:** Ensure the trained model (`model_final.h5`) is placed in the project directory.
- **Parking Positions:** Ensure `car_positions.pkl` (predefined parking space positions) is in the project directory.
- **Video Feed:** Place your test video (`carPark.mp4`) in the project directory.

### 4. Run the Application
Start the Flask application:
```sh
python main.py
```
## Project Structure
```
Parking Detection/
│── main.py               # Main Flask application file
│── model_final.h5       # Pre-trained CNN model for detecting cars
│── car_positions.pkl      # Pickled list of parking space positions
│── carPark.mp4         # Sample test video file
│── datacollection.py    # Script for collecting training data
│── test.py             # Script for testing the model
│── parkinglot.png      # Image of the parking lot
│── cropped_images1/    # Directory containing cropped parking space images
│── templates/
│   ├── index.html       # Web interface template
│   └── index.jpeg       # Image file for the web interface
│── requirements.txt     # List of Python dependencies
```

To install the dependencies, run:
```sh
pip install -r requirements.txt
```

Please download the model_final.h5 file through this drive link: 
```sh
https://drive.google.com/file/d/1ROne5iR9kiGrz_qTJjFyhvvmVjHIs04r/view?usp=sharing
```
