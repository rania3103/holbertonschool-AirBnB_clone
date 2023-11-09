#!/usr/bin/python3
"""Write a program called console.py that contains
the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """this is the class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """exit the program"""
        return True

    def do_EOF(self, line):
        """exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def help_quit(self):
        """help quit"""
        print("Quit command to exit the program\n")

    def do_create(self, line):
        """Creates a new instance of BaseModel,saves
        it (to the JSON file) and prints the id."""
        args = line.split(" ")
        if len(line) < 1:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
            inst.save()
            print(inst.id)

    def do_show(self, line):
        """ Prints the string representation of
        an instance based on the class name and id"""
        args = line.split(" ")

        if len(line) < 1:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()
            if key not in obj_dict:
                print("** no instance found **")
            else:
                print(key)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split(" ")

        if len(line) < 1:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()
            if key not in obj_dict:
                print("** no instance found **")
            else:
                del (obj_dict[key])
                storage.save()

    def do_all(self, line):
        """Prints all string representation of
        all instances based on the class name or not"""
        args = line.split(" ")
        if len(line) == 2 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj_dict = storage.all()
            for v in obj_dict.values():
                print(v)

    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        args = line.split(" ")

        if len(line) < 1:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()
            if key not in obj_dict:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            else:
                if len(args) == 3:
                    print("** value missing **")
                else:
                    if isinstance(
                            args[3], (str, int, float)) and args[2] in [
                            "name", "my_number"]:
                        inst = obj_dict[key]
                        setattr(inst, args[2], args[3])
                        inst.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
