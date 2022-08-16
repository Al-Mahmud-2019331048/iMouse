import cv2
import mediapipe
import pyautogui

# open web camera
cam = cv2.VideoCapture(0)

# detect face
face_mesh = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_width, screen_height = pyautogui.size()
while True:
    _, frame = cam.read()
    # flipping image
    frame = cv2.flip(frame, 1)
    # rgb mode
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)

    # mark full face
    landmark_points = output.multi_face_landmarks
    frame_height, frame_width, _ = frame.shape

    # print(landmark_points)
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for i, landmark in enumerate(landmarks[474:478]):
            # position
            # print(len(landmarks[474:478]))
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            # print(x, y)

            cv2.circle(frame, (x, y), 3, (0, 255, 0))

            # moving mouse
            if i == 1:
                screen_x = 1.7 * screen_width / frame_width * x
                screen_y = 1.7 * screen_height / frame_height * y
                pyautogui.moveTo(screen_x, screen_y)

        left= [landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        print(left[0].y-left[1].y)
        if (left[0].y-left[1].y)< 0.025:
            print('click')
            pyautogui.click()
            pyautogui.sleep(1)




    cv2.imshow("iMouse", frame)
    cv2.waitKey(1)  # waiting for listener
