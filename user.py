from request import Request


class User:

    def __init__(self, user_id):
        self.id = user_id
        self.user_requests = []

    def create_request(self, resource, duration):
        return Request(f"User {self.id}", self.id, resource, duration)

    def set_user_requests(self, requests):
        self.user_requests = requests

    def display_user_detail(self):
        print(f"User {self.id} has {len(self.user_requests)} resource request/s.")

    def display_requested_resources(self):
        print("Requested resource/s:", " ".join(str(req.resource) for req in self.user_requests))
