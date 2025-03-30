# IMU Data Visualization
This is a Python and Micropython implemetation of visualizing continuous IMU data using realtime graphs. It also calculates roll, pitch, and yaw, and visualizes them using a cube in 3D space.

MPU-6500 (accel + gyro) and Raspberry Pi Pico W was used for testing. However you can use any other IMU sensor by changing the main.py file to fit it. For mag readings, you will have to make changes in other files as well. You can also use any other microcontroller that has support for Micropython.

### File Overview:
Here is a list of the files in this repo:

* main.py: This file contains the code that the microcontroller will run. It needs to be loaded onto the microcontroller. 
* processrunner.py: This file is intended to be run on the computer. It runs all the associated files.
* reader.py: This reads the data provided by the microcontroller in real-time.
* plotter.py: This plots the data provided by reader.py in real-time.
* cube.py: This visualizes the gyro data as yaw, pitch, roll provided by reader.py in real-time.
* shared_data.py: This contains variables shared by the python files. Since, multiprocessing is used, variables need to be shared this way.
* Wiring.fzz: This is a schematic wiring diagram intended to be opened by fritzing.


### Requirements:
* Libraries: serial, matplotlib, multiprocessing, panda3d. Other libraries used are built-in python.
* A microcontroller capable of running micropython.
* An IMU sensor capable of outputting gyroscrope and accelerometer readings (6DoF).
Wire the hardware according to the schematic given (for different sensor or microcontroller, follow their documentation). Make sure that both the microcontroller and the sensor operate on the same voltage (3.3v in this case).

### Procedure:
1. Connect the hardware according to the schematic given.
2. Connect the microcontroller to the computer via a usb cable. 
3. Flash the micropython firmware. You can find details of the Pico on this link: https://www.raspberrypi.com/documentation/microcontrollers/micropython.html. Disconnect and reconnect the microcontroller.
4. Clone this repo using git or curl or just download and extract zip file.
4. Drop the main.py file on the microcontroller using either Thonny or VS Code with Micropico extension, or an editor of your choice. Disconnect and reconnect the microcontroller.
5. Run the processrunner.py file in terminal or a code-editor/IDE. You will see a live graph and a cube visualization of the sensor readings.
