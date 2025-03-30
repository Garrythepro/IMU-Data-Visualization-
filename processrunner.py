import multiprocessing
from shared_data import realtime, rollpitchyaw
import reader
import plotter
import cube
from time import sleep

def main():
    # Create processes
    reader_process = multiprocessing.Process(target=reader.reader)
    plotter_process = multiprocessing.Process(target=plotter.plotter)
    cube_process = multiprocessing.Process(target=cube.runner)

    # Start the processes
    reader_process.start()
    plotter_process.start()
    cube_process.start()

    try:
        while True:
            print(realtime)  # Print the shared realtime data
            sleep(0.1)  # Sleep for a second before printing again
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        reader_process.join()
        plotter_process.join()
        cube_process.join()

if __name__ == "__main__":
    main()