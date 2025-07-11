class LaserSimulator:
    def __init__(self):
        self.on = False
        self.wavelength_nm = 532.0  # default: grüner Laser
        self.power_mw = 0.0

    def set_power(self, state: bool):
        self.on = state
        self.power_mw = 10.0 if state else 0.0

    def set_wavelength(self, wl: float):
        self.wavelength_nm = wl

    def read_status(self):
        return {
            "on": self.on,
            "wavelength_nm": self.wavelength_nm,
            "power_mw": self.power_mw,
        }

sim = LaserSimulator()
