class DeterministicQueue():

    def __init__(self, vals):

        self.arrival_rate = vals['arrival_rate']
        self.service_rate = vals['service_rate']
        self.initial_no_of_customers = vals['initial_no_of_customers']
        self.system_capacity = vals['system_capacity']
        self.limit = vals['limit']
        self.s_s_time = None
        self.no_of_customers_in = None
        self.waiting_time = None
        self.average_waiting_time = None
