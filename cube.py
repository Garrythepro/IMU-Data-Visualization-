# gyroscope_cube.py
from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
import math
from shared_data import realtime

class GyroCube(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the cube model
        self.cube = self.loader.loadModel("models/box")
        self.cube.setScale(1, 1, 1)
        self.cube.setColor(1, 0, 0, 1)  # Red color
        self.cube.reparentTo(self.render)

        # Initial position
        self.cube.setPos(0, 10, 0)

        # Initialize previous angles
        self.prev_roll = 0
        self.prev_pitch = 0
        self.prev_yaw = 0

        # Add a task to update the cube's orientation
        self.taskMgr.add(self.update_cube, "update_cube_task")

    def update_cube(self, task):
        # Read gyroscope values from the shared dictionary
        gyr_x = realtime['GyrX'] if realtime['GyrX'] is not None else 0
        gyr_y = realtime['GyrY'] if realtime['GyrY'] is not None else 0
        gyr_z = realtime['GyrZ'] if realtime['GyrZ'] is not None else 0

        # Convert gyroscope values to radians
        roll = math.radians(gyr_x / 16384.0 * 180)  # Scale to degrees
        pitch = math.radians(gyr_y / 16384.0 * 180)
        yaw = math.radians(gyr_z / 16384.0 * 180)

        # Update the cube's orientation based on gyroscope data
        self.cube.setH(self.cube.getH() + yaw)
        self.cube.setP(self.cube.getP() + pitch)
        self.cube.setR(self.cube.getR() + roll)

        # Return task.cont to continue the task
        return Task.cont

def runner():
    app = GyroCube()
    app.run()

if __name__ == "__main__":
    runner()