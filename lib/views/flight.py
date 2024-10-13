from typing import Optional, Any
from pydantic import BaseModel
from lib.models.flight import Flight
from lib.views.rocket import RocketView, RocketSummary
from lib.views.environment import EnvSummary
from lib.utils import to_python_primitive


class FlightSummary(RocketSummary, EnvSummary):
    # TODO: implement {flight_id}/summary/motor; {flight_id}/summary/rocket; {flight_id}/summary/environment
    name: Optional[str]
    max_time: Optional[int]
    min_time_step: Optional[int]
    max_time_step: Optional[Any]
    equations_of_motion: Optional[str]
    heading: Optional[int]
    inclination: Optional[int]
    initial_solution: Optional[list]
    effective_1rl: Optional[float]
    effective_2rl: Optional[float]
    out_of_rail_time: Optional[float]
    out_of_rail_time_index: Optional[int]
    parachute_cd_s: Optional[float]
    rail_length: Optional[float]
    rtol: Optional[float]
    t: Optional[float]
    t_final: Optional[float]
    t_initial: Optional[int]
    terminate_on_apogee: Optional[bool]
    time_overshoot: Optional[bool]
    latitude: Optional[Any]
    longitude: Optional[Any]
    M1: Optional[Any]
    M2: Optional[Any]
    M3: Optional[Any]
    R1: Optional[Any]
    R2: Optional[Any]
    R3: Optional[Any]
    acceleration: Optional[Any]
    aerodynamic_bending_moment: Optional[Any]
    aerodynamic_drag: Optional[Any]
    aerodynamic_lift: Optional[Any]
    aerodynamic_spin_moment: Optional[Any]
    alpha1: Optional[Any]
    alpha2: Optional[Any]
    alpha3: Optional[Any]
    altitude: Optional[Any]
    angle_of_attack: Optional[Any]
    apogee: Optional[Any]
    apogee_freestream_speed: Optional[Any]
    apogee_state: Optional[Any]
    apogee_time: Optional[Any]
    apogee_x: Optional[Any]
    apogee_y: Optional[Any]
    atol: Optional[Any]
    attitude_angle: Optional[Any]
    attitude_frequency_response: Optional[Any]
    attitude_vector_x: Optional[Any]
    attitude_vector_y: Optional[Any]
    attitude_vector_z: Optional[Any]
    ax: Optional[Any]
    ay: Optional[Any]
    az: Optional[Any]
    bearing: Optional[Any]
    drag_power: Optional[Any]
    drift: Optional[Any]
    dynamic_pressure: Optional[Any]
    e0: Optional[Any]
    e1: Optional[Any]
    e2: Optional[Any]
    e3: Optional[Any]
    free_stream_speed: Optional[Any]
    frontal_surface_wind: Optional[Any]
    function_evaluations: Optional[Any]
    function_evaluations_per_time_step: Optional[Any]
    horizontal_speed: Optional[Any]
    impact_state: Optional[Any]
    impact_velocity: Optional[Any]
    initial_stability_margin: Optional[Any]
    kinetic_energy: Optional[Any]
    lateral_attitude_angle: Optional[Any]
    lateral_surface_wind: Optional[Any]
    mach_number: Optional[Any]
    max_acceleration: Optional[Any]
    max_acceleration_power_off: Optional[Any]
    max_acceleration_power_off_time: Optional[Any]
    max_acceleration_power_on: Optional[Any]
    max_acceleration_power_on_time: Optional[Any]
    max_acceleration_time: Optional[Any]
    max_dynamic_pressure: Optional[Any]
    max_dynamic_pressure_time: Optional[Any]
    max_mach_number: Optional[Any]
    max_mach_number_time: Optional[Any]
    max_rail_button1_normal_force: Optional[Any]
    max_rail_button1_shear_force: Optional[Any]
    max_rail_button2_normal_force: Optional[Any]
    max_rail_button2_shear_force: Optional[Any]
    max_reynolds_number: Optional[Any]
    max_reynolds_number_time: Optional[Any]
    max_speed: Optional[Any]
    max_speed_time: Optional[Any]
    max_stability_margin: Optional[Any]
    max_stability_margin_time: Optional[Any]
    max_total_pressure: Optional[Any]
    max_total_pressure_time: Optional[Any]
    min_stability_margin: Optional[Any]
    min_stability_margin_time: Optional[Any]
    omega1_frequency_response: Optional[Any]
    omega2_frequency_response: Optional[Any]
    omega3_frequency_response: Optional[Any]
    out_of_rail_stability_margin: Optional[Any]
    out_of_rail_state: Optional[Any]
    out_of_rail_velocity: Optional[Any]
    parachute_events: Optional[Any]
    path_angle: Optional[Any]
    phi: Optional[Any]
    potential_energy: Optional[Any]
    psi: Optional[Any]
    rail_button1_normal_force: Optional[Any]
    rail_button1_shear_force: Optional[Any]
    rail_button2_normal_force: Optional[Any]
    rail_button2_shear_force: Optional[Any]
    reynolds_number: Optional[Any]
    rotational_energy: Optional[Any]
    solution: Optional[Any]
    solution_array: Optional[Any]
    speed: Optional[Any]
    stability_margin: Optional[Any]
    static_margin: Optional[Any]
    stream_velocity_x: Optional[Any]
    stream_velocity_y: Optional[Any]
    stream_velocity_z: Optional[Any]
    theta: Optional[Any]
    thrust_power: Optional[Any]
    time: Optional[Any]
    time_steps: Optional[Any]
    total_energy: Optional[Any]
    total_pressure: Optional[Any]
    translational_energy: Optional[Any]
    vx: Optional[Any]
    vy: Optional[Any]
    vz: Optional[Any]
    w1: Optional[Any]
    w2: Optional[Any]
    w3: Optional[Any]
    x: Optional[Any]
    x_impact: Optional[Any]
    y: Optional[Any]
    y_impact: Optional[Any]
    y_sol: Optional[Any]
    z: Optional[Any]
    z_impact: Optional[Any]
    flight_phases: Optional[Any]

    class Config:
        json_encoders = {Any: to_python_primitive}


class FlightCreated(BaseModel):
    flight_id: str
    message: str = "Flight successfully created"


class FlightUpdated(BaseModel):
    flight_id: str
    message: str = "Flight successfully updated"


class FlightDeleted(BaseModel):
    flight_id: str
    message: str = "Flight successfully deleted"


class FlightView(Flight):
    rocket: RocketView
