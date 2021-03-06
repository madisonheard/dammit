from unittest import TestCase

from nose.plugins.attrib import attr
import os
import stat

from dammit.app import DammitApp
from dammit import dependencies

from utils import TemporaryDirectory, TestData, runscript


PATH_BACKUP = os.environ['PATH']

def run(args, **kwargs):
    return runscript('dammit', args, **kwargs)


class TestDammitApp(TestCase):

    def test_dammit_version(self):
        '''Test the dammit --version command.
        '''

        from dammit import __version__
        status, out, err = run(['--version'])
        self.assertEquals(status, 0)
        self.assertEquals(err.strip(), 'dammit {0}'.format(__version__))
