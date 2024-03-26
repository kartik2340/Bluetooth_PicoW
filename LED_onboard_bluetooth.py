from machine import Pin  # Import Pin module from machine
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral

led = Pin("LED", Pin.OUT)  # Define GPIO pin 7 for the LED
led_state = 0
ble = bluetooth.BLE()  # Create a BLE object
my_bt = BLESimplePeripheral(ble)  # Create an instance of BLESimplePeripheral

def bt_rx
(data):
    print("Data received: ", data)  # Print the received data
    if data == b'A\r\n':  # if received data is 'A'
        led.value(1)  # Turn ON the LED
        my_bt.send('LED is ON')  # Send message via Bluetooth
    elif data == b'B\r\n':  # if received data is 'B'
        led.value(0)  # Turn OFF the LED
        my_bt.send('LED is OFF')  # Send message via Bluetooth

while True:  # Infinite loop
    if my_bt.is_connected():  # Test if BLE connection is established
        my_bt.on_write(bt_rx)
