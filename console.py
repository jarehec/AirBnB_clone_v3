#!/usr/bin/python3
"""Command interpreter for Holberton AirBnB project
"""
import cmd
import models

BaseModel = models.base_model.BaseModel
storage = models.storage


class HBNBCommand(cmd.Cmd):
    """Command inerpreter class"""

    CLASSES = {'BaseModel': BaseModel}
    FS = {'BaseModel': storage}
    ERR = [
        "** class doesn't exist **",
        '** class name missing **',
        '** instance id missing **',
        '** no instance found **',
        '** attribute name missing **',
        '** value missing **',
        ]

    def __has_err(self, arg):
        error = 0
        if arg == '':
            print(HBNBCommand.ERR[1])
            error = 1
        else:
            arg = arg.split()
            if (len(arg) < 2):
                print(HBNBCommand.ERR[2])
                error = 1
            elif arg[0] not in HBNBCommand.CLASSES:
                print(HBNBCommand.ERR[0])
                error = 1
        return error

    def __init__(self):
        """Instantiation for hbnb class"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_airbnb(self, arg):
        """airbnb: airbnb
        SYNOPSIS: Command to print arguments"""
        print('** you found my test **')
        error = self.__has_err(arg)

    def do_quit(self, line):
        """quit: quit
        USAGE: Command to quit the program
        """
        return True

    def do_EOF(self, line):
        """function to handle EOF"""
        print()
        return True

    def do_create(self, arg):
        """create: create [ARG]
        ARG = Class Name
        SYNOPSIS: Creates a new instance of the Class from given input ARG"""
        if arg == '':
            print(HBNBCommand.ERR[0])
        elif arg not in CLASSES:
            print(HBNBCommand.ERR[1])
        else:
            for k, v in CLASSES.items():
                if k == arg:
                    my_obj = v()
                    my_obj.save()
                    print(my_obj.id)

    def do_show(self, arg):
        """show: show [ARG] [ARG1]
        ARG = Class
        ARG1 = ID #
        SYNOPSIS: Prints object of given ID from given Class"""
        error = self.__has_err(arg)
        if not error:
            valid_id = 0
            arg = arg.split()
            my_objects = HBNBCommand.FS[arg[0]].all()
            for k in my_objects.keys():
                if arg[1] in k:
                    valid_id = 1
            if not valid_id:
                print(HBNBCommand.ERR[3])
            else:
                for k, v in my_objects.items():
                    if arg[1] in k:
                        print(v)

    def do_destroy(self, arg):
        """destroy: destroy [ARG] [ARG1]
        ARG = Class
        ARG1 = ID #
        SYNOPSIS: destroys object of given ID from given Class"""
        error = self.__has_err(arg)
        if not error:
            valid_id = 0
            arg = arg.split()
            my_objects = HBNBCommand.FS[arg[0]].all()
            for k in my_objects.keys():
                if arg[1] in k:
                    valid_id = 1
                    key = k
            if not valid_id:
                print(HBNBCommand.ERR[3])
            else:
                del my_objects[key]
                HBNBCommand.FS[arg[0]].save()

    def do_all(self, arg):
        """all: all [ARG]
        ARG = Class
        SYNOPSIS: prints all objects of given class"""
        if arg == '':
            print(HBNBCommand.ERR[1])
        elif arg not in HBNBCommand.CLASSES:
            print(HBNBCommand.ERR[0])
        else:
            my_objects = HBNBCommand.FS[arg].all()
            for v in my_objects.values():
                print(v)

    def do_update(self, arg):
        """destroy: destroy [ARG] [ARG1] [ARG2] [ARG3]
        ARG = Class
        ARG1 = ID #
        ARG2 = attribute name
        ARG3 = value of new attribute
        SYNOPSIS: updates or adds a new attribute and value of given Class"""
        error = self.__has_err(arg)
        if not error:
            valid_id = 0
            arg = arg.split()
            my_objects = HBNBCommand.FS[arg[0]].all()
            for k in my_objects.keys():
                if arg[1] in k:
                    valid_id = 1
                    key = k
            if not valid_id:
                print(HBNBCommand.ERR[3])
            else:
                if len(arg) < 3:
                    print(HBNBCommand.ERR[4])
                elif len(arg) < 4:
                    print(HBNBCommand.ERR[5])
                else:
                    setattr(my_objects[key], arg[2], arg[3].strip('"\''))
                    HBNBCommand.FS[arg[0]].save()

    def default(self, line):
        """default response for unknown commands"""
        print("** unknown command **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
