#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/01 16:34:50 by fanilran            #+#    #+#            #
#   Updated: 2026/05/07 05:58:02 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}:{self.height: .1f}cm, ", end="")
        print(f"{self.age} day old")

    def get_name(self) -> str:
        return self.name

    def get_grow(self) -> float:
        return self.height


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 is_bloom: bool):
        super().__init__(name, height, age)
        self.color = color
        self.is_bloom = is_bloom

    def bloom(self) -> None:
        if self.is_bloom:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 truck_diameter: float):
        super().__init__(name, height, age)
        self.truck_diameter = truck_diameter

    def produce_shade(self) -> None:
        if self.height > 0 and self.truck_diameter > 0:
            print(f"Tree {self.name} ", end="")
            print("now produce a shade of", end="")
            print(f"{self.height: .1f}cm long", end="")
            print(f"{self.truck_diameter: .1f}cm wide.")
        else:
            return

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.truck_diameter: .1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def set_nutritional(self, value: int) -> None:
        self.nutritional_value += value

    def set_grow_and_age(self, age: int = 0) -> None:
        self.height += age * 2.1
        self.age += age
        self.set_nutritional(age)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose1 = Flower("Rose", 15, 10, "red", False)
    rose1.show()
    rose1.bloom()
    print(f"[asking the {rose1.get_name()} to bloom]")
    rose1.is_bloom = True
    rose1.show()
    rose1.bloom()

    print("\n=== Tree")
    oak1 = Tree("Oak", 200, 365, 5)
    oak1.show()
    print(f"[asking the {oak1.get_name()} to produce shade]")
    oak1.produce_shade()

    print("\n=== Vegetable")
    Vegetable1 = Vegetable("Tomato", 5, 10, "avril", 0)
    Vegetable1.show()
    print(f"[make {Vegetable1.get_name()} grow and age for 20 days]")
    Vegetable1.set_grow_and_age(20)
    Vegetable1.show()
