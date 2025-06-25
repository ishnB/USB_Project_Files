import supervisor
import usb_hid
import time
import random
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

KEYBOARD_DESC = bytes((
0x05, 0x01,                         # Usage Page (Generic Desktop)
0x09, 0x06,                         # Usage (Keyboard)
0xA1, 0x01,                         # Collection (Application)
0x05, 0x07,                         #     Usage Page (Key Codes)
0x19, 0xe0,                         #     Usage Minimum (224)
0x29, 0xe7,                         #     Usage Maximum (231)
0x15, 0x00,                         #     Logical Minimum (0)
0x25, 0x01,                         #     Logical Maximum (1)
0x75, 0x01,                         #     Report Size (1)
0x95, 0x08,                         #     Report Count (8)
0x81, 0x02,                         #     Input (Data, Variable, Absolute)

0x95, 0x01,                         #     Report Count (1)
0x75, 0x08,                         #     Report Size (8)
0x81, 0x01,                         #     Input (Constant) reserved byte(1)

0x95, 0x05,                         #     Report Count (5)
0x75, 0x01,                         #     Report Size (1)
0x05, 0x08,                         #     Usage Page (Page# for LEDs)
0x19, 0x01,                         #     Usage Minimum (1)
0x29, 0x05,                         #     Usage Maximum (5)
0x91, 0x02,                         #     Output (Data, Variable, Absolute), Led report
0x95, 0x01,                         #     Report Count (1)
0x75, 0x03,                         #     Report Size (3)
0x91, 0x01,                         #     Output (Data, Variable, Absolute), Led report padding

0x95, 0x06,                         #     Report Count (6)
0x75, 0x08,                         #     Report Size (8)
0x15, 0x00,                         #     Logical Minimum (0)
0x25, 0x65,                         #     Logical Maximum (101)
0x05, 0x07,                         #     Usage Page (Key codes)
0x19, 0x00,                         #     Usage Minimum (0)
0x29, 0x65,                         #     Usage Maximum (101)
0x81, 0x00,                         #     Input (Data, Array) Key array(6 bytes)


0x09, 0x05,                         #     Usage (Vendor Defined)
0x15, 0x00,                         #     Logical Minimum (0)
0x26, 0xFF, 0x00,                   #     Logical Maximum (255)
0x75, 0x08,                         #     Report Count (2)
0x95, 0x02,                         #     Report Size (8 bit)
0xB1, 0x02,                         #     Feature (Data, Variable, Absolute)

0xC0                                # End Collection (Application)
))
# Initialize the keyboard object
keyboard = usb_hid.Device(
	report_descriptor=KEYBOARD_DESC,
	usage_page=0x01, # Generic Desktop Control
	usage=0x06, # Keyboard
	report_ids=(0,), # Descriptor uses no report IDs.
	in_report_lengths=(8,), # This gamepad sends 8 bytes in its report.
	out_report_lengths=(0,), # It does not receive any reports.
)

usb_hid.enable((usb_hid.Device.KEYBOARD,keyboard))

supervisor.set_usb_identification(
    manufacturer="China Resource Semico., Ltd",  
    product="USB Keyboard",  
    vid=0x1a2c,               
    pid=0x4c5e                
) 