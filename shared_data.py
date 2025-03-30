from multiprocessing import Manager, Lock

manager = Manager()
lock = manager.Lock()  # Create a lock for synchronization
realtime = manager.dict(
    GyrX = None,
    GyrY = None,
    GyrZ = None,
    AccX = None,
    AccY = None,
    AccZ = None
)
rollpitchyaw = manager.dict(
    Roll = None,
    Pitch = None,
    Yaw = None
)