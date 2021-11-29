import stochastic_queue


class MM1k(stochastic_queue.StochasticQueue):

    def __init__(self, vals):
        super(MM1k, self).__init__(vals)
        self.traffic_intensity = (self.mean_arrival_rate / self.mean_service_rate)
        self.buffers=vals["buffer"]
        self.p=vals["p"]
        self.no_of_customers=vals["no_of_customrs"]
        self.ex_no_of_customers_in_queu=vals["ex_no_of_customers_in_queu"]
        self.ex_waiting_time=vals["ex_waiting_time"]
        self.ex_waiting_time_in_queue=vals["ex_waiting_time_in_queue"]
        self.compute_ex_no_of_customers()
        self.compute_ex_no_of_customers_in_queue()
        self.compute_ex_waiting_time()
        self.compute_ex_waiting_time_in_queue()
        self.compute_p()

    def compute_ex_no_of_customers(self):
        if self.traffic_intensity == 1:
            ans= self.buffers /2
        else:
            ans = self.traffic_intensity*((1- (self.buffers+1) * pow(self.traffic_intensity,self.buffers) + (self.buffers * pow(self.traffic_intensity,self.buffers+1)))/((1-self.traffic_intensity) * (1-pow(self.traffic_intensity,self.buffers+1 ))))
        self.no_of_customers=ans

    def compute_p(self):
        if self.traffic_intensity==1:
            self.p=(1/(self.buffers +1))
        else:
            self.p=pow(self.traffic_intensity,self.buffers)*((1-self.traffic_intensity) /(1-pow(self.traffic_intensity,self.buffers+1)))

    def compute_ex_no_of_customers_in_queue(self):
        self.ex_no_of_customers_in_queu=self.no_of_customers-(self.traffic_intensity*(1-self.p))

    def compute_ex_waiting_time(self):
        self.ex_waiting_time=((self.no_of_customers) / ((self.mean_arrival_rate) * (1-self.p)))

    def compute_ex_waiting_time_in_queue(self):
       self.ex_waiting_time_in_queue= self.ex_waiting_time-(1/self.mean_service_rate)







