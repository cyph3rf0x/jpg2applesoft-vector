import cv2
import argparse

def image_to_apple2_vectors(image_path, epsilon_factor=0.015):
    """
    Converts an image to Applesoft BASIC HPLOT commands.
    """
    
    # 1. Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from '{image_path}'. Check the path and try again.")
        return

    # 2. Resize to Apple II HGR resolution (280x192)
    img_resized = cv2.resize(img, (280, 192))

    # 3. Convert to Grayscale
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

    # 4. Edge Detection (Canny Algorithm)
    edges = cv2.Canny(gray, 100, 200)

    # 5. Find Contours 
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    apple_basic_code = []
    line_number = 10 

    # 6. Vector Approximation 
    apple_basic_code.append(f"{line_number} HGR : HCOLOR= 3") 
    line_number += 10

    for contour in contours:
        epsilon = epsilon_factor * cv2.arcLength(contour, closed=False)
        approx = cv2.approxPolyDP(contour, epsilon, closed=False)

        if len(approx) > 1:
            points = [pt[0] for pt in approx]
            cmd = f"{line_number} HPLOT {points[0][0]},{points[0][1]}"
            for p in points[1:]:
                cmd += f" TO {p[0]},{p[1]}"
            
            apple_basic_code.append(cmd)
            line_number += 10

    return apple_basic_code

# --- Command Line Interface Setup ---
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Convert an image to Apple II HGR vector lines.")
    
    # Add a required positional argument for the file path
    parser.add_argument("image", help="Path to the input image (e.g., photo.jpg)")
    
    # Add an optional argument for the detail level
    parser.add_argument("-e", "--epsilon", type=float, default=0.015, 
                        help="Detail level (default: 0.015). Lower numbers = more detail, higher = more abstract.")

    # Parse the arguments from the terminal
    args = parser.parse_args()

    # Run the function using the arguments provided by the user
    basic_script = image_to_apple2_vectors(args.image, epsilon_factor=args.epsilon)
    
    if basic_script:
        for line in basic_script:
            print(line)