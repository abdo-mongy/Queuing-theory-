class StochasticQueue:

    def __init__(self, vals):
        self.mean_arrival_rate = vals['mean_arrival_rate']
        self.mean_service_rate = vals['mean_service_rate']
