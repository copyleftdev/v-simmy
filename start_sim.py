from libs.VehicleEmuDriver import CarSim
import uuid
import concurrent.futures


NUM_WORKERS = 10

def fleet_swarm(sim_id):
    c = CarSim(sim_id)
    c.sim_init()

sim_ids = []
for x in range(NUM_WORKERS):
    sim_ids.append("vehicle-{}".format(uuid.uuid4()))


with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    futures = {executor.submit(fleet_swarm, sid) for sid in sim_ids}
    concurrent.futures.wait(futures)
