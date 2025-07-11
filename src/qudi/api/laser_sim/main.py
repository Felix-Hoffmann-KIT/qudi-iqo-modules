from fastapi import FastAPI

from models import PowerCommand, WavelengthCommand, LaserStatus
from state import sim

app = FastAPI(title="Laser Simulation API", version="1.0")


### FastAPI Basics
# GET:    get information
# POST:   create something new
# PUT:    change something existing
# DELETE: delete something
#
# async def get_data():
#     await request
#     return {"data": "Hello World!"}

@app.get("/")
def index():
    return {"message": "Welcome to the Laser Simulation API! Please go to http://.../docs"}

@app.get("/status/", response_model=LaserStatus)
def get_status():
    return sim.read_status()

@app.post("/power/")
def set_power(cmd: PowerCommand):
    sim.set_power(cmd.on)
    return {"status": "ok", "on": sim.on}

@app.post("/wavelength/")
def set_wavelength(cmd: WavelengthCommand):
    sim.set_wavelength(cmd.wavelength_nm)
    return {"status": "ok", "wavelength": sim.wavelength_nm}

@app.get("/readback/", response_model=LaserStatus)
def readback():
    return sim.read_status()
