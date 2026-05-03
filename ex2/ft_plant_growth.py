#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 01:07:00 by fanilran            #+#    #+#            #
#   Updated: 2026/04/29 01:34:46 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}:{self.height: .1f}cm, {self.age} days old")

    def grow(self, increment: float = 0.8) -> float:
        self.height += increment
        return self.height

    def ages(self) -> int:
        self.age += 1
        return self.age


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    for i in range(7):
        rose.ages()
        rose.grow()
        print(f"=== Day {i + 1} ===")
        rose.show()
    print("Growth this week: 5.6cm")
