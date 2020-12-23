import io
import socket
import struct
from PIL import Image

# Start a socket listening for connections on 0.0.0.0:8000
# (0.0.0.0) means listening on all interfaces
print(f"Socket hostname: {socket.gethostname()}")

server_socket = socket.socket()
print("Socket object created")
# server_socket.bind(('0.0.0.0', 8000))
server_socket.bind(('192.168.1.42', 8000))
print("Server socket bound")
server_socket.listen(0)
print("Socket listening")

# Accept a single connection and make a file-like object out of it
# connection = server_socket.accept()[0].makefile('rb')
connection = server_socket.accept()
print("Connected")
try:
    while True:
        print(".")
        # Read the ength of the image as a 32-bit unsigned int.
        # If the length is 0 (stopped transmitting), exit out of the loop

        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
    
        # Construct a stream to hold the image data and read the image
        # data from the connection

        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))

        # Rewind the stream, open it as an image with PIL and do some processing on it
        image_stream.seek(0) # Go back to the start of the image stream.
        image = Image.open(image_stream)

        print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')
finally:
    connection.close()
    server_socket.close()