from . import deterministic_queue


class D_D_1(deterministic_queue.DeterministicQueue):

    def compute_lambda(self):
        print("lambda")


