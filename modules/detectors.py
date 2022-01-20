import cv2
import imutils
import glob


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    box_coordinates, weights = hog.detectMultiScale(gray, winStride=(3, 3), padding=(8, 8), scale=1.6)

    person_count = 1
    for x, y, w, h in box_coordinates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, f'Person {person_count}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person_count += 1

    cv2.putText(img, f'Total people count: {person_count - 1}', (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('output', img)

    return img


def detect_image(path, output_path):
    image = cv2.imread(path)
    image = imutils.resize(image, width=min(800, image.shape[1]))

    result_image = detect(image)

    if output_path is not None:
        cv2.imwrite(output_path, result_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_camera():
    cv2.startWindowThread()
    video = cv2.VideoCapture(0)
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 15., (640, 480))

    while True:
        check, frame = video.read()
        frame = cv2.resize(frame, (640, 480))

        frame = detect(frame)
        if out is not None:
            out.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def person_detector(args):
    image_path = args["image"]

    if args['output'] is not None and image_path is None:
        for file in glob.iglob('images/*', recursive=True):
            detect_image(file, None)

    if str(args["camera"]) == 'true':
        detect_camera()

    if image_path is not None:
        detect_image(image_path, args['output'])
