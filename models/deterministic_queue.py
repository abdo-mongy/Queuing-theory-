class DeterministicQueue():

    def __init__(self, vals):
        self.arrival_rate = vals['arrival_rate']
        self.service_rate = vals['service_rate']
        self.s_s_time = vals['s_s_time']
        self.no_of_customers_in = vals['no_of_customers_in']
        self.waiting_time = vals['waiting_time']
        self.average_waiting_time = vals['average_waiting_time']
        self.initial_no_of_customers = vals['initial_no_of_customers']
        self.system_capacity = vals['system_capacity']
        self.limit = vals['limit']
