"""
Generate a form diagram in static equilibrium.
"""
from ghpythonlib.componentbase import executingcomponent as component

from compas_cem import PROXY_PORT

from compas.rpc import Proxy


class ConstrainedFormFindingComponent(component):
    def RunScript(self, solve, topology, constraints, parameters, algorithm, iters_max, eps, tmax, eta):
        algorithm = algorithm or "SLSQP"
        iters_max = iters_max or 100
        eps = eps or 1e-6
        tmax = tmax or 100
        eta = eta or 1e-6

        if not (solve and topology and constraints and parameters):
            return

        topology = topology.copy()

        # clean constraints and parameters from None
        constraints = [c for c in constraints if c is not None]
        parameters = [p for p in parameters if p is not None]

        with Proxy("compas_cem.optimization", port=PROXY_PORT) as opt:
            solution = opt.solve_nlopt_proxy(topology=topology,
                                             constraints=constraints,
                                             parameters=parameters,
                                             algorithm=algorithm,
                                             iters=iters_max,
                                             eps=eps,
                                             tmax=tmax,
                                             eta=eta)

        form, objective, grad_norm, iters, time, status = solution
        return form, objective, grad_norm, iters, time, status
