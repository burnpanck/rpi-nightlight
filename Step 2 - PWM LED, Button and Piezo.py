""" HSG NightLight Step 2 - Full implementation of LED, Button and Piezo speaker drivers.

"""
# Standard-library imports
import time       # utilities to measure time

# third-party library imports
import gpiozero   # hardware abstraction of RaspberryPi's GPIOs and common connected peripherals

# first-party imports
from nightlight import colour_constants as C   # named colour constants


class NightLight:
    """ The HSG NightLight class.

    Features provided:
    - Colour changes with each button press
    - An indicator sound is produced with each button press
    - A long-press stops the program
    """

    def __init__(self):
        """ Create an instance of the HSG NightLight. """
        # configuration
        self._sequence = (
            C.FIREBRICK,
            C.ALICEBLUE,
            C.AQUAMARINE1,
            C.GREEN,
            C.GOLD1,
        )

        # state
        self._keep_running = True

        # initialise
        self._setup_hardware()

        # set initial colour
        self.LEDs = C.RED1

    def _setup_hardware(self):
        """ Create instances of all peripherals needed. """
        # TODO: create an instance of gpiozero.RGBLED

        # TODO: create an instance of gpiozero.PWMOutputDevice for the piezo

        # TODO: ensure that the following button is connected to the correct GPIO
        self._button = gpiozero.Button(4,hold_time=3,hold_repeat=False,pull_up=True)
        self._button.when_pressed = self._on_button_press
        self._button.when_released = self._on_button_release
        self._button.when_held = self._on_button_hold

    def _on_button_press(self):
        """ Event handler, called when the button is pressed. """
        print("Button was pressed")
        # set LED to next colour in the sequence
        # TODO: Assign next colour in sequence to LED

        # TODO: Trigger a piezo sound


    def _on_button_release(self):
        """ Event handler, called when the button is released """
        print("Button was released")
        # nothing left to do
        pass

    def _on_button_hold(self):
        """ Event handler, called when the button is held for a long time. """
        print(f"Long button press detected -> stopping...")
        # signal the loop to stop running
        self._keep_running = False

    @property
    def LEDs(self):
        """ Return a tuple `(R,G,B)` of the current LED brightness value (range 0..1). """
        # TODO: return the currently active state of the LED

    @LEDs.setter
    def LEDs(self, value):
        """ Set the LED brightness value to the given `(r,g,b)` tuple. """
        if isinstance(value, (tuple, list)):
            # we received an (r,g,b) tuple
            r,g,b = value
        else:
            # assume we received a single value -> set it to all three channels
            r = g = b = value
        print(f"Setting LEDs to {100*r:.0f}/{100*g:.0f}/{100*b:.0f}")
        # TODO: Set the LED to the given RGB values

    def run(self):
        """ Run the main loop, periodically checking for events.

        This function only exits at device shutdown.
        """
        print("Entered main loop")
        last_run = time.monotonic()
        while self._keep_running:
            # make this loop run once every 0.25 s
            now = time.monotonic()
            next_run = last_run + 0.25
            wait = max(0, next_run - now)
            time.sleep(wait)
            last_run = now + wait

            # now do whatevery needs to be done
            pass  # nothing

        # we're stopping, do some cleanup

        # switch off all LEDs!
        # TODO: ensure LEDs are switched off
        print("Leaving main loop")


# Main entry point
if __name__ == "__main__":
    # create an instance of the HSG NightLight
    nightlight = NightLight()

    # run the instance
    nightlight.run()
