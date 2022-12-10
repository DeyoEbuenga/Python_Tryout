class AnimalSounds:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

class Dinasour(AnimalSounds):
    def make_sound(self):
        print("Rawr!!")

rodulph = Dinasour()
rodulph.make_sound()
# output: Rawr!!
