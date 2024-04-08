import cv2

def show_ip_camera(url):
    cap = cv2.VideoCapture(url)

    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560);
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440);

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("IP Camera Stream", frame)

        # Press 'q' on the keyboard to exit the stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Replace with your IP camera URL
ip_camera_url = 2
#ip_camera_url = 'http://192.168.5.45:5000/video'
show_ip_camera(ip_camera_url)

