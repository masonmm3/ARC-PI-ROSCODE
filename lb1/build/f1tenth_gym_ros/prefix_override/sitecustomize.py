import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mason/Documents/Ros/lb1/install/f1tenth_gym_ros'
