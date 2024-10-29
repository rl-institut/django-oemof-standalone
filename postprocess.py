from setup import init_django

OEMOF_DATAPACKAGE = "dispatch"
OEMOF_PARAMETERS = {}

if __name__ == "__main__":
    init_django()
    from django_oemof import simulation, models

    simulation_id = simulation.simulate_scenario(scenario=OEMOF_DATAPACKAGE, parameters=OEMOF_PARAMETERS)
    sim = models.Simulation.objects.get(id=simulation_id)
    inputs, outputs = sim.dataset.restore_results()

    # Do your stuff as usual
    print(inputs)
    print(outputs)