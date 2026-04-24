from alchemy.grimoire.dark_spellbook import dark_spell_record

# Circular import : dark_spellbook -> dark_validator -> dark_spellbook
if __name__ == "__main__":

    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")

    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    result = dark_spell_record("Dark Ritual", "bats and frogs")

    print(result)
