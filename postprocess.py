from setup import init_django

OEMOF_DATAPACKAGE = "dispatch"
OEMOF_PARAMETERS = {}

if __name__ == "__main__":
    init_django()
    from django_oemof import models

    sim = models.Simulation.objects.get(id=1)
    inputs, outputs = sim.dataset.restore_results()

    # Do your stuff as usual
    print(inputs)
    print(outputs)