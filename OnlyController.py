import pygame
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time
from screeninfo import get_monitors

# Get screen resolution
monitor = get_monitors()[0]  # Assume there is only one monitor
screen_width = monitor.width
screen_height = monitor.height

# Define sensitivity
sensitivity = 10  # Initial sensitivity

# Initialize mouse and keyboard controllers
mouse = MouseController()
keyboard = KeyboardController()

# Initialize virtual mouse position
virtual_x, virtual_y = screen_width // 2, screen_height // 2
last_mouse_x, last_mouse_y = virtual_x, virtual_y

# Update the mouse position interval
frame_delay = 2  # If update every 10 ms, approximately 100FPS

def initialize_pygame():
    """Initialize pygame and detect the joystick"""
    pygame.init()
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No joystick detected!")
        exit()

    # Select the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    return joystick

def initialize_controllers():
    """Initialize mouse and keyboard controllers"""
    mouse_controller = MouseController()
    keyboard_controller = KeyboardController()
    return mouse_controller, keyboard_controller

def get_joystick_input(joystick):
    """Get the joystick's input values"""
    x_axis = joystick.get_axis(0)  # Left joystick X-axis
    y_axis = joystick.get_axis(1)  # Left joystick Y-axis
    return x_axis, y_axis

def handle_button_events(event, mouse, keyboard):
    """Handle button press and release events"""
    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 0:  # A button -> Left mouse button
            mouse.press(Button.left)
        elif event.button == 1:  # B button -> Right mouse button
            mouse.press(Button.right)
        elif event.button == 2:  # X button -> Left Ctrl key
            keyboard.press(Key.ctrl_l)

    elif event.type == pygame.JOYBUTTONUP:
        if event.button == 0:  # A button -> Release left mouse button
            mouse.release(Button.left)
        elif event.button == 1:  # B button -> Release right mouse button
            mouse.release(Button.right)
        elif event.button == 2:  # X button -> Release left Ctrl key
            keyboard.release(Key.ctrl_l)

def update_virtual_cursor_position(joystick, mouse):
    """Update the virtual cursor position based on joystick or mouse input"""
    global virtual_x, virtual_y, last_mouse_x, last_mouse_y
    
    # Get the physical mouse position
    mouse_position = mouse.position
    mouse_x, mouse_y = mouse_position

    # Check if the physical mouse has moved
    mouse_moved = (mouse_x != last_mouse_x) or (mouse_y != last_mouse_y)

    # If the physical mouse has moved, use its position; otherwise, use joystick input
    if mouse_moved:
        # Update virtual cursor position to match the physical mouse position
        virtual_x = mouse_x
        virtual_y = mouse_y
    else:
        # Get the values from the left joystick (range -1 to 1)
        x_axis, y_axis = get_joystick_input(joystick)

        # Map joystick input to virtual mouse movement
        move_x = x_axis * sensitivity
        move_y = y_axis * sensitivity

        # Update virtual mouse position
        virtual_x += move_x
        virtual_y += move_y

        # Ensure the virtual mouse stays within screen bounds
        virtual_x = max(0, min(screen_width, virtual_x))
        virtual_y = max(0, min(screen_height, virtual_y))

    # Set the virtual mouse's new position
    mouse.position = (virtual_x, virtual_y)

    # Update the last known physical mouse position
    last_mouse_x, last_mouse_y = mouse_x, mouse_y

def main_loop():
    """Main program loop"""
    joystick = initialize_pygame()
    mouse, keyboard = initialize_controllers()

    last_time = pygame.time.get_ticks()

    try:
        while True:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - last_time

            if elapsed_time > frame_delay:
                last_time = current_time

                # Handle pygame events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    # Handle button events (press and release)
                    handle_button_events(event, mouse, keyboard)

                # Update the virtual mouse position
                update_virtual_cursor_position(joystick, mouse)

            # Control program speed to prevent excessive CPU usage
            time.sleep(0.001)  # Pause for 1 ms to reduce CPU usage

    except KeyboardInterrupt:
        pygame.quit()

if __name__ == "__main__":
    main_loop()
