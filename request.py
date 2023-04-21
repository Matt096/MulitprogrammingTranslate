class Request:

    def __init__(self, name, user, resource, duration):
        self.name = name
        self.user = user
        self.resource = resource
        self.duration = duration
        self.status = "default"
        self.waiting_time = -1

    def is_waiting(self):
        print(f"{self.name} will have to WAIT for resource {self.resource} to be AVAILABLE.")
        self.update_waiting_time()

    def in_action(self):
        print(f"{self.name} will be using the resource {self.resource} for {self.duration} second/s.")

    def is_completed(self):
        return self.status == "complete"

    def display_complete_req(self):
        if self.is_completed():
            print(f"User {self.user}'s request on resource {self.resource} has been COMPLETED.")

    def display_time(self):
        print(f"{self.name} on resource {self.resource} | Time left: {self.duration} second/s.")
        self.duration -= 1

    def update_waiting_time(self):
        self.waiting_time -= 1
