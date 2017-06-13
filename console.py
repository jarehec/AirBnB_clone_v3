#!/usr/bin/python3
"""
Command interpreter for Holberton AirBnB project
"""
import cmd
from models import base_model, user, storage, CNC

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
            if arg[0] not in CNC:
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
            for k, v in CNC.items():
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
            print('[', end='')
            fs_o = FS.all()
            l = 0
            for v in fs_o.values():
                if type(v).__name__ == CNC[arg[0]].__name__:
                    l += 1
            c = 0
            for v in fs_o.values():
                if type(v).__name__ == CNC[arg[0]].__name__:
                    c += 1
                    print(v, end=(', ' if c < l else ''))
            print(']')

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

    def __rreplace(self, s, l):
        for c in l:
            s = s.replace(c, '')
        return s

    def __check_dict(self, arg):
        """checks if the arguments input has a dictionary"""
        if '{' and '}' in arg:
            l = arg.split('{')[1]
            l = l.split(', ')
            l = list(s.split(':') for s in l)
            d = {}
            for subl in l:
                k = subl[0].strip('"\' {}')
                v = subl[1].strip('"\' {}')
                d[k] = v
            return d
        else:
            return None

    def do_update(self, arg):
        """update: update [ARG] [ARG1] [ARG2] [ARG3]
        ARG = Class
        ARG1 = ID #
        ARG2 = attribute name
        ARG3 = value of new attribute
        SYNOPSIS: updates or adds a new attribute and value of given Class"""
        d = self.__check_dict(arg)
        arg = self.__rreplace(arg, [',', '"'])
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
                    if not d:
                        avalue = arg[3].strip('"')
                        if avalue.isdigit():
                            avalue = int(avalue)
                        fs_o[key].bm_update(arg[2], avalue)
                    else:
                        for k, v in d.items():
                            if v.isdigit():
                                v = int(v)
                            fs_o[key].bm_update(k, v)

    def do_BaseModel(self, arg):
        """class method with .function() syntax"""
        self.__parse_exec('BaseModel', arg)

    def do_Amenity(self, arg):
        """class method with .function() syntax"""
        self.__parse_exec('Amenity', arg)

    def do_City(self, arg):
        """class method with .function() syntax"""
        self.__parse_exec('City', arg)

    def do_Place(self, arg):
        """class method with .function() syntax"""
        self.__parse_exec('Place', arg)

    def do_Review(self, arg):
        """class method with .function() syntax"""
        self.__parse_exec('Review', arg)

    def do_State(self, arg):
        """class method with .function() syntax"""
        self.__parse_exec('State', arg)

    def do_User(self, arg):
        """class method with .function() syntax"""
        self.__parse_exec('User', arg)

    def __count(self, arg):
        args = arg.split()
        fs_o = FS.all()
        count = 0
        for k in fs_o.keys():
            if args[0] in k:
                count += 1
        print(count)

    def __parse_exec(self, c, arg):
        CMD_MATCH = {
            '.all': self.do_all,
            '.count': self.__count,
            '.show': self.do_show,
            '.destroy': self.do_destroy,
            '.update': self.do_update,
            '.create': self.do_create,
        }
        replace = ['"', ',']
        if '(' and ')' in arg:
            check = arg.split('(')
            new_arg = "{} {}".format(c, check[1][:-1])
            for k, v in CMD_MATCH.items():
                if k == check[0]:
                    if ((',' or '"' in new_arg) and k != '.update'):
                        for c in replace:
                            new_arg = new_arg.replace(c, '')
                    v(new_arg)
                    return
        self.default(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
