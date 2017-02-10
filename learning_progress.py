"""
This is a commandline application for tracking learning progress. Made with love by TeamAwesome
Usage:
    learning_map add  <code>
    learning_map view [--studied] [--todo]
    learning_map studied
    learning_map not_studied


"""

import sys
import cmd
from docopt import docopt


class LearningTracker (cmd.Cmd):
    intro = 'Add Skill'
    prompt = '(learning_map) '


    def do_add(self, arg):
        """Usage: add <code> """

        print(arg)

    def do_view(self, arg):
        """Usage: view <port>

        """

        print(arg)

    def do_quit(self, arg):

        print('See you next time!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--tracker']:
    LearningTracker().cmdloop()

print(opt)