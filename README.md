# Face Recognition Using OpenCV

This project implements a face recognition system using OpenCV. The system can detect and recognize faces in real-time from live camera feeds or static images. It leverages OpenCV's powerful computer vision library to perform face detection and recognition efficiently.

## Features

- Real-time face detection using Haar Cascades.
- Face recognition based on pre-trained models.
- Supports multiple face recognition techniques.
- Can work with live camera feeds or images.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- OpenCV (`cv2`)

You can install OpenCV using pip:

```bash
pip install opencv-python
```

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/mohammadreza-mohammadi94/Face-Recognition-OpneCV.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Face-Recognition-OpneCV
    ```
3. Run the face recognition script:
    ```bash
    python face_recognition.py
    ```

The script will launch a live camera feed to detect and recognize faces in real-time.

## Usage

- **Live Camera Mode**: The script uses your webcam to detect faces in real-time.
- **Image Mode**: Modify the script to detect faces from a pre-specified image by providing the image path.

## Customization

You can fine-tune the face detection and recognition parameters in the script, such as:

- Adjusting the Haar Cascade classifier to improve detection accuracy.
- Experimenting with different recognition algorithms.

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details.
