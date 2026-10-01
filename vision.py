import cv2
import os

def get_face_xml_path():
    # ... Keep the original implementation ...
    p1 = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
    if os.path.exists(p1):
        return p1
    p2 = "haarcascade_frontalface_default.xml"
    if os.path.exists(p2):
        return p2
    return None

def check_face_in_camera():
    """Open camera for one snapshot then close immediately, return face‑detection status"""
    xml_path = get_face_xml_path()
    if xml_path is None:
        return "[Vision System: Face‑recognition model file not found]"

    face_detector = cv2.CascadeClassifier(xml_path)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "[Vision System: Failed to open camera]"

    ret, frame = cap.read()
    cap.release()  # Release camera right after capturing one frame
    cv2.destroyAllWindows()

    if not ret:
        return "[Vision System: Failed to read frame]"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        return "[Vision System: User is sitting in front of the computer looking at the screen]"
    else:
        return "[Vision System: No human face detected in front of camera]"

if __name__ == "__main__":
    print("Testing camera, please wait...")
    result = check_face_in_camera()
    print("Detection result:", result)
