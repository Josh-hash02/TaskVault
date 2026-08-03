import random

class Character:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, amount: int):
        self.health = max(0, self.health - amount)
        print(f"{self.name} took {amount} damage! (HP: {self.health}/{self.max_health})")

    def attack(self, target: "Character"):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.take_damage(self.attack_power)

class Warrior(Character):
    def __init__(self, name: str, health: int, attack_power: int, armor: int):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def take_damage(self, amount: int):
        effective_damage = max(1, amount - self.armor)
        print(f"{self.name}'s armor absorbed {self.armor} damage!")
        super().take_damage(effective_damage)

class Mage(Character):
    def __init__(self, name: str, health: int, attack_power: int, mana: int):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def cast_spell(self, target: Character):
        mana_cost = 20
        spell_damage = self.attack_power * 2

        if self.mana >= mana_cost:
            self.mana -= mana_cost
            print(f"{self.name} casts Fireball on {target.name} for {spell_damage} damage! (Mana left: {self.mana})")
            target.take_damage(spell_damage)
        else:
            print(f"{self.name} tried to cast Fireball, but didn't have enough mana!")

class Rogue(Character):
    def __init__(self, name: str, health: int, attack_power: int, dodge_chance: float):
        super().__init__(name, health, attack_power)
        self.dodge_chance = dodge_chance

    def take_damage(self, amount: int):
        # Roll a random float between 0.0 and 1.0
        if random.random() < self.dodge_chance:
            print(f"{self.name} dodged the attack and took 0 damage!")
        else:
            super().take_damage(amount)

    def backstab(self, target: Character):
        crit_damage = self.attack_power * 3
        print(f"{self.name} executes a Backstab on {target.name} for {crit_damage} CRITICAL damage!")
        target.take_damage(crit_damage)

if __name__ == "__main__":
    print("--- ⚔️ RPG COMBAT SIMULATION ⚔️ ---\n")

    # Instantiate combatants
    conan = Warrior(name="Conan", health=100, attack_power=15, armor=5)
    gandalf = Mage(name="Gandalf", health=60, attack_power=10, mana=50)
    valeera = Rogue(name="Valeera", health=70, attack_power=12, dodge_chance=0.40)

    gandalf.cast_spell(conan)
    print()

    conan.attack(gandalf)
    print(f"Is Gandalf alive? {gandalf.is_alive()}\n")

    valeera.backstab(conan)
    print()

    print("--- Testing Rogue Dodge Mechanic (3 Attacks) ---")
    for i in range(1, 4):
        print(f"[Attack {i}]")
        conan.attack(valeera)
        print()