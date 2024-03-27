import cv2
import face_recognition

# Load a sample picture and learn how to recognize it.
saumitra_image = face_recognition.load_image_file("Saumitra.jpg")
saumitra_face_encoding = face_recognition.face_encodings(saumitra_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    saumitra_face_encoding,
]
known_face_names = [
    "Saumitra",
]

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Could not read frame")
        break

    rgb_frame = frame[:, :, ::-1]  # Convert BGR (OpenCV) to RGB (face_recognition)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), font, 1, (0, 255, 0), 1)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
