from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# -----------------------------
# SAMPLE DATA
# -----------------------------

depots = [
    {
        "id": 1,
        "name": "Central Depot",
        "location": "Chennai"
    },
    {
        "id": 2,
        "name": "North Depot",
        "location": "Bangalore"
    }
]


vehicles = [
    {
        "id": 1,
        "vehicle_number": "TN01AB1234",
        "depot_id": 1,
        "downtime_cost_per_day": 1000,
        "estimated_duration_hours": 3
    },
    {
        "id": 2,
        "vehicle_number": "TN02CD5678",
        "depot_id": 1,
        "downtime_cost_per_day": 2000,
        "estimated_duration_hours": 4
    },
    {
        "id": 3,
        "vehicle_number": "KA03EF9999",
        "depot_id": 2,
        "downtime_cost_per_day": 1500,
        "estimated_duration_hours": 2
    }
]


# -----------------------------
# PYDANTIC MODEL
# -----------------------------

class Vehicle(BaseModel):
    vehicle_number: str
    depot_id: int
    downtime_cost_per_day: int
    estimated_duration_hours: int


# -----------------------------
# HOME ROUTE
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Vehicle Maintenance Scheduler API Running"
    }


# -----------------------------
# GET DEPOTS
# -----------------------------

@app.get("/depots")
def get_depots():
    return depots


# -----------------------------
# GET VEHICLES
# -----------------------------

@app.get("/vehicles")
def get_vehicles():
    return vehicles


# -----------------------------
# ADD VEHICLE
# -----------------------------

@app.post("/vehicles")
def add_vehicle(vehicle: Vehicle):

    new_vehicle = {
        "id": len(vehicles) + 1,
        "vehicle_number": vehicle.vehicle_number,
        "depot_id": vehicle.depot_id,
        "downtime_cost_per_day": vehicle.downtime_cost_per_day,
        "estimated_duration_hours": vehicle.estimated_duration_hours
    }

    vehicles.append(new_vehicle)

    return {
        "message": "Vehicle added successfully",
        "vehicle": new_vehicle
    }


# -----------------------------
# SCHEDULE TASKS
# -----------------------------

@app.get("/schedule")
def schedule_tasks():

    mechanic_hours = 8

    selected_tasks = []

    total_duration = 0
    total_impact = 0

    sorted_vehicles = sorted(
        vehicles,
        key=lambda x: x["downtime_cost_per_day"],
        reverse=True
    )

    for vehicle in sorted_vehicles:

        duration = vehicle["estimated_duration_hours"]

        if total_duration + duration <= mechanic_hours:

            selected_tasks.append(vehicle)

            total_duration += duration

            total_impact += vehicle["downtime_cost_per_day"]

    return {
        "mechanic_hours": mechanic_hours,
        "total_selected_duration": total_duration,
        "total_impact": total_impact,
        "selected_tasks": selected_tasks
    }