from serial.tools import list_ports

def list_serial_ports():
    ports = list_ports.comports()
    for port in ports:
        print("device:", port.device)
        print("name:", port.name)
        print(port.description)
        print()

list_serial_ports()
