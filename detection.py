import cv2 as cv
import os

# Function to load images from a folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        img = cv.imread(filepath)
        if img is not None:
            images.append((filename, img))
    return images

# Load all images from the folder
folder = 'Photos'
images = load_images_from_folder(folder)

# Read the Haar cascade file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Check if Haar cascade is loaded
if haar_cascade.empty():
    print("Error: Haar cascade file not found or invalid.")
else:
    for filename, img in images:
        # Convert to grayscale
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Detect faces
        faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        print(f"-> {filename}: Number of faces found = {len(faces)}")

        # Draw rectangles around detected faces and save cropped faces
        for i, (x, y, w, h) in enumerate(faces):
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), thickness=4)
            face = img[y:y + h, x:x + w]
            face_filename = f"{filename.split('.')[0]}_face{i}.jpeg"
            cv.imwrite(face_filename, face)
            print(f"Saved {face_filename}")

        # Display the processed image
        cv.imshow(f'Detected Faces in {filename}', img)
        cv.waitKey(0)
        cv.destroyAllWindows()
