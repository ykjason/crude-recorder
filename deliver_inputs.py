import recording_inputs
import format_inputs
import pyautogui
import time


def start():
    # Gathers and returns the recorded inputs and delays
    recorded = recording_inputs.run()
    inputs = recorded.return_inputs()
    delays = recorded.return_delay()
    return inputs, delays


if __name__ == '__main__':
    inputs, delays = start()
    inputs, directions = format_inputs.key_direction_split(inputs, pyautogui.KEYBOARD_KEYS)
    input_sequence = zip(inputs, directions, delays)
    time.sleep(2) # time before inputs are generated
    for i in input_sequence:
        input, direction, delay = i
        time.sleep(delay)
        if direction == None:
            pyautogui.press(input)
        else:
            if direction == 'KeyDown':
                pyautogui.keyDown(input)
            else:
                pyautogui.keyUp(input)
