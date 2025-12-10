import random


def main():
    print("────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")
    print("࿔‧ ֶָ֢˚˖𐦍˖˚ֶָ֢ ‧࿔  WELCOME TO THIS FANTASY WORD!  ࿔‧ ֶָ֢˚˖𐦍˖˚ֶָ֢ ‧࿔")
    print("WHEN YOU ENTERED THIS WORLD YOU FORGOT WHO YOU ARE...")
    Q = input("WOULD YOU LIKE TO FIND OUT WHO YOU ARE AND WHAT YOUR STORY IS? ")
    print("THERE'S ALSO A CUTE LITTLE SURPRISE AT THE END (˶˃ ᵕ ˂˶) ")
       
    if(Q== "yes" or "YES"):
        print("RECALLING MEMORIES IS NOT EASY, GIVE IT A MINUTE...")
        print("࿓࿓༄༄ WOOSH ࿓࿓༄༄")
        print("────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")
        build_character() 
    else:
        print("aw :( why do you not what to know who you are?")

    R = input("\t  WHAT WOULD YOU RATE THIS EXPERIENCE OUT OF FIVE? ")
    if(R== "5" or R== "4" ):
        print("𐙚 𝓽𝓱𝓪𝓷𝓴𝓼 𝓼𝓸 𝓶𝓾𝓬𝓱, 𝓱𝓪𝓿𝓮 𝓪 𝓵𝓸𝓿𝓮𝓵𝔂 𝓭𝓪𝔂𝔂! 𐙚")
    else:
        print("aw :(  , maybe you can create another version of yourself that you would like more.")



def build_character():
    names = ["JUDE", "CARDAN", "ORAYA", "EVANGELINE", "JACKS", "HERMIONE", "DONATELLA", "ACHILLES", "PAEDYN", "NYX"]
    races  = ["WITCH", "WARRIOR", "ROUGE", "HUMAN", "GOD", "VAMPIRE", "MAGE", "GOBLIN", "DWARF", "ELF"]
    abilities = ["INVISIBILITY", "FIREBALL", "HEALING", "POISON", "SHAPESHIFTING", "ALCHEMY", "FLIGHT", "ILLUSION", "TELEKINESIS", "CONJURATION"]
    weapons = ["SWORD", "STAFF", "BOW", "AXE", "DAGGER", "KATANA", "SPEAR", "HAMMER", "WHIP", "THROWING STARS"]

    name = random.choice(names)
    race = random.choice(races)
    ability = random.choice(abilities)
    weapon = random.choice(weapons)
    character = {"NAME": name, "RACE": race, "ABILITY": ability, "WEAPON": weapon }
    from ai import call_gpt
    backstory = call_gpt(f"create a small backstory for the given {character}, also give a beautiful and text art of the {character} with a closing statement but do not specify that it is a closing statement ")
    characters = {"NAME": name, "RACE": race, "ABILITY": ability, "WEAPON": weapon, "BACKSTORY": backstory}
    for key, value in characters.items():
      print (f"{key}: {value}")
  


if __name__ == "__main__":
    main()
