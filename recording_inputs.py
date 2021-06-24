import pygame
import time
import random


class InputRecorder():
    def __init__(self, inputs):
        # Initializes the input recorder object.
        # delay 0, 1, 2 represent no delay, actual delay, and randomly generated delay respectively
        # self._record_mode  may be set to values in (0, 1, 2)
        # 0 - pygame.TextInput
        # 1 - pygame.KeyDown
        # 2 - pygame.KeyUp
        self._delay = inputs[0]
        self._inputs = []
        self._record_mode = inputs[1]
        self._delay_list = []
        if self._delay == 1:
            self._start_time = time.time()
        print(self._delay, self._record_mode)



    def record(self):
        # Creates a display to enter inputs into
        # Checks the list of events and appends the key name if any key event occurs
        # Adds a delay at the end of each valid event
        self._running = True
        pygame.init()
        surface = pygame.display.set_mode((600, 600))
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type in (pygame.TEXTINPUT, pygame.KEYDOWN, pygame.KEYUP):
                    if event.type == pygame.TEXTINPUT and self._record_mode == 0:
                        self._inputs.append(event.text)
                        self._add_delay()
                    elif event.type in (pygame.KEYDOWN, pygame.KEYUP) and self._record_mode in (1,2):
                        print(pygame.event.event_name(event.type))
                        self._inputs.append(pygame.key.name(event.key)+f'({pygame.event.event_name(event.type)})')
                        self._add_delay()



            surface.fill(pygame.Color(128, 128, 128))
            pygame.display.flip()


    def _add_delay(self):
        #creates a list of numeric values representing the delay in seconds between inputs
        if self._delay == 0:
            self._delay_list.append(0)
        elif self._delay == 1:
            self._delay_list.append(time.time() - self._start_time)
            self._start_time = time.time()
        elif self._delay == 2:
            self._delay_list.append(random.random())



    def return_delay(self):
        return self._delay_list


    def change_record_mode(self, new_mode):
        assert new_mode in (0,1,2) and new_mode != self._record_mode, 'New mode must be a different, valid int'
        self._record_mode = new_mode



    def return_inputs(self):
        return self._inputs


    def show_inputs(self):
        print(self._inputs)


    def get_recording_mode(self):
        return self._record_mode



def get_input():
    delay = input('\n0 - No Delay\n1 - Actual Delay\n2 - Random Delay\nEnter delay mode:')
    record = input('\n0 - TextInput\n1 - KeyDown\n2 - KeyUp\nEnter recording mode:')
    assert delay.isnumeric() and int(delay) in (0,1,2), 'Delay must be either 0, 1, or 2'
    assert record.isnumeric() and int(record) in (0,1,2), 'Recording mode must be either 0, 1, or 2'
    return int(delay), int(record)


def run():
    inputs = get_input()
    ir = InputRecorder(inputs)
    ir.record()
    return ir


if __name__ == '__main__':
    ir = run()
    ir.show_inputs()
    print(ir.return_delay())