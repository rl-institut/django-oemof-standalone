import logging
from oemof.solph.buses import Bus


def remove_component_by_name(es, component_name):
    """Remove a component and its reference from an EnergySystem instance

    :param es: solph.EnergySystem
    :param component_name: str the unique name of the component
    :return: None
    """

    # remove component from _groups if component name key exists
    component = es._groups.pop(component_name, None)
    if component is not None:
        logging.info(f"Removing {component_name} from energy system")
        # remove component from _nodes
        es._nodes.pop(es.nodes.index(component))

        component_is_bus = isinstance(component, Bus)
        cascade_removal = (
            []
        )  # for other components linked to the component which need to also be removed

        # find possible component inputs and output and remove any existing connexion stored
        outputs = [o for o in component.outputs]
        inputs = [i for i in component.inputs]
        # clear the outputs of the component's inputs
        if inputs:

            for i in inputs:
                if component_is_bus is True:
                    if i.label not in cascade_removal:
                        cascade_removal.append(i.label)
                else:
                    i.outputs.pop(component)
        # clear the inputs of the component's outputs
        if outputs:
            for o in outputs:
                if component_is_bus is True:
                    if o.label not in cascade_removal:
                        cascade_removal.append(o.label)
                else:
                    o.inputs.pop(component)

        # look into special groups if the component appear and removes in case it does
        for k, group in es.groups.items():
            if not isinstance(k, str):
                if len(group) > 0:
                    element_to_remove = []
                    # group elements can be tuples of component instance or directly component instances
                    for e in group:
                        if isinstance(e, tuple):
                            if component in e:
                                element_to_remove.append(e)
                        else:
                            if e == component:
                                element_to_remove.append(e)
                    if element_to_remove:
                        logging.debug(
                            f"The following elements will be removed from group {k}"
                        )
                        logging.debug(element_to_remove)
                    else:
                        logging.debug(f"Nothing to remove in group {k}")
                    for e in element_to_remove:
                        group.remove(e)

        if cascade_removal:
            logging.info(
                f"{component_name} is now removed from energy system. The following component also need to be removed: {','.join(cascade_removal)}"
            )
            remove_components(es, cascade_removal)
        else:
            logging.info(f"Removed {component_name} from energy system")


def remove_components(es, components_to_remove):
    """Remove several components and their references from an EnergySystem instance

    :param es: solph.EnergySystem
    :param component_name: list[str] the unique names of the components
    :return: None
    """
    for component_name in components_to_remove:
        remove_component_by_name(es, component_name)

    # remove dangling busses
    busses = [c for c in es.nodes if isinstance(c, Bus)]
    for bus in busses:
        if len(bus.inputs) + len(bus.outputs) == 0:
            # remove the dangling bus
            logging.info(f"Removed bus {bus.label} as it had no inputs nor outputs")
            remove_component_by_name(es, bus.label)
