from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from models import MMckQueue, MM1Queue, MM1K, MMcQueue, increasing_queue, decreasing_queue, deterministic_queue
from PyQt5.uic import loadUiType
import urllib.request

import os
from os import path

ui, _ = loadUiType('views/untitled.ui')


class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_buttons()

    def handle_buttons(self):

        self.cancel_sto.clicked.connect(self.close)
        self.compute_stochastic_queue.clicked.connect(self.compute_stochastic_out)
        self.cancel.clicked.connect(self.close)
        self.compute_deterministic.clicked.connect(self.comput_determenstic)
        self.make_graph.clicked.connect(self.graph)

    def prepare_stochastic_vals(self):
        try:
            model = str(self.comboBox_7.currentText())
            if model == "MM1":
                try:
                    arrival_rate = float(self.mean_arrival_rate.text())
                    service_rate = float(self.mean_service_rate.text())
                    if arrival_rate <= 0 or service_rate <= 0:
                        return
                    # system_capacity = int(self.system_capacity.text())
                    # no_of_servers = int(self.no_of_servers.text())
                    vals = {
                        'mean_arrival_rate': arrival_rate,
                        'mean_service_rate': service_rate,
                    }
                    return ["MM1", vals]
                except:
                    pass

            elif model == "MM1k":
                try:
                    arrival_rate = float(self.mean_arrival_rate.text())
                    service_rate = float(self.mean_service_rate.text())
                    system_capacity = int(self.system_capacity.text())
                    if arrival_rate <= 0 or service_rate <= 0 or system_capacity <= 0:
                        return
                    vals = {
                        'mean_arrival_rate': arrival_rate,
                        'mean_service_rate': service_rate,
                        'buffer': system_capacity,
                    }
                    return ["MM1k", vals]
                except:
                    pass

            elif model == "MMc":
                try:
                    arrival_rate = float(self.mean_arrival_rate.text())
                    service_rate = float(self.mean_service_rate.text())
                    no_of_servers = int(self.no_of_servers.text())
                    if no_of_servers <= 0 or arrival_rate <= 0 or service_rate <= 0:
                        return
                    vals = {
                        'mean_arrival_rate': arrival_rate,
                        'mean_service_rate': service_rate,
                        'no_of_servers': no_of_servers,
                    }
                    return ["MMc", vals]
                except:
                    pass
            else:
                try:
                    arrival_rate = float(self.mean_arrival_rate.text())
                    service_rate = float(self.mean_service_rate.text())
                    no_of_servers = int(self.no_of_servers.text())
                    system_capacity = int(self.system_capacity.text())
                    if system_capacity <= 0 or no_of_servers <= 0 or arrival_rate <= 0 or service_rate <= 0:
                        return
                    vals = {
                        'mean_arrival_rate': arrival_rate,
                        'mean_service_rate': service_rate,
                        'no_of_servers': no_of_servers,
                        'system_capacity': system_capacity,
                    }
                    return ["MMck", vals]
                except:
                    pass
        except:
            pass

    def compute_stochastic_out(self):
        try:
            model, vals = self.prepare_stochastic_vals()
            if model == "MMck":
                queue = MMckQueue.MMckQueue(vals)
            elif model == "MMc":
                queue = MMcQueue.MMcQueue(vals)
            elif model == "MM1k":
                queue = MM1K.MM1k(vals)
            else:
                queue = MM1Queue.MM1Queue(vals)
            if model == "MM1k":
                self.av_no_of_customers_in_q.setText(str(queue.ex_no_of_customers_in_queu))
                self.av_no_of_customers_in_system.setText(str(queue.no_of_customers))
                self.av_waiting_time_in_q.setText(str(queue.ex_waiting_time_in_queue))
                self.av_waiting_time_in_system.setText(str(queue.ex_waiting_time))
            else:
                self.av_no_of_customers_in_q.setText(str(queue.expected_no_of_customers_in_queue))
                self.av_no_of_customers_in_system.setText(str(queue.expected_no_of_customers))
                self.av_waiting_time_in_q.setText(str(queue.expected_waiting_time_in_queue))
                self.av_waiting_time_in_system.setText(str(queue.expected_waiting_time))
        except:
            pass

    def prepare_detrmanstic_vals(self):
        try:
            model = str(self.comboBox.currentText())
            arrival = float(self.input_arrival_rate.text())
            service = float(self.input_service_rate.text())
            system_capacity = int(self.input_capcity.text())
            intial_no = int(self.input_intial_no_of_customers.text())
            lim = int(self.input_limit.text())
            if arrival <= 0 or service <= 0 or intial_no < 0 or system_capacity < 0 or lim < 0:
                return
            vals = {
                'arrival_rate': arrival,
                'service_rate': service,
                'initial_no_of_customers': intial_no,
                'system_capacity': system_capacity + 1,
                'limit': lim
            }
            if arrival > service:
                return ["increasing_queue", vals]
            else:
                return ["decreasing_queue", vals]
        except:
            pass

    def comput_determenstic(self):
        model, vals = self.prepare_detrmanstic_vals()
        if model == "decreasing_queue":
            queue = decreasing_queue.DecreasingQueue(vals)
            self.no_of_customers.setText(str(queue.no_of_customers_in))
            self.waiting_time.setText(str(queue.waiting_time))
        else:
            queue = increasing_queue.IncreasingQueue(vals)
            self.no_of_customers.setText(str(queue.no_of_customers_in))
            self.waiting_time.setText(str(queue.waiting_time))

    def graph(self):
        try:
            model, vals = self.prepare_detrmanstic_vals()
            if model == "decreasing_queue":
                queue = decreasing_queue.DecreasingQueue(vals)
                queue.graph()
            else:
                queue = increasing_queue.IncreasingQueue(vals)
                queue.graph()
        except:
            pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
