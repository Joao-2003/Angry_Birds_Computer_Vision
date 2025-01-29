global mouse_x
global pinch_detected
global mouse_y
global pinch_initialized
global pinch_start_time
import cv2
import mediapipe as mp
import time
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mouse_x, mouse_y = (0, 0)
pinch_detected = False
pinch_start_time = None
pinch_initialized = False
MIN_PINCH_DURATION = 0.2
sling_x, sling_y = (0, 0)
SCALE_FACTOR_X = 1.5
SCALE_FACTOR_Y = 3.0
CENTER_OFFSET_X = 0.3
CENTER_OFFSET_Y = 0.2


def detect_hand_movements():
    global pinch_start_time
    global pinch_initialized
    global mouse_y
    global pinch_detected
    global mouse_x
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        if results.multi_hand_landmarks:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                if handedness.classification[0].label == 'Left':
                    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    thumb_coords = (int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0]))
                    index_coords = (int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0]))
                    distance = ((thumb_coords[0] - index_coords[0]) ** 2 + (thumb_coords[1] - index_coords[1]) ** 2) ** 0.5
                    if distance < 30:
                        if pinch_start_time is None:
                            pinch_start_time = time.time()
                        elif time.time() - pinch_start_time > MIN_PINCH_DURATION:
                            pinch_detected = True
                            if not pinch_initialized:
                                mouse_x = int(sling_x + frame.shape[1] * CENTER_OFFSET_X)
                                mouse_y = int(sling_y + frame.shape[0] * CENTER_OFFSET_Y)
                                pinch_initialized = True
                            else:
                                mouse_x = int((index_coords[0] - frame.shape[1] * CENTER_OFFSET_X) * SCALE_FACTOR_X + sling_x)
                                mouse_y = int((index_coords[1] - frame.shape[0] * CENTER_OFFSET_Y) * SCALE_FACTOR_Y + sling_y)
                    else:
                        pinch_detected = False
                        pinch_start_time = None
                        pinch_initialized = False
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow('Hand Movement Detection', frame)
        if cv2.waitKey(1) & 255 == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()