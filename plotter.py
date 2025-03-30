import matplotlib.pyplot as plt
from shared_data import realtime, lock
import time

def plotter():
    plt.ion()  # Enable interactive mode for dynamic plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    # Set the y-axis limits
    ax1.set_ylim(-18000, 18000)
    ax2.set_ylim(-18000, 18000)

    # Set labels and titles
    ax1.set_title('Gyroscope Data')
    ax1.set_ylabel('Gyr Values')
    ax2.set_title('Accelerometer Data')
    ax2.set_ylabel('Acc Values')
    ax2.set_xlabel('Time')

    # Create line objects for each axis
    line1, = ax1.plot([], [], label='GyrX', lw=2)
    line2, = ax1.plot([], [], label='GyrY', lw=2)
    line3, = ax1.plot([], [], label='GyrZ', lw=2)

    line4, = ax2.plot([], [], label='AccX', lw=2)
    line5, = ax2.plot([], [], label='AccY', lw=2)
    line6, = ax2.plot([], [], label='AccZ', lw=2)

    ax1.legend()
    ax2.legend()

    x_data = []
    y1_data = []
    y2_data = []
    y3_data = []
    y4_data = []
    y5_data = []
    y6_data = []

    window_size = 50  # Set the desired window size

    while True:
        with lock:
            gyrx = realtime['GyrX']
            gyry = realtime['GyrY']
            gyrz = realtime['GyrZ']
            accx = realtime['AccX']
            accy = realtime['AccY']
            accz = realtime['AccZ']

        # Append the current data to the lists
        x_data.append(len(x_data))  # Use a simple index for x-axis
        y1_data.append(gyrx)
        y2_data.append(gyry)
        y3_data.append(gyrz)
        y4_data.append(accx)
        y5_data.append(accy)
        y6_data.append(accz)

        # Update the line data
        line1.set_data(x_data, y1_data)
        line2.set_data(x_data, y2_data)
        line3.set_data(x_data, y3_data)
        line4.set_data(x_data, y4_data)
        line5.set_data(x_data, y5_data)
        line6.set_data(x_data, y6_data)

        # Set the x-axis limits to create a sliding window effect
        if len(x_data) >= window_size:
            ax1.set_xlim(len(x_data) - window_size, len(x_data))
            ax2.set_xlim(len(x_data) - window_size, len(x_data))
        else:
            ax1.set_xlim(0, window_size)
            ax2.set_xlim(0, window_size)

        # Rescale the axes
        ax1.relim()
        ax1.autoscale_view()
        ax2.relim()
        ax2.autoscale_view()

        # Draw the updated figure
        fig.canvas.draw()
        fig.canvas.flush_events()

        time.sleep(0.1)  # Update every second

if __name__ == "__main__":
    plotter()
