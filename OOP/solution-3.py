from enum import Enum

class Position:
    def __init__(self, pan, tilt, zoom):
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom

    def __str__(self):
        return f"Pan: {str(self.pan)}. Tilt: {str(self.tilt)}. Zoom: {str(self.zoom)}."

    def __eq__(self, other):
        return self.pan == other.pan and self.tilt == other.tilt and self.zoom == other.zoom

    __hash__ = None
            

class Camera:

    def parse_camera():
        with open("cameras.txt") as f:
            d = f.read().split(" ")
            serial_number = d[0]
            position = Position(int(d[1]), int(d[2]), int(d[3]))
            camera_type = Camera.CameraType[d[4]]

        return Camera(serial_number, position, camera_type)

    def __init__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type

    def __str__(self):
        return f"Serial number: {self.serial_number}. Camera type: {self.camera_type}. " + self.position.__str__()

    def __eq__(self, other):
        return self.serial_number == other.serial_number and self.position == other.position and self.camera_type == other.camera_type

    __hash__ = None

    class CameraType(Enum):
        ptz = 0
        eptz = 1
        stationary = 2

c = Camera.parse_camera()
print(c)