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
    INSTANCES = {'BaseModel': storage}

    def __init__(self):
        """Instantiation for hbnb class"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_airbnb(self, arg):
        print('** you found my test **')
        print(arg)

    def do_quit(self, line):
        """quit
        Command to quit the program
        """
        return True

    def do_EOF(self, line):
        """function to handle EOF"""
        print()
        return True

    def do_create(self, arg):
        if arg == '':
            print("** class doesn't exist **")
        elif arg not in CLASSES:
            print("** class name missing **")
        else:
            for k, v in CLASSES.items():
                if k == arg:
                    my_obj = v()
                    my_obj.save()
                    print(my_obj.id)

    def do_show(self, arg):
        exists = 0
        if arg == '':
            print('** class name missing **')
        else:
            arg = arg.split()
            if (len(arg) < 2):
                print('** instance id missing **')
            elif arg[0] not in HBNBCommand.CLASSES:
                print("** class doesn't exist **")
            else:
                my_objects = HBNBCommand.INSTANCES[arg[0]].all()
                for k in my_objects.keys():
                    if arg[1] in k:
                        exists = 1
                if exists:
                    for k, v in my_objects.items():
                        if arg[1] in k:
                            print(v)
                else:
                    print('** no instance found **')

    def do_destroy(self, arg):
        exists = 0
        if arg == '':
            print('** class name missing **')
        else:
            arg = arg.split()
            if (len(arg) < 2):
                print('** instance id missing **')
            elif arg[0] not in HBNBCommand.CLASSES:
                print("** class doesn't exist **")
            else:
                my_objects = HBNBCommand.INSTANCES[arg[0]].all()
                for k in my_objects.keys():
                    if arg[1] in k:
                        exists = 1
                        key = k
                if exists:
                    storage.delete(key)
                else:
                    print('** no instance found **')

    def do_all(self, arg):
        exists = 0
        if arg == '' or arg not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        else:
            my_objects = HBNBCommand.INSTANCES[arg].all()
            for v in my_objects.values():
                print(v)

    def do_update(self, arg):
        print(arg)

    def default(self, line):
        print("** command doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
