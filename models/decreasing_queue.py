import deterministic_queue


class DecreasingQueue(deterministic_queue.DeterministicQueue):
    def __init__(self, vals):
        super(DecreasingQueue, self).__init__(vals)

    def compute_no_of_customers_in(self):
        if self.initial_no_of_customers:
            nt = []
            for i in range(10):
                nt.append()

    def compute_waiting_time(self):
        wq = []
        if self.initial_no_of_customers:
            for n in range(10):
                wq.append((self.initial_no_of_customers - 1 + n) * (1 / self.service_rate) - n * (1 / self.arrival_rate))
        else:
            wq = [0,1]


    def compute_average_waiting_time(self):
        if self.initial_no_of_customers:
            return (self.initial_no_of_customers - 1) / (2 * self.service_rate)

    def compute_s_s_time(self):
        pass


