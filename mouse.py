import cv2
import mediapipe as mp
import pyautogui
from selenium import webdriver


def videoon():
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_COUNT,30)
    hand_detector=mp.solutions.hands.Hands()
    drawing_utils=mp.solutions.drawing_utils
    screen_width,screen_height=pyautogui.size()
    index_y=0
    while True:
        _,frame=cap.read()
        frame=cv2.flip(frame,1)
        frame_height,frame_width,_=frame.shape
        rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands=output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame,hand)
                landmarks=hand.landmark
                for id, landmark in enumerate(landmarks):
                    x=int(landmark.x*frame_width)
                    y=int(landmark.y*frame_height)
                    if id==8:
                        cv2.circle(img=frame,center=(x,y),radius=20,color=(0,0,255))
                        index_x=screen_width/frame_width*x
                        index_y=screen_height/frame_height*y
                        pyautogui.moveTo(index_x,index_y,0.1)

                    
        cv2.imshow('sds',frame)
        if cv2.waitKey(1) == ord('q'):
            break


def eyecamon():
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)

driver=webdriver.Chrome()

def youtube():
    driver.get('https://www.youtube.com/')
    
    
def markuphero():
    driver.get('https://markuphero.com/new')

def spotify():
    driver.get('https://open.spotify.com/')

def tome():
    driver.get('https://tome.app/alfred-157/new-tome-clf83zibs1unya743jr0m8mq6')



