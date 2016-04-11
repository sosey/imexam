"""Licensed under a 3-clause BSD style license - see LICENSE.rst."""

from __future__ import print_function, division, absolute_import

from imexam.xpa import xpa
import sys


class XPA(xpa):
    """Interface with the xpa for ds9."""

    def __init__(self, template):
        xpa.__init__(self, template.encode('utf-8'))

    def get(self, param=None):
        """Get information from the xpa."""
        if int(sys.version[0]) < 3:
            r = xpa.get(self, param.encode('utf-8'))
            return r.decode()
        else:
            return xpa.get(self, param.encode('utf-8')).decode()

    def set(self, param=None, buf=None):
        """send information to the xpa."""
        xpa.set(self, param.encode(), buf)

    def nslookup(self):
        """Return a list of access point ids."""
        return xpa.nslookup()
