#!/usr/bin/python3
"""
Command interpreter for Holberton AirBnB project
"""
import cmd
from models import base_model, user, storage, CLS

BaseModel = base_model.BaseModel
User = user.User
FS = storage


class HBNBCommand(cmd.Cmd):
    """Command inerpreter class"""

    ERR = [
        '** class name missing **',
        "** class doesn't exist **",
        '** instance id missing **',
        '** no instance found **',
        '** attribute name missing **',
        '** value missing **',
        ]

    def __class_err(self, arg):
        """private: checks for missing class or unknown class"""
        error = 0
        if len(arg) == 0:
            print(HBNBCommand.ERR[0])
            error = 1
        else:
            if arg[0] not in CLS:
                print(HBNBCommand.ERR[1])
                error = 1
        return error

    def __id_err(self, arg):
        """private checks for missing ID or unknown ID"""
        error = 0
        if (len(arg) < 2):
            print(HBNBCommand.ERR[2])
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
        arg = arg.split()
        error = self.__class_err(arg)

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
        arg = arg.split()
        error = self.__class_err(arg)
        if not error:
            for k, v in CLS.items():
                if k == arg[0]:
                    my_obj = v()
                    my_obj.save()
                    print(my_obj.id)

    def do_show(self, arg):
        """show: show [ARG] [ARG1]
        ARG = Class
        ARG1 = ID #
        SYNOPSIS: Prints object of given ID from given Class"""
        arg = arg.split()
        error = self.__class_err(arg)
        if not error:
            error += self.__id_err(arg)
        if not error:
            valid_id = 0
            my_objects = FS.all()
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
        arg = arg.split()
        error = self.__class_err(arg)
        if not error:
            error += self.__id_err(arg)
        if not error:
            valid_id = 0
            my_objects = FS.all()
            for k in my_objects.keys():
                if arg[1] in k:
                    valid_id = 1
                    key = k
            if not valid_id:
                print(HBNBCommand.ERR[3])
            else:
                del my_objects[key]
                FS.save()

    def do_all(self, arg):
        """all: all [ARG]
        ARG = Class
        SYNOPSIS: prints all objects of given class"""
        arg = arg.split()
        error = self.__class_err(arg)
        if not error:
            my_objects = FS.all()
            for v in my_objects.values():
                if type(v).__name__ == CLS[arg[0]].__name__:
                    print(v)

    def do_update(self, arg):
        """update: update [ARG] [ARG1] [ARG2] [ARG3]
        ARG = Class
        ARG1 = ID #
        ARG2 = attribute name
        ARG3 = value of new attribute
        SYNOPSIS: updates or adds a new attribute and value of given Class"""
        arg = arg.split()
        error = self.__class_err(arg)
        if not error:
            error += self.__id_err(arg)
        if not error:
            valid_id = 0
            my_objects = FS.all()
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
                    if arg[2] == 'id':
                        print('** cannot update id **')
                    else:
                        value = arg[3].strip('"\'')
                        my_objects[key].update(arg[2], value)

    def default(self, line):
        """default response for unknown commands"""
        print("** unknown command **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
