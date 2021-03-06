from enum import Enum
from abc import ABC, abstractmethod


class SecurityDevice(ABC):
    def __init__(self, active):
        self.active = active

    @abstractmethod
    def reset(self):
        pass


class Sensor(SecurityDevice):
    def __init__(self, silent, distance):
        self.silent = silent
        self.distance = distance

    def reset(self):
        print("Resetting ... Sensor version")
        self.silent = False
        self.distance = 20


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


class Camera(SecurityDevice):

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

    def reset(self):
        print("Resetting camera...")
        self.position = Position(0, 0, 0)


camera = Camera('abc', Position(1, 2, 3), Camera.CameraType.ptz)
sensor = Sensor(True, 10)

security_devices = [camera, sensor]

for security_device in security_devices:
    security_device.reset()
