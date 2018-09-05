import time

import gpiozero

class ExtendedButton(gpiozero.Button):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._prev_state_time = None

    def _fire_events(self):
        old_state = self._last_state
        new_state = self._last_state = self.is_active
        if old_state is None:
            # Initial "indeterminate" state; set events but don't fire
            # callbacks as there's not necessarily an edge
            if new_state:
                self._active_event.set()
            else:
                self._inactive_event.set()
        elif old_state != new_state:
            now = time.time()
            self._prev_state_time = now - self._last_changed
            self._last_changed = now
            if new_state:
                self._inactive_event.clear()
                self._active_event.set()
                self._fire_activated()
            else:
                self._active_event.clear()
                self._inactive_event.set()
                self._fire_deactivated()

    @property
    def previous_state_time(self):
        return self._prev_state_time