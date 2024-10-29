from setup import init_django

OEMOF_DATAPACKAGE = "dispatch"
OEMOF_PARAMETERS = {}

if __name__ == "__main__":
    init_django()
    from django_oemof import simulation

    simulation_id = simulation.simulate_scenario(scenario=OEMOF_DATAPACKAGE, parameters=OEMOF_PARAMETERS)
    print("Simulation ID:", simulation_id)