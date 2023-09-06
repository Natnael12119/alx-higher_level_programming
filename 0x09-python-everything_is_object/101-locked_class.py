#!/usr/bin/python3

class LockedClass:
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Can't create attribute {name}")
