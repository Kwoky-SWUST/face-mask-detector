# This is the code for the face mask detection 

This is used in the food delivery robot, and is used for human robot interaction.

link: https://blog.csdn.net/weixin_44388819/article/details/119673338


# Face Mask Detector 😷

This repository contains code for a face mask detector implemented in Python.

## Installation ⚙️

1.  **Prerequisites:**

    *   Python 3.6+
    *   pip (Python package installer)

2.  **Clone the repository:**

    ```bash
    git clone https://github.com/Kwoky-SWUST/face-mask-detector.git
    cd face-mask-detector
    ```

3.  **Install the required packages:**

    While the specific dependencies aren't listed, based on the file names, you'll likely need libraries like OpenCV and potentially others for image processing and potentially a deep learning framework.  Here's a general example, adjust based on your actual needs:

    ```bash
    pip install opencv-python numpy scikit-image # Example dependencies
    ```

    *Note: You might need to install additional packages depending on the specific implementation details within `mask_detector.py`, `preprocess.py`, and `resize.py`.*

## Key Features ✨

*   **Image Preprocessing:**  Includes functionality for image preprocessing, likely found in `src/preprocess.py`.
*   **Image Resizing:**  Provides image resizing capabilities, implemented in `src/resize.py`.
*   **Mask Detection:**  Core mask detection logic resides in `src/mask_detector.py`.
