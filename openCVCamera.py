import face_recognition
import cv2

class OpenCVCamera(object):
    def __init__(self):
        """ Constructor for the OpenCV Camera Abstraction """
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        """ Destructor for the OpenCV Camera Abstraction """
    
    def get_frame(self):
        """ Method to get JPEG bytes """
        success, image = self.video.read()

        resizedFrame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        RGB_resizedFrame = resizedFrame[:, :, ::-1]

        if processThisFrame:
            face_locations = face_recognition.face_locations(RGB_resizedFrame)
            print(f"There are {len(face_locations)} faces in this frame!")

        # Convert the image to a JPEG
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()