""" HSG NightLight Step 2 - Full implementation of LED, Button and Piezo speaker drivers.

"""
# Standard-library imports
import time       # utilities to measure time

# third-party library imports
import gpiozero   # hardware abstraction of RaspberryPi's GPIOs and common connected peripherals

# first-party imports
from nightlight import colour_constants as C   # named colour constants
from nightlight.extended_button import ExtendedButton  # a button that knows how long it has been pressed

class NightLight:
    """ The HSG NightLight class.

    Features provided:
    - Colour changes with each button press
    - An indicator sound is produced with each button press
    - A long-press stopps the program
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
        self._main_LED = gpiozero.RGBLED(12,13,19,pwm=True)

        self._piezo = gpiozero.PWMOutputDevice(18,frequency=400)

        self._button = ExtendedButton(4,pull_up=True)
        self._button.when_pressed = self._on_button_press
        self._button.when_released = self._on_button_release

    def _on_button_press(self):
        """ Event handler for Button-presses. """
        print(f"Button was pressed")
        # set LED to next colour in the sequence
        self.LEDs = self._sequence[0]
        # rotate the sequence (first all elements following the first, then all up to the first)
        self._sequence = self._sequence[1:] + self._sequence[:1]
        # and switch on the piezo-speaker
        self._piezo.value = 0.5  # 0.5 is the loudest value


    def _on_button_release(self, button):
        """ Event handler for Button-releases.

        Parameters:
            - button: The button instnace that was relreased
        """
        # switch off the piezo speaker again
        self._piezo.value = 0
        # check button-press time
        if button.previous_state_time < 2.:
            # short press, less than 2 seconds -> do nothing further
            return
        print(f"Long button press detected ({button.previous_state_time:.1f} s) -> stopping...")
        # switch off the LED!
        self.LEDs = C.BLACK
        # stop the loop
        self._keep_running = False

    @property
    def LEDs(self):
        """ Return a tuple `(R,G,B)` of the current LED brightness value (range 0..1). """
        return self._main_LED.color

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
        self._main_LED.color = (r,g,b)

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
            pass  # nothing


# Main entry poing
if __name__ == "__main__":
    # create an instance of the HSG NightLight
    nightlight = NightLight()

    # run the instance
    nightlight.run()
