from machine import I2C, Pin
import time

class MPU6500:
    def __init__(self, i2c, addr):
        self.i2c = i2c
        self.addr = addr
        self.initialize()

    def initialize(self):
        # Wake up the MPU-6500
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')  # PWR_MGMT_1 register
        time.sleep(0.1)  # Wait for the device to stabilize

        # Configure the accelerometer and gyroscope
        self.i2c.writeto_mem(self.addr, 0x1B, b'\x00')  # Gyroscope config: ±250 °/s
        self.i2c.writeto_mem(self.addr, 0x1C, b'\x00')  # Accelerometer config: ±2g

    def read_raw_values(self):
        # Read 14 bytes of data starting from the ACCEL_XOUT_H register
        data = self.i2c.readfrom_mem(self.addr, 0x3B, 14)

        # Extract raw acceleration values
        ax = (data[0] << 8) | data[1]  # ACCEL_XOUT_H and ACCEL_XOUT_L
        ay = (data[2] << 8) | data[3]  # ACCEL_YOUT_H and ACCEL_YOUT_L
        az = (data[4] << 8) | data[5]  # ACCEL_ZOUT_H and ACCEL_ZOUT_L

        # Extract raw gyroscope values
        gx = (data[8] << 8) | data[9]  # GYRO_XOUT_H and GYRO_XOUT_L
        gy = (data[10] << 8) | data[11]  # GYRO_YOUT_H and GYRO_YOUT_L
        gz = (data[12] << 8) | data[13]  # GYRO_ZOUT_H and GYRO_ZOUT_L

        # Convert to signed values
        if ax >= 32768: ax -= 65536
        if ay >= 32768: ay -= 65536
        if az >= 32768: az -= 65536
        if gx >= 32768: gx -= 65536
        if gy >= 32768: gy -= 65536
        if gz >= 32768: gz -= 65536

        return (gx, gy, gz, ax, ay, az)

# Example of usage
if __name__ == "__main__":
    i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Adjust pins as necessary
    addr = 0x68  # Define the I2C address here
    mpu = MPU6500(i2c, addr)  # Pass the address to the MPU6500 instance

    while True:
        raw_values = mpu.read_raw_values()
        print(f"{raw_values[0]} {raw_values[1]} {raw_values[2]} {raw_values[3]} {raw_values[4]} {raw_values[5]}")
        time.sleep(0.01)  # Delay for readability
