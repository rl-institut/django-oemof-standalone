from setup import init_django

OEMOF_DATAPACKAGE = "dispatch"
OEMOF_PARAMETERS = {
    "electricity_demand": 7000
}


def test_parameter_hook(scenario, parameters, request):
    parameters["demand0"] = {"amount": parameters.pop("electricity_demand")}
    return parameters


def test_model_hook(scenario, model, request):
    # Adapt model here
    return model

def test_es_hook(scenario, es, request):
    return es


if __name__ == "__main__":
    init_django()
    from django_oemof import simulation, hooks

    ph = hooks.Hook(OEMOF_DATAPACKAGE, test_parameter_hook)
    esh = hooks.Hook(OEMOF_DATAPACKAGE, test_es_hook)
    mh = hooks.Hook(OEMOF_DATAPACKAGE, test_model_hook)

    hooks.register_hook(hook_type=hooks.HookType.PARAMETER, hook=ph)
    hooks.register_hook(hook_type=hooks.HookType.ENERGYSYSTEM, hook=esh)
    hooks.register_hook(hook_type=hooks.HookType.MODEL, hook=mh)

    simulation_id = simulation.simulate_scenario(scenario=OEMOF_DATAPACKAGE, parameters=OEMOF_PARAMETERS)
    print("Simulation ID:", simulation_id)