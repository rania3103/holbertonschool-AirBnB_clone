#!/usr/bin/python3
"""Write a program called console.py that contains
the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """this is the class"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """exit the program"""
        return True

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_emptyline(self, line):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def help_quit(self):
        """help quit"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
