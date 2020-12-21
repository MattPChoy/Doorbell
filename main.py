from flask import Flask, render_template, Response
from camera_pi import Camera

""" Helper Methods """
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


""" Flask Routes """
@app.route('/')
def index():
    """ Landing page for the stream """
    return render_template('index.html')

@app.route('/stream')
def stream():
    """ Video streaming route. Put this in the src attribute of an img tag. """
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)