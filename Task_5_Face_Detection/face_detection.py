import cv2

# Load Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def detect_faces(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(40, 40)
    )

    count = 1

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Face {count}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        count += 1

    cv2.putText(
        frame,
        f"Total Faces: {len(faces)}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    return frame


def detect_image():

    path = input("\nEnter image path: ")

    image = cv2.imread(path)

    if image is None:
        print("Unable to open image.")
        return

    result = detect_faces(image)

    h, w = result.shape[:2]

    max_width = 1200
    max_height = 700

    scale = min(max_width / w, max_height / h)

    if scale < 1:
        result = cv2.resize(
            result,
            (int(w * scale), int(h * scale))
        )

    cv2.namedWindow("Image Face Detection", cv2.WINDOW_NORMAL)
    cv2.imshow("Image Face Detection", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_video():

    path = input("\nEnter video path: ")

    video = cv2.VideoCapture(path)

    if not video.isOpened():
        print("Unable to open video.")
        return

    while True:

        success, frame = video.read()

        if not success:
            break

        frame = detect_faces(frame)

        cv2.imshow("Video Face Detection", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def detect_webcam():

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Unable to access webcam.")
        return

    while True:

        success, frame = camera.read()

        if not success:
            break

        frame = detect_faces(frame)

        cv2.imshow("Live Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


while True:

    print("\nFace Detection System")
    print("1. Detect Faces from Image")
    print("2. Detect Faces from Video")
    print("3. Live Webcam Detection")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        detect_image()

    elif choice == "2":
        detect_video()

    elif choice == "3":
        detect_webcam()

    elif choice == "4":
        print("\nProgram Closed.")
        break

    else:
        print("\nInvalid Choice.")