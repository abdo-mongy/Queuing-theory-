from . import stochastic_queue


class MM1Queue(stochastic_queue.StochasticQueue):

    def __init__(self, vals):
        super(MM1Queue, self).__init__(vals)
        self.traffic_intensity = (self.mean_arrival_rate / self.mean_service_rate)
        self.expected_no_of_customers = None
        self.expected_no_of_customers_in_queue = None
        self.expected_waiting_time = None
        self.expected_waiting_time_in_queue = None
        self.compute_ex_no_of_customers()
        self.compute_ex_no_of_customers_in_queue()
        self.compute_ex_waiting_time()
        self.compute_ex_waiting_time_in_queue()

    def compute_ex_no_of_customers(self):
        self.expected_no_of_customers = self.mean_arrival_rate/(self.mean_service_rate - self.mean_arrival_rate)

    def compute_ex_no_of_customers_in_queue(self):
        self.expected_no_of_customers_in_queue = self.expected_no_of_customers * \
                                                 (self.mean_arrival_rate / self.mean_service_rate)

    def compute_ex_waiting_time(self):
        self.expected_waiting_time = 1/(self.mean_service_rate - self.mean_arrival_rate)

    def compute_ex_waiting_time_in_queue(self):
        self.expected_waiting_time_in_queue = self.expected_waiting_time * \
                                              (self.mean_arrival_rate / self.mean_service_rate)
