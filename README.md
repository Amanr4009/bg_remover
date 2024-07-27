# Background Removal Script

This project provides a Python script to remove the background from an image, specifically focusing on accurately isolating a person or object in the image. The script leverages the `rembg` library which uses the U2Net model for background removal, providing accurate results.

## Features

- Accurate background removal using the U2Net model.
- Easy-to-use script with minimal dependencies.
- Outputs a new image with the background removed.

## Requirements

- Python 3.x
- `opencv-python-headless`
- `numpy`
- `rembg`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Amanr4009/bg_remover.git
   cd background-removal-script
   
2. **Install Required Libraries**:
``
pip install opencv-python-headless numpy rembg``

## Usage
**Save the Image**:
Save your target image to the specified path. In this example, we use image.png.

**Run the Script**:
python `remove_background.py`

**View the Output**:
The output image will be saved as output_image.png in the current directory.

## Acknowledgements
* rembg library for the U2Net model.
  
* OpenCV for image processing.

* NumPy for array manipulations.
