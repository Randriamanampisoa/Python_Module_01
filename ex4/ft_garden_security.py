#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 01:50:23 by fanilran            #+#    #+#            #
#   Updated: 2026/05/02 23:16:08 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"Plant created: {self._name}:{self._height: .1f}cm, "
              f"{self._age} days old\n")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Age update rejected")
        else:
            self._height = new_height

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def show_up(self) -> None:
        print(f"Current state: {self._name}:{self._height: .1f}cm, "
              f"{self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 1, 10)
    rose.show()
    rose.set_height(25)
    print(f"Height update: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()
    rose.set_height(-25)
    rose.set_age(-30)
    print()
    rose.show_up()
