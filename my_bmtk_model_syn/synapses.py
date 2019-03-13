from bmtk.simulator.bionet.pyfunction_cache import add_synapse_model
from neuron import h

def InhSyn(syn_params, sec_x, sec_id):
    """Create a inhsyn synapse
    :param syn_params: parameters of a synapse
    :param sec_x: normalized distance along the section
    :param sec_id: target section
    :return: NEURON synapse object
    """

    lsyn = h.inhsyn(sec_x, sec=sec_id)

    if syn_params.get('esyn'):
        lsyn.esyn = float(syn_params['esyn'])
    if syn_params.get('gmax'):
        lsyn.gmax = float(syn_params['gmax'])
		
    return lsyn

def inhsyn(syn_params, xs, secs):
    """Create a list of inhsyn synapses
    :param syn_params: parameters of a synapse
    :param xs: list of normalized distances along the section
    :param secs: target sections
    :return: list of NEURON synpase objects
    """
    syns = []
    for x, sec in zip(xs, secs):
        syn = InhSyn(syn_params, x, sec)
        syns.append(syn)
    return syns

def load():
    add_synapse_model(InhSyn, 'inhsyn', overwrite=False)
    add_synapse_model(InhSyn, overwrite=False)
    return
