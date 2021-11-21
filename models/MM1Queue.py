import stochastic_queue


class MM1Queue(stochastic_queue.StochasticQueue):

    def __init__(self, vals):
        super(MM1Queue, self).__init__(vals)
        self.mean_arrival_rate = vals['arrival_rate']
        self.mean_service_rate = vals['service_rate']
        self.traffic_intensity = (self.mean_arrival_rate / self.mean_service_rate)
        self.compute_ex_no_of_customers()
        self.compute_ex_no_of_customers_in_queue()
        self.compute_ex_waiting_time()
        self.compute_ex_waiting_time_in_queue()

