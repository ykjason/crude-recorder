def key_direction_split(inputs: list, valid_keys: list):
    #Splits the inputs in the form of left shift(KeyDown) to that of shiftleft and KeyDown while separating both
    if is_key_held(inputs):
        keys = [key[:key.index('(Key')] for key in inputs]
        direction = [key[key.index('Key'):-1] for key in inputs]
    else:
        return inputs, [None for _ in inputs]
    return pyautogui_key_format(keys, valid_keys), direction


def is_key_held(inputs: list):
    # Checks if recording KeyUp or down
    return '(Key' in inputs[0]


def pyautogui_key_format(keys: list, valid_keys: list):
    # Iterates through the list of keys and changes some that are incorectly formatted
    new_keys = []
    for key in keys:
        if key not in valid_keys:
            new_keys.append(swap_key(key))
        else: new_keys.append(key)
    return new_keys


def swap_key(key: str):
    # Correctly swaps the key name to be compatible with pyautogui's keys for only a few keys
    if ' ' in key:
        return key[key.index(' ')+1:] + key[:key.index(' ')]
    else:
        print(f'{key} has incorrect format')