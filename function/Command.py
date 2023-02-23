class Command:
    def guide():
        return """

                """

    def command_list():
        return "**COMMAND LIST**\n>>> !start => Start the game\n!help => Show all possible command\n!menu => Show all main menu option\n"\
                "!history => Check all run history\n!exit => Exit from the run and save it\n!surrender => Force to finish the current run if any\n"\
                "#inventory => Check items in inventory\n"\
                "!gallery => Show List of all character with the lore description"
                

    def main_menu():
        return """!start\n!gallery\n!history\n!exit
        
        """
    