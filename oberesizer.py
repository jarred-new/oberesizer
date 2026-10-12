import numpy as np
import cv2 # OpenCV

import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: oberesizer <image_path> [--resize <width> <height>] [--grayscale]")
        print("Usage: python oberesizer <image_path> [--resize <width> <height>] [--grayscale]")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        sys.exit(1)

    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not read the image '{image_path}'.")
        sys.exit(1)

    # Resize the image if requested
    if '--resize' in sys.argv:
        try:
            resize_index = sys.argv.index('--resize')
            width = int(sys.argv[resize_index + 1])
            height = int(sys.argv[resize_index + 2])
            image = cv2.resize(image, (width, height), interpolation=cv2.INTER_NEAREST)
        except (ValueError, IndexError):
            print("Error: Invalid resize parameters. Usage: --resize <width> <height>")
            sys.exit(1)

    # Convert to grayscale
    if '--grayscale' in sys.argv:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Display the original and grayscale images
        cv2.imshow('Original Image', image)
        cv2.imshow('Grayscale Image', gray_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
