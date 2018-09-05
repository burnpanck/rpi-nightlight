
""" HSG NightLight Step 4 - Complete nightlight implementation including mobile app support

"""
# Standard-library imports
import time       # utilities to measure time

# third-party library imports
import gpiozero   # hardware abstraction of RaspberryPi's GPIOs and common connected peripherals
import BlynkLib   # interfacing with the Blynk IoT platform

# first-party imports
from nightlight import colour_constants as C   # named colour constants
from nightlight.extended_button import ExtendedButton  # a button that knows how long it has been pressed

BLYNK_AUTH = "577719804e734257959d59c796c6c493"

class NightLight:
    """ The HSG NightLight class.

    Features provided:
    - The following parameters are configurable:
      - Colour of the light when on
      - Brightness of the light when on
      - Threshold: The ambient brightness level at which the light switches on (in normal mode)
    - Mode and configuration changes trigger a notification pattern, including sound
    - The mode can be cycled with the button
    - A companion mobile app provides:
      - Remote configuration of the parameters
      - Remote display of historic ambient light levels
    """

    def __init__(self):
        """ Create an instance of the HSG NightLight. """

        # configuration of nightlight
        self._colour = C.FIREBRICK
        self._brightness = 1.
        self._threshold = 0.15
        self._mode = "normal"

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
        self._currently_on = False
        self._notification_on = False

        # initialise
        self._setup_hardware()
        self._setup_blynk()

    def _setup_hardware(self):
        """ Create instances of all peripherals needed. """
        self._main_LED = gpiozero.RGBLED(12,13,19,pwm=True)

        self._piezo = gpiozero.PWMOutputDevice(18,frequency=400)
        self._button = ExtendedButton(4,pull_up=True)

        self._pt_adc = gpiozero.MCP3008(port=0,device=0,channel=0)
        self._ldr_adc = gpiozero.MCP3008(port=0,device=0,channel=3)

        self._button.when_pressed = self._on_button_press
        self._button.when_released = self._on_button_release

    def _on_button_press(self):
        """ Event handler for Button-presses. """
        print("Button pressed")
        mode_transition_map = {
            "off": "normal",
            "normal": "on",
            "on": "off",
        }
        self.mode = mode_transition_map[self.mode]

    def _on_button_release(self, button):
        """ Event handler for Button-releases.

        Parameters:
            - button: The button instnace that was relreased
        """
        if button is not None:
            t = button.previous_state_time
            print(f"Button released after {t:.1f} s")
        else:
            print(f"Button released")

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
        mine = tuple()
        try:
            self._notification_on = mine
            for dt,light,tone in pattern:
                if self._notification_on is not mine:
                    # another notification has started and overrides this one
                    break
                self.LEDs = tuple(v/255 for v in light)
                self._piezo.value = 0.5 if tone else 0
                time.sleep(dt)
        finally:
            if self._notification_on is mine:
                # only restore non-notification state if we were the last one
                self._piezo.value = 0
                self._notification_on = None
                self._update_LEDs()

    def _update_LEDs(self):
        """ Analyse the current state and determine the appropriate LED colour."""
        if self._notification_on:
            # currently, a notification sequence is running, so we're not responsible for LEDs
            return
        b = self.brightness
        amb = self.ambient_brightness
        if self._mode == "normal":
            on = amb < self._threshold
        elif self._mode == "off":
            on = False
        elif self._mode == "on":
            on = True
        else:
            raise ValueError(f'Unknown mode "{self._mode}"')
        print(f'Ambient={amb*100:.1f} %, threshold={100*self._threshold:.1f} %, mode="{self._mode}" => on={on} (colour={self._colour}, brightness={self._brightness})')
        self._currently_on = on
        if not on:
            # when off, simply set brightness to zero
            b = 0
        self.LEDs = tuple(b*v/255 for v in self.colour)

    @property
    def ambient_brightness(self):
        return self._ldr_adc.value

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

    def _setup_blynk(self):
        blynk = self._blynk = BlynkLib.Blynk(BLYNK_AUTH)

        @blynk.VIRTUAL_WRITE(0)
        def set_button(val):
            val = int(val)
            print(f'set_button({repr(val)})')
            if val:
                self._on_button_press()
            else:
                self._on_button_release()

        @blynk.VIRTUAL_WRITE(4)
        def set_mode(mode):
            print(f'set_mode({repr(mode)})')
            mode = ["off","normal","on"][int(mode)-1]
            self.mode = mode

        @blynk.VIRTUAL_WRITE(5)
        def set_colour(colour_idx):
            colour_list = [
                C.BLUE,
                C.DEEPSKYBLUE1,
                C.GOLD1,
                C.CRIMSON,
                C.DARKOLIVEGREEN1,
                C.DARKORCHID,
            ]
            colour = colour_list[int(colour_idx)-1]
            print(f'set_colour({colour_idx} = {colour})')
            self.colour = colour

        @blynk.VIRTUAL_WRITE(6)
        def set_brightness(brightness):
            brightness = float(brightness)
            print(f'set_brightness({repr(brightness)})')
            self.brightness = brightness

        @blynk.VIRTUAL_WRITE(7)
        def set_threshold(threshold):
            threshold = float(threshold)/100
            print(f'set_threshold({repr(threshold)})')
            self.threshold = threshold

        @blynk.on_connect
        def on_connect():
            print('Connected to Blynk')

        blynk.set_user_task(self.one_pass, 250)

    def one_pass(self):
        self._blynk.virtual_write(1,self.ambient_brightness)
        self._blynk.virtual_write(2,self._currently_on)
        self._update_LEDs()

    def run_blynk(self):
        """ Run the main loop, periodically checking for events, with support for Blynk.

        This function only exits at device shutdown.
        """
        self._blynk.run()

    def run_standalone(self):
        """ Run the main loop, periodically checking for events, no support for Blynk.

        This function only exits at device shutdown.
        """
        tlast = time.monotonic()
        while True:
            tnow = time.monotonic()
            twait = max(0,tlast+1-tnow)
            if twait>0:
                time.sleep(twait)
            tlast = tnow+twait
            self.one_pass()

# Main entry poing
if __name__ == "__main__":
    # create an instance of the HSG NightLight
    nightlight = NightLight()

    # run the instance
    nightlight.run_standalone()
