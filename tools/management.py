import sys
import os


class ManagementUtility:
    """
    Encapsulate the logic of the manage.py utilities.
    """
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        self.settings_exeception = None
    
    def execute(self):
        """ Given the command-line arguments, figure out which subcommand is being run,
        create a parser appropriate to that command, and run it.
        """
        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = 'help'


def execute_from_command_line(argv=None):
    """Run a MangementUtility"""
    utility = MangementUtility(argv)
    utility.execute()