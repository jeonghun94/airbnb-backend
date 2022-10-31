class Human:
  def print_test(self):
    print("I'm Human");

class Player(Human):
  def __init__(self, name, age):
    self.name = name;
    self.age = age;

  def print_player(self):
    print(f"player is {self.name} and {self.age} year's old");

player = Player("jhun", 29);
player.print_player();
player.print_test();

    