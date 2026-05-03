#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_intro.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 00:41:53 by fanilran            #+#    #+#            #
#   Updated: 2026/05/02 23:08:24 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print("=== Welcome to My Garden")
        print(f"Plant: {self.name}")
        print(f"Height: {self.height}cm")
        print(f"Age: {self.age} days")
        print("\n=== End of Program ===")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.show()
