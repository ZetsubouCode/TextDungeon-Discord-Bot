class Player:

  def get_by_id(id):
    ...

  def get_all():
    #TODO
    ...

  def get_by_discord_name(name):
    #TODO
    ...

  def add(inventory_id: int, job_id: int, discord_name: str, exp: int,
          level: int, add_attack: int, add_defend: int, add_eva: int):
    #TODO
    ...

  def update_by_id(target_id: int, inventory_id: int, job_id: int,
                   discord_name: str, exp: int, level: int, add_attack: int,
                   add_defend: int, add_eva: int):
    ...

  def update_by_discord_name(target_discord_name: str, inventory_id: int,
                             job_id: int, discord_name: str, exp: int,
                             level: int, add_attack: int, add_defend: int,
                             add_eva: int):
    ...
