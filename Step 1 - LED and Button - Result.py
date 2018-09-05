""" HSG NightLight Step 1 - First experience with GPIOs

"""
# Standard-library imports
import time       # utilities to measure time

# third-party library imports
import gpiozero   # hardware abstraction of RaspberryPi's GPIOs and common connected peripherals

# first-party imports
from nightlight.extended_button import ExtendedButton  # a button that knows how long it has been pressed


class NightLight:
    """ The HSG NightLight class.

    Features provided:
    - The red LED is enabled while the button is pressed
    - The green LED toggles enabled state when the button is pressed
    - The blue LED blinks continuously
    - A long-press stopps the program
    """

    def __init__(self):
        """ Create an instance of the HSG NightLight. """

        # state
        self._keep_running = True

        # initialise
        self._setup_hardware()

    def _setup_hardware(self):
        """ Create instances of all peripherals needed. """
        self._red_LED = gpiozero.LED(12)
        self._green_LED = gpiozero.LED(13)
        self._blue_LED = gpiozero.LED(19)

        self._button = ExtendedButton(4,pull_up=True)
        self._button.when_pressed = self._on_button_press
        self._button.when_released = self._on_button_release

    def _on_button_press(self):
        """ Event handler for Button-presses. """
        print(f"Button was pressed")
        # enable red LED just while the button is being pressed
        self._red_LED.enabled = True
        # toggle green LED
        self._green_LED.enabled = not self._green_LED.enabled

    def _on_button_release(self, button):
        """ Event handler for Button-releases.

        Parameters:
            - button: The button instnace that was relreased
        """
        # disable red LED again
        self._red_LED.enabled = False

        if button.previous_state_time >= 2.:
            print(f"Long button press detected ({button.previous_state_time:.1f} s) -> stopping...")
            # signal the loop to stop running
            self._keep_running = False

    def run(self):
        """ Run the main loop, periodically checking for events.

        This function only exits at device shutdown.
        """
        last_run = time.monotonic()
        while self._keep_running:
            # make this loop run once every 0.25 s
            now = time.monotonic()
            next_run = last_run + 0.25
            wait = max(0, next_run - now)
            time.sleep(wait)
            last_run = now + wait

            # now do whatevery needs to be done
            # toggle the blue LED
            self._blue_LED.enabled = not self._blue_LED.enabled

        # we're stopping, do some cleanup

        # switch off all LEDs!
        self._red_LED.enabled = False
        self._green_LED.enabled = False
        self._blue_LED.enabled = False

# Main entry poing
if __name__ == "__main__":
    # create an instance of the HSG NightLight
    nightlight = NightLight()

    # run the instance
    nightlight.run()
