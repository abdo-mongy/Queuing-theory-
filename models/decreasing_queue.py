from . import deterministic_queue
import matplotlib.pyplot as mat


class DecreasingQueue(deterministic_queue.DeterministicQueue):
    def __init__(self, vals):
        super(DecreasingQueue, self).__init__(vals)

        self.compute_s_s_time()
        self.compute_waiting_time()
        self.compute_no_of_customers_in()
        self.compute_average_waiting_time()

    def compute_no_of_customers_in(self):
        nt = []
        if self.initial_no_of_customers:
            ti = self.s_s_time
            for t in range(self.limit+2):
                if t >= ti:
                    nt.append(0)
                else:
                    nt.append(self.initial_no_of_customers + int(self.arrival_rate * t) - int(self.service_rate * t))
        self.no_of_customers_in = nt

    def compute_waiting_time(self):
        wq = []
        ti = self.s_s_time
        if self.initial_no_of_customers:
            for n in range(self.limit+2):
                if n >= int(self.arrival_rate * ti):
                    wq.append(0)
                else:
                    wq.append((self.initial_no_of_customers - 1 + n) * (1 / self.service_rate) - n *
                              (1 / self.arrival_rate))
        else:
            wq = [0]
        self.waiting_time = wq

    def compute_average_waiting_time(self):
        if self.initial_no_of_customers:
            self.average_waiting_time = (self.initial_no_of_customers - 1) / (2 * self.service_rate)

    def compute_s_s_time(self):
        for t in range(100000):
            if (int(self.service_rate * t) - int(self.arrival_rate * t)) == self.initial_no_of_customers:
                self.s_s_time = t
                break
            else:
                self.s_s_time = 0

    def graph(self):
        x = self.no_of_customers_in
        y = [i for i in range(self.limit+2)]
        mat.plot(y, x)
        mat.xlabel('x - axis')
        mat.ylabel('y - axis')
        mat.title('no of customers')
        mat.show()

        return

