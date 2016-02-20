import os
import sys
from django.core.management import BaseCommand, call_command


# based on: http://stackoverflow.com/a/15080780/145349
class Command(BaseCommand):

    def transfer_stdin_to_tempfile(self):
        content = sys.stdin.read()
        outfile = open('temp.json', 'w')
        outfile.write(content)
        outfile.close()
        return outfile.name

    def handle(self, *args, **options):
        tempfile_name = self.transfer_stdin_to_tempfile()
        call_command('loaddata', tempfile_name, traceback=True)
        os.remove(tempfile_name)
