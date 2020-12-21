import io
import time
import picamera
from base_camera import BaseCamera
from facial_recognition import processImage


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                image = stream.read()
                yield image

                # process the frame
                processImage(image)

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()