import facial_recognition as f

def processImage(img):
    image = f.load_image(img)

    numberOfFaces = len(f.face_locations(image))
    print(F"There are {numberOfFaces} faces in the image")
    return numberOfFaces