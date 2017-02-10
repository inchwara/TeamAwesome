"""
A program to track personal learning progress when going through any learning program (like boot camp).
 Made with love by TeamAwesome

Usage:
    learning_map add  <skill>
    learning_map view [--studied] [--todo] 
    learning_map show-progress
    learning_map (-h | --help)


"""

import sys
import cmd
from docopt import docopt, DocoptExit

def docopt_cmd(func):
    """
    This decorator describes the annotation @docopt_cmd
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        return func(self, opt)

    # replaces fn attributes with those of annotated function
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class LearningTracker (cmd.Cmd):
    intro = 'A Program to track personal learning progress when going through any learning program (like boot camp)\n'
    prompt = '(learning_map)'
    
    @docopt_cmd
    def do_add(self, arg):
        """Usage: add <skill> """

        print(arg)

    @docopt_cmd
    def do_view(self, arg):
        """Usage: view [--studied] [--todo] 

        """
        if arg["--studied"]:
        	if not self.skills is None:
        		for i in skills:
        			if skills[i] == True:
        				print(i)
        elif arg["--todo"]:
        	if not self.skills is None:
        		for i in skills:
        			if skills[i] == False:
        				print(i)
        else:
        	if not self.skills is None:
        		for i in skills:
        			print (i)

    
    def do_quit(self, arg):

        print('See you next time!')
        exit()

def main():
	LearningTracker().cmdloop()

if __name__ == '__main__':
	main()