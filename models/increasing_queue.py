import deterministic_queue
import matplotlib.pyplot as mat


class IncreasingQueue(deterministic_queue.DeterministicQueue):

    def __init__(self, vals):
        super(IncreasingQueue, self).__init__(vals)
        self.compute_s_s_time()
        self.compute_no_of_customers_in()
        self.compute_waiting_time()

    def compute_no_of_customers_in(self):
        no_of_customers_in = []
        for i in range(self.limit):
            if i < self.s_s_time:
                no_of_customers_in.append(
                    int(i * self.arrival_rate) - int(
                        (self.service_rate * i - self.service_rate / self.arrival_rate) + 1 / 1000000))
            else:
                no_of_customers_in.append(self.system_capacity - 1)
        self.no_of_customers_in = no_of_customers_in

    def compute_waiting_time(self):
        wq = []
        for i in range(1, self.limit):
            if self.arrival_rate * self.s_s_time > i:
                wq.append((1 / self.service_rate - 1 / self.arrival_rate) * (i - 1))
            else:
                wq.append((1 / self.service_rate - 1 / self.arrival_rate) * (self.arrival_rate * self.s_s_time - 2))
        self.waiting_time = wq

    def compute_s_s_time(self):
        for i in range(100000):
            if self.system_capacity == int(i * self.arrival_rate) - int(
                    (self.service_rate * i - self.service_rate / self.arrival_rate) + 1 / 10000000000000):
                self.s_s_time = i
                return

    def graph(self):
        x = self.no_of_customers_in
        y = [i for i in range(self.limit)]
        mat.plot(y, x)
        mat.xlabel('x - axis')
        mat.ylabel('y - axis')
        mat.title('no of customers')
        mat.show()

        return
