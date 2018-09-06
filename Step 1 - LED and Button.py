""" HSG NightLight Step 1 - First experience with GPIOs

"""
# Standard-library imports
import time       # utilities to measure time

# third-party library imports
import gpiozero   # hardware abstraction of RaspberryPi's GPIOs and common connected peripherals

class NightLight:
    """ The HSG NightLight class.

    Features provided:
    - The red LED is enabled while the button is pressed
    - The green LED toggles enabled state when the button is pressed
    - The blue LED blinks continuously
    - A long-press stops the program
    """

    def __init__(self):
        """ Create an instance of the HSG NightLight. """

        # state
        self._keep_running = True   # signals the main loop to keep running

        # initialise
        self._setup_hardware()

    def _setup_hardware(self):
        """ Create instances of all peripherals needed. """

        # TODO: create three instances of gpiozero.LED for the three LED colours
        self._red_LED = ...
        self._green_LED = ...
        self._blue_LED = ...

        # TODO: create an instance of gpiozero.Button
        # Configure the button as following:
        # - Select the correct GPIO pin
        # - Ensure that the intenal pull-up resistor is enabled
        # - Configure that a long-press triggers it's separate event handler, e.g. after 3 seconds
        # Do not forget to register the three event handler methods below
        self._button = ...

    def _on_button_press(self):
        """ Event handler, called when the button is pressed. """
        print("Button was pressed")
        # TODO: enable red LED just while the button is being pressed
        # TODO: toggle green LED

    def _on_button_release(self):
        """ Event handler, called when the button is released. """
        print("Button was released")
        # TODO: disable red LED again

    def _on_button_hold(self):
        """ Event handler, called when the button is held for a long time. """
        print("Long button press detected -> stopping...")
        # TODO: signal the loop to stop running

    def run(self):
        """ Run the main loop, periodically checking for events.

        This function only exits at device shutdown.
        """
        print("Entering main loop")
        while self._keep_running:
            # TODO: make this loop run once every 0.25 s
            # Hint: take a look at the functions time.monotonic() and time.sleep(dt)

            # now do whatevery needs to be done
            # TODO: toggle the blue LED
            self._blue_LED.toggle()

        # we're stopping, do some cleanup

        # TODO: switch off all LEDs!

        print("Leaving main loop")

# Main entry point
if __name__ == "__main__":
    # create an instance of the HSG NightLight
    nightlight = NightLight()

    # run the instance
    nightlight.run()
