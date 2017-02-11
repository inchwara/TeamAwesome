"""
A program to track personal learning progress when going through any learning program (like boot camp).
 Made with love by TeamAwesome
Usage:
    learning_map add  <skill>
    learning_map view [--studied] [--todo]
    learning_map show_progress
    learning_map (-h | --help)
"""
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


class LearningTracker(cmd.Cmd, dict):
    intro = 'A Program to track personal learning progress when going through any learning program (like boot camp)\n'
    prompt = '(learning_map)'

    def __init__(self):
        super(LearningTracker, self).__init__()

    @docopt_cmd
    def do_add(self, arg):
        """Usage: add <skill> """

        self[arg["<skill>"]] = False

        print(arg)

    @docopt_cmd
    def do_view(self, arg):
        """Usage: view [--studied] [--todo]
        """
        if arg["--studied"]:
            for i in self:
                if self[i] == True:
                    print(i)
        elif arg["--todo"]:

            for i in self:
                if self[i] == False:
                    print(i)
        else:
            for i in self:
                print(i)
                # print(arg)

    def do_show_progress(self, arg):
        count = 0
        for i in self:
            if self[i] == True:
                count = count + 1
        print("Out of " + str(len(self)) + "skills, you have completed " + str(count))

    def do_quit(self, arg):

        print('See you next time!')
        exit()


def main():
    LearningTracker().cmdloop()


if __name__ == '__main__':
    main()