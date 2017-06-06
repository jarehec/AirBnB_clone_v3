#!/usr/bin/python3
"""Command interpreter for Holberton AirBnB project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command inerpreter class"""
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_quit(self, line):
        """quit
        Command to quit the program
        """

        return True

    def do_EOF(self, line):
        """function to handle EOF"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
