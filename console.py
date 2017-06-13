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
    prompt = '(hbnb) '
    ERR = [
        '** class name missing **',
        "** class doesn't exist **",
        '** instance id missing **',
        '** no instance found **',
        '** attribute name missing **',
        '** value missing **',
        ]

    def default(self, line):
        """default response for unknown commands"""
        print("** unknown command **")

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

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
            fs_o = FS.all()
            for k in fs_o.keys():
                if arg[1] in k:
                    valid_id = 1
            if not valid_id:
                print(HBNBCommand.ERR[3])
            else:
                for k, v in fs_o.items():
                    if arg[1] in k:
                        print(v)

    def do_all(self, arg):
        """all: all [ARG]
        ARG = Class
        SYNOPSIS: prints all objects of given class"""
        arg = arg.split()
        error = self.__class_err(arg)
        if not error:
            fs_o = FS.all()
            for v in fs_o.values():
                if type(v).__name__ == CLS[arg[0]].__name__:
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
            fs_o = FS.all()
            for k in fs_o.keys():
                if arg[1] in k:
                    valid_id = 1
                    key = k
            if not valid_id:
                print(HBNBCommand.ERR[3])
            else:
                del fs_o[key]
                FS.save()

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
            fs_o = FS.all()
            for k in fs_o.keys():
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
                        fs_o[key].bm_update(arg[2], value)

    def do_BaseModel(self, args):
        """class method with .function() syntax"""
        self.__parse_exec('BaseModel', args)

    def do_Amenity(self, args):
        """class method with .function() syntax"""
        self.__parse_exec('Amenity', args)

    def do_City(self, args):
        """class method with .function() syntax"""
        self.__parse_exec('City', args)

    def do_Place(self, args):
        """class method with .function() syntax"""
        self.__parse_exec('Place', args)

    def do_Review(self, args):
        """class method with .function() syntax"""
        self.__parse_exec('Review', args)

    def do_State(self, args):
        """class method with .function() syntax"""
        self.__parse_exec('State', args)

    def do_User(self, args):
        """class method with .function() syntax"""
        self.__parse_exec('User', args)

    def __count(self, args):
        args = args.split()
        fs_o = FS.all()
        count = 0
        for k in fs_o.keys():
            if args[0] in k:
                count += 1
        print(count)

    def __parse_exec(self, c, args):
        CMD_MATCH = {
            '.all': self.do_all,
            '.count': self.__count,
            '.show': self.do_show,
            '.destroy': self.do_destroy,
            '.update': self.do_update
        }
        replace = ['"', ',']
        check = args.split('(')
        for k, v in CMD_MATCH.items():
            if k == check[0]:
                new_arg = "{} {}".format(c, check[1][:-1])
                if ',' or '"' in new_arg:
                    for c in replace:
                        new_arg = new_arg.replace(c, '')
                v(new_arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
