import time                 
import argparse
from brping import Ping360
from builtins import input
import numpy as np 

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import Normalize
from matplotlib.text import TextPath

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ping python library example.")
    parser.add_argument('--device', action="store", required=False, type=str, help="Ping device port. E.g: /dev/ttyUSB0")
    parser.add_argument('--baudrate', action="store", type=int, default=115200, help="Ping device baudrate. E.g: 115200")
    parser.add_argument('--udp', action="store", required=False, type=str, help="Ping UDP server. E.g: 192.168.2.2:9092")
    args = parser.parse_args()
    if args.device is None and args.udp is None:
        parser.print_help()
        exit(1)

    p = Ping360()
    if args.device is not None:
        p.connect_serial(args.device, args.baudrate)
    elif args.udp is not None:
        (host, port) = args.udp.split(':')
        p.connect_udp(host, int(port))

    print("Initialized: %s" % p.initialize())

    print(p.set_transmit_frequency(800))
    print(p.set_sample_period(80))
    print(p.set_number_of_samples(200))

    tstart_s = time.time()
    for x in range(400):            #In Gradians, 100 = 90 degrees, so 360 deg
        p.transmitAngle(x)
        vals = bytearray(p._data) # convert the ping data to a byte array
        vals_8bit = np.array(vals).astype(np.uint8)
        np.save("/home/wrc/Desktop/Github/MICRO_UUV_PERCEPTION/data/"+str(x)+".npy", vals_8bit)
        #print("----------------------------------------------------------")
    
    tend_s = time.time()

    vals = bytearray(p._data) # convert the ping data to a byte array
    vals_8bit = np.array(vals).astype(np.uint8)
    print(vals_8bit)
    for index in vals:
        print((index+1)*5/200.) # converts index to range?

    print("full scan in %dms, %dHz" % (1000*(tend_s - tstart_s), 400/(tend_s - tstart_s)))

    # turn on auto-scan with 1 grad steps
    p.control_auto_transmit(0,399,1,0)

    tstart_s = time.time()
    # wait for 400 device_data messages to arrive
    for x in range(400):
        p.wait_message([definitions.PING360_DEVICE_DATA])
    tend_s = time.time()

    print("full scan in %dms, %dHz" % (1000*(tend_s - tstart_s), 400/(tend_s - tstart_s)))

    # stop the auto-transmit process
    p.control_motor_off()

    # turn on auto-transmit with 10 grad steps
    p.control_auto_transmit(0,399,10,0)

    tstart_s = time.time()
    # wait for 40 device_data messages to arrive (40 * 10grad steps = 400 grads)
    for x in range(40):
        p.wait_message([definitions.PING360_DEVICE_DATA])
    tend_s = time.time()

    print("full scan in %dms, %dHz" % (1000*(tend_s - tstart_s), 400/(tend_s - tstart_s)))

    p.control_reset(0, 0)
