import random
from user import User
from program import Program


def random_number(bound):
    return random.randint(1, bound)


user_count = random_number(30)
users = [User(i + 1) for i in range(user_count)]
resource_count = random_number(30)

print("Number of Users:", user_count)
print("Number of Available Resources:", resource_count)
print()

for i, user in enumerate(users):
    req_count = random_number(resource_count)
    reqs = []

    taken_resource = set()

    for _ in range(req_count):
        resource = random_number(resource_count)
        time_length = random_number(30)

        while resource in taken_resource:
            resource = random_number(resource_count)

        reqs.append(user.create_request(resource, time_length))
        taken_resource.add(resource)

    user.set_user_requests(reqs)

    if i == 0:
        print("--- Initializing users and resources ---")
        print()

    user.display_user_detail()
    user.display_requested_resources()

print()
program = Program(users)

program.display_in_action()
print("P R O G R A M | S I M U L A T I O N ")
print()

program.display_program_flow()
