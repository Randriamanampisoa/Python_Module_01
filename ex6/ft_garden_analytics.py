#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/02 16:55:16 by fanilran            #+#    #+#            #
#   Updated: 2026/04/29 05:03:32 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    class Static:
        def __init__(self) -> None:
            self._show_up = 0
            self._grow_up = 0
            self._age_up = 0

        def increment_show(self) -> None:
            self._show_up += 1

        def increment_grow(self) -> None:
            self._grow_up += 1

        def increment_age(self) -> None:
            self._age_up += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_up} grow, "
                  f"{self._age_up} age, {self._show_up} show")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self._static = Plant.Static()

    @staticmethod
    def check(years: int) -> None:
        if years < 365:
            print(f"Is {years} days more than a year? -> False")
        else:
            print(f"Is {years} days more than a year? -> True")

    @classmethod
    def anonymous(cls) -> "Plant":
        plant = cls("Unknown plant", 0.0, 0)
        plant.show()
        plant._static.display()
        return plant

    def grow(self, value: float) -> None:
        self.height += value
        self._static.increment_grow()

    def ages(self, value: int) -> None:
        self.age += value
        self._static.increment_age()

    def get_name(self) -> str:
        return self.name

    def show(self) -> None:
        self._static.increment_show()
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, {self.age} days old")


class Tree(Plant):
    class Shade:
        def __init__(self) -> None:
            self.count = 0

        def increment(self) -> None:
            self.count += 1

        def display(self) -> None:
            print(f"{self.count} shade")
    _shade_stat = Shade()

    def __init__(self, name: str, height: float, age: int,
                 truck_diameter: float) -> None:
        super().__init__(name, height, age)
        self.truck_diameter = truck_diameter

    def produce_shade(self) -> None:
        if self.height > 0 and self.truck_diameter > 0:
            Tree._shade_stat.increment()
            print(f"Tree {self.name.capitalize()} ", end="")
            print("now produce a shade of", end="")
            print(f"{self.height: .1f}cm long", end="")
            print(f"{self.truck_diameter: .1f}cm wide")
        else:
            return

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.truck_diameter: .1f}cm")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, is_bloom: bool) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloom = is_bloom
        self._static = Plant.Static()

    def bloom(self) -> None:
        if self.is_bloom:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, is_bloom: bool):
        super().__init__(name, height, age, color, is_bloom)
        self.seed = 0

    def bloom(self) -> None:
        if self.is_bloom:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def show(self) -> None:
        super().show()

    def set_seeds(self, value: int) -> None:
        self.seed += value

    def get_seed(self) -> int:
        return self.seed


def display_statistics(plant: "Plant") -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant._static.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check(300)
    Plant.check(400)
    print("\n=== Flower")
    rose = Flower("rose", 15, 10, "red", False)
    rose.show()
    rose.bloom()
    display_statistics(rose)
    print(f"[asking the {rose.get_name()} to grow and bloom]")
    rose.grow(8)
    rose.is_bloom = True
    rose.show()
    rose.bloom()
    display_statistics(rose)

    print("\n=== Seed")
    Sunflower = Seed("sunflower", 80, 45, "yellow", False)
    Sunflower.show()
    Sunflower.bloom()
    print(f"Seeds: {Sunflower.get_seed()}")
    print(f"[make {Sunflower.get_name()} grow, age and bloom]")
    Sunflower.grow(30)
    Sunflower.ages(20)
    Sunflower.is_bloom = True
    Sunflower.set_seeds(42)
    Sunflower.show()
    Sunflower.bloom()
    print(f"Seeds: {Sunflower.get_seed()}")
    display_statistics(Sunflower)

    print("\n=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    display_statistics(oak)
    Tree._shade_stat.display()
    print(f"[asking the {oak.get_name()} to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    Tree._shade_stat.display()

    print("\n=== Anonymous")
    plant = Plant.anonymous()
    display_statistics(plant)
