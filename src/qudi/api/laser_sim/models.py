from enum import IntEnum
from typing import List, Optional

from pydantic import BaseModel, Field

class PowerCommand(BaseModel):
    on: bool = Field(..., description="True = Laser an, False = aus")

class WavelengthCommand(BaseModel):
    wavelength_nm: float = Field(..., gt=400, lt=1100, description="Wellenlänge in nm")

class LaserStatus(BaseModel):
    on: bool
    wavelength_nm: float
    power_mw: float