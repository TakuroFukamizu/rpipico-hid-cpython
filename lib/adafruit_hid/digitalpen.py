import time

from . import find_device


class Mouse:
    """Send USB HID digitalpen reports."""

    LEFT_BUTTON = 1
    """Left mouse button."""
    RIGHT_BUTTON = 2
    """Right mouse button."""
    MIDDLE_BUTTON = 4
    """Middle mouse button."""

    def __init__(self, devices):
        # 0x0d: Digitizers
        #     0x01: Digitizer
        #     0x02: Pen digitizer
        #     0x04: Touch Screen
        self._pen_device = find_device(devices, usage_page=0x0d, usage=0x02)

        # Reuse this bytearray to send mouse reports.
        # report[0] buttons pressed (LEFT, MIDDLE, RIGHT)
        # report[1] x movement
        # report[2] y movement
        # report[3] wheel movement
        self.report = bytearray(5)

        # Do a no-op to test if HID device is ready.
        # If not, wait a bit and try once more.
        # try:
        #     self._send_no_move()
        # except OSError:
        #     time.sleep(1)
        #     self._send_no_move()

    def update(self, tip, x, y):
        self.report[0] = 0x01
        self.report[1] = 0x01
        self.report[2] = 0x01
        self._pen_device.send_report(self.report)

    @staticmethod
    def _limit(dist):
        return min(127, max(-127, dist))
