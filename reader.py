from shared_data import realtime, lock
import serial
import time

def reader():
    # Replace '/dev/ttyACM0' with the appropriate port for your system
    port = '/dev/ttyACM0'
    baud_rate = 115200

    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(0.1)  # Wait for the serial connection to initialize

        while True:
            if ser.in_waiting > 0:  # Check if there is data waiting to be read
                line = ser.readline().decode('utf-8').rstrip()  # Read a line and decode it
                # print(line)  # Print the output or process it as needed
                data = [int(x) for x in line.split()]
                if len(data) == 6:  # Ensure we have exactly 6 values
                        with lock:
                            realtime['GyrX'] = data[0]
                            realtime['GyrY'] = data[1]
                            realtime['GyrZ'] = data[2]
                            realtime['AccX'] = data[3]
                            realtime['AccY'] = data[4]
                            realtime['AccZ'] = data[5]
                else:
                    print(f"Invalid data length: {len(data)}. Expected 6 values.")
            else:
                time.sleep(0.1)  # Avoid busy waiting

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()

if __name__ == "__main__":
    reader()
