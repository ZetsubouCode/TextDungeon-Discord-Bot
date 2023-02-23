class TextFormatter:
    def character_select(data):

        words = "Choose a character : "
        for character in data:
            words+=f"\n{character.id}. {character.name}"
        return words

