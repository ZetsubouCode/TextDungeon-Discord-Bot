from controller.Player import Player as PlayerController
# from controller.Job import Job as JobController
# from controller.Inventory import Inventory as InventoryController

class StartGame:
    async def start_game(client, message):
        await message.channel.send('Choose a character : \n1. Raden Mandala\n2. Indrayani\n3. Raider\n4. Maling')

        def check(m):
            option=['1','2','3','4']
            return m.content in option and m.channel == message.channel and m.author == message.author
        try:
            msg = await client.wait_for("message", check=check,timeout=60)
            
        except Exception as e:
            print("time out!")
        # job = JobController.add()
        # data = PlayerController.add(job.id)
        # inventory = InventoryController.add()
