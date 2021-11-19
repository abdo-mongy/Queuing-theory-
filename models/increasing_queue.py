import deterministic_queue


class Increasing_queue(deterministic_queue.DeterministicQueue):

    def __init__(self, vals):
        super(Increasing_queue, self).__init__(vals)
        self.s_s_time = self.compute_s_s_time()

    def compute_no_of_customers_in(self):
        no_of_customers_in = []
        if self.initial_no_of_customers:
            for i in range(self.limit):
                if i < self.s_s_time:
                    no_of_customers_in.append(
                        int(i * self.arrival_rate) - int(
                            (self.service_rate * i - self.service_rate / self.arrival_rate) + 1 / 10000000000000))
                else:
                    no_of_customers_in.append(self.system_capacity - 1)
        else:
            no_of_customers_in = [1, 0]
        return no_of_customers_in

    def compute_waiting_time(self):
        wq = []
        for i in range(1,self.limit):
            if self.arrival_rate * self.s_s_time > i:
                wq.append((1 / self.service_rate - 1 / self.arrival_rate) * (i - 1))
            else:
                wq.append((1 / self.service_rate - 1 / self.arrival_rate) * (self.arrival_rate * self.s_s_time - 2))
        return wq

    def compute_s_s_time(self):
        ti = 500000
        for i in range(50):
            if self.system_capacity == int(i * self.arrival_rate) - int(
                    (self.service_rate * i - self.service_rate / self.arrival_rate) + 1 / 10000000000000):
                ti = min(ti, i)
        return ti
