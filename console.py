#!/usr/bin/python3
"""
Command interpreter for Holberton AirBnB project
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command inerpreter class"""

    def do_quit(self, line):
        print()
        return True

    def EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
