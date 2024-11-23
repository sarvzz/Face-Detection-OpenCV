# face-detection and Cropping Using OpenCV


## Overview

This project demonstrates a Python-based solution for face detection and cropping using the OpenCV library. 
It processes multiple images, detects faces using Haar cascades, and saves the cropped face images for further use. 

<div align="center">
  <img src="haar_face_detect.jpg" alt="Face Detection Image" width="300">
</div>

---

## Features

- **Batch Image Processing**: Load and process multiple images from a specified folder.
- **Face Detection**: Use Haar cascades to identify faces in images.
- **Grayscale Conversion**: Convert images to grayscale to optimize face detection.
- **Cropped Face Extraction**: Save individual faces as separate image files.
- **Visualization**: Display processed images with rectangles marking detected faces.

---

## How It Works

1. **Load Images**: All images from the `Photos` directory are loaded into the script.
2. **Grayscale Conversion**: Each image is converted to grayscale for efficient face detection.
3. **Face Detection**: Haar cascades detect faces, returning coordinates for bounding boxes.
4. **Cropping and Saving**: Detected faces are cropped and saved as separate files.
5. **Visualization**: Processed images with detected faces highlighted are displayed.


---

## Example Output

- **Input Image**: An image from the `Photos` folder.
- **Processed Image**: Displayed with rectangles marking detected faces.
- **Cropped Face Images**: Saved as individual `.jpeg` files.

---

