class Dog:
    energy = "high"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak()

jk_growling = Dog()
jk_growling.energy = "low"
print(jk_growling.energy)
jk_growling.speak()