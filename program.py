class Program:

    def __init__(self, users):
        self.users = users
        self.request_sequence = []
        self.set_request_sequence()

    def set_request_sequence(self):
        curr_reqs = set()
        idx = 0
        max_size = self.get_max_size()

        while idx < max_size:
            for user in self.users:
                if idx < len(user.user_requests):
                    req = user.user_requests[idx]
                    if not curr_reqs or req.resource not in curr_reqs:
                        curr_reqs.add(req.resource)
                        req.status = "in action"
                    else:
                        req.status = "in waiting"
                    self.request_sequence.append(req)
            idx += 1

    def get_max_size(self):
        return max(len(user.user_requests) for user in self.users)

    def display_in_action(self):
        is_waiting = False
        for req in self.request_sequence:
            if req.status == "in action":
                req.in_action()
            else:
                is_waiting = True
        if is_waiting:
            print("The rest of the requests will have to wait for other resources to be available.")
        print()

    def display_program_flow(self):
        while self.request_sequence:
            for i in range(len(self.users)):
                if i < len(self.request_sequence):
                    req = self.request_sequence[i]
                    if req.status == "in action":
                        if req.duration > 0:
                            req.display_time()
                        else:
                            req.status = "complete"
                            req.display_complete_req()
                            self.request_sequence.remove(req)
                    elif req.status == "in waiting":
                        req.is_waiting()
                        if req.waiting_time == 0:
                            req.status = "in action"
            print("__________________________________________________")
            print()
