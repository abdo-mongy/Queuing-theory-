import stochastic_queue
import math


class MMckQueue(stochastic_queue.StochasticQueue):

    def __init__(self, vals):
        super(MMckQueue, self).__init__(vals)
        self.r = (self.mean_arrival_rate / self.mean_service_rate)
        self.no_of_servers = vals['no_of_servers']
        self.system_capacity = vals['system_capacity']
        self.traffic_intensity = (self.r / self.no_of_servers)
        self.p_note = self.compute_p_note()
        self.p_k = self.compute_p_k()
        self.accepted_mean_arrival_rate = self.mean_arrival_rate * (1 - self.p_k)
        self.expected_no_of_customers = None
        self.expected_no_of_customers_in_queue = None
        self.expected_waiting_time = None
        self.expected_waiting_time_in_queue = None
        self.compute_ex_no_of_customers_in_queue()
        self.compute_ex_no_of_customers()
        self.compute_ex_waiting_time()
        self.compute_ex_waiting_time_in_queue()

    def compute_p_note(self):
        if self.traffic_intensity == 1:
            segma = 0
            for n in range(self.no_of_servers):
                segma += ((self.r ** n) / math.factorial(n))
            return 1 / (segma + ((self.system_capacity - self.no_of_servers + 1) * (
                        self.r ** self.no_of_servers) / math.factorial(self.no_of_servers)))
        else:
            segma = 0
            for n in range(self.no_of_servers):
                segma += ((self.r ** n) / math.factorial(n))
            return 1 / (segma + ((1 - self.traffic_intensity ** (self.system_capacity - self.no_of_servers + 1) / (
                        1 - self.traffic_intensity)) * (
                                         self.r ** self.no_of_servers) / math.factorial(self.no_of_servers)))

    def compute_p_k(self):
        return ((self.r ** self.system_capacity) * self.p_note) / (
                    math.factorial(self.no_of_servers) * self.no_of_servers ** (
                        self.system_capacity - self.no_of_servers))

    def compute_ex_no_of_customers_in_queue(self):
        self.expected_no_of_customers_in_queue = (1 - self.traffic_intensity ** (
                    self.system_capacity - self.no_of_servers + 1) - (1 - self.traffic_intensity) *
                                                  (self.system_capacity - self.no_of_servers + 1) *
                                                  self.traffic_intensity **
                                                  (self.system_capacity - self.no_of_servers)) * \
                                                  (self.traffic_intensity * self.r ** self.no_of_servers * self.p_note)\
                                                  / (math.factorial(self.no_of_servers) *
                                                     (1 - self.traffic_intensity) ** 2)

    def compute_ex_no_of_customers(self):
        segma = 0
        for n in range(self.no_of_servers):
            segma += (self.no_of_servers - n) * (self.r ** n) / math.factorial(n)
        self.expected_no_of_customers = \
            self.expected_no_of_customers_in_queue + self.no_of_servers - segma * self.p_note

    def compute_ex_waiting_time(self):
        self.expected_waiting_time = self.expected_no_of_customers / self.accepted_mean_arrival_rate

    def compute_ex_waiting_time_in_queue(self):
        self.expected_waiting_time_in_queue = self.expected_no_of_customers_in_queue / self.accepted_mean_arrival_rate
