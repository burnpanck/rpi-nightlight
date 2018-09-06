
""" HSG NightLight Step 4 - Complete nightlight implementation

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
    - The following parameters are configurable:
      - Colour of the light when on
      - Brightness of the light when on
      - Threshold: The ambient brightness level at which the light switches on (in normal mode)
    - Mode and configuration changes trigger a notification pattern, including sound
    - The mode can be cycled with the button
    - A button press-hold resets the threshold to the current ambient brightness
    """

    def __init__(self):
        """ Create an instance of the HSG NightLight. """

        # configuration of nightlight
        self._colour = C.FIREBRICK
        self._brightness = 1.
        self._threshold = 0.15
        self._mode = "normal"

        # audio-visual notification patterns:
        # each entry is a tuple (time, light, tone) describing the duration of the entry
        # what colour to show and if the buzzer should make some noise
        self._configuration_changed_pattern = [
            (0.2, C.BLUE, True),
        ]
        self._mode_changed_pattern = {
            "off": [
                (0.5, C.FIREBRICK, True),
                (1.0, C.FIREBRICK, False),
            ],
            "normal": [
                (0.3, C.GREEN, True),
                (0.4, C.BLACK, False),
                (0.3, C.GREEN, False),
            ],
            "on": [
                (0.5, C.WHITE, True),
            ],
        }

        # state of nightlight
        self._keep_running = True
        self._currently_on = False
        self._notification_on = False

        # initialise
        self._setup_hardware()

    def _setup_hardware(self):
        """ Create instances of all peripherals needed. """
        self._main_LED = ... # TODO: create your RGB LED instance here

        # TODO: ensure that the correct GPIO pin is used for the piezo
        self._piezo = gpiozero.PWMOutputDevice(18,frequency=400)

        self._sensor_adc = ... # TODO: Create an instance of a

        # TODO: ensure that the correct GPIO pin is used for the button
        self._button = gpiozero.Button(4,hold_time=3,hold_repeat=False,pull_up=True)
        self._button.when_pressed = self._on_button_press
        self._button.when_released = self._on_button_release
        self._button.when_held = self._on_button_hold

    def _on_button_press(self):
        """ Event handler, called when the button is pressed. """
        print("Button was pressed")
        # TODO: make a mode change, such that all three modes "off","normal","on" can be reached

    def _on_button_release(self):
        """ Event handler, called when the button is released """
        print("Button was released")
        # nothing left to do
        pass

    def _on_button_hold(self):
        """ Event handler, called when the button is held for a long time. """
        print(f"Long button press detected -> resetting threshold")
        # TODO: assign the current ambient level as threshold value

    @property
    def LEDs(self):
        """ Return a tuple `(R,G,B)` of the current LED brightness value (range 0..1). """
        return self._main_LED.color

    @LEDs.setter
    def LEDs(self, value):
        """ Set the LED brightness value to the given `(r,g,b)` tuple. """
        if isinstance(value, (tuple, list)):
            r,g,b = value
        else:
            r = g = b = value
#        print(f"Setting LEDs to {100*r:.0f}/{100*g:.0f}/{100*b:.0f}")
        self._main_LED.color = (r,g,b)


    def _notification(self,pattern):
        """ Start a notification pattern.

        A notification is a sequence of colors and tones.

        If another notification is still active, it will be cancelled and replaced by this one.
        The pattern is specified as a list of tuples `(dt,light,tone)`,
        where `dt` is the time in seconds of each phase in the pattern,
        `light` is an RGB tuple for the light colour, and `tone` is a boolean indicating if the piezo speaker
        should be active in this phase.
        """
        # indicate that we're currently notifying and the LEDs are under our control
        self._notfication_on = True
        # TODO: cycle trough the lights and tones in time intervals as given
        # give control over LEDs back to main program
        self._notfication_on = False

    def _update_LEDs(self):
        """ Analyse the current state and determine the appropriate LED colour."""
        on = ... # TODO: determine if the LEDs should be on (depends on mode, ambient level and threshold).
        self._currently_on = on
        if self._notification_on:
            # currently, a notification sequence is running, so we're not responsible for LEDs
            return
        print(f'Ambient={amb*100:.1f} %, threshold={100*self._threshold:.1f} %, mode="{self._mode}" => on={on} (colour={self._colour}, brightness={self._brightness})')
        # when off, simply set brightness to zero
        v = self.brightness if on else 0
        r,g,b =  self.colour
        self.LEDs = v*r, v*g, v*b

    @property
    def ambient_brightness(self):
        # TODO: read ambient sensor value
        pass

    @property
    def brightness(self):
        return self._brightness
    @brightness.setter
    def brightness(self, b):
        self._brightness = b
        self._configuration_changed()

    @property
    def colour(self):
        return self._colour
    @colour.setter
    def colour(self, c):
        self._colour = c
        self._configuration_changed()

    @property
    def threshold(self):
        return self._threshold
    @threshold.setter
    def threshold(self, t):
        self._threshold = t
        self._configuration_changed()

    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self,mode):
        self._mode = mode
        self._notification(self._mode_changed_pattern[mode])
        self._update_LEDs()

    def _configuration_changed(self):
        self._notification(self._configuration_changed_pattern)

    def one_pass(self):
        self._update_LEDs()

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

            self.one_pass()

        # we're stopping, do some cleanup

        # switch off all LEDs!
        self._main_LED.off()
        print("Leaving main loop")

# Main entry point
if __name__ == "__main__":
    # create an instance of the HSG NightLight
    nightlight = NightLight()

    # run the instance
    nightlight.run()
