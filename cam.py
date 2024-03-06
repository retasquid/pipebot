#-----LIBRARIES-----
#pip3 install Flask
#pip install opencv-python
from flask import Flask, render_template, Response
import cv2


app = Flask(__name__)

@app.route('/')

def index():
    """Video streaming home page."""
    return render_template('cam.html')

def gen():
    cap = cv2.VideoCapture(1)
    while True:
        ret,frame=cap.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame=jpeg.tobytes()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port =2006, debug=True, threaded=True)