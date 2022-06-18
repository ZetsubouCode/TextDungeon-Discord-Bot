from ..controller.Player import Player as PlayerController
from ..controller.Job import Job as JobController
from ..controller.Inventory import Inventory as InventoryController

class StartGame:
    def start_game(discord_name:str):
        job = JobController.add()
        data = PlayerController.add(job.id)
        inventory = InventoryController.add()
