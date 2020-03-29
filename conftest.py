# Uncomment the following lines to display the version number of the
# package rather than the version number of Astropy in the top line when
# running the tests.

import os

import pytest
from _pytest.doctest import DoctestItem


@pytest.fixture(autouse=True)
def _docdir(request):
    """
    Make sure that doctests run in a temporary directory so that any files that
    are created as part of the test get removed automatically.
    """

    # Trigger ONLY for the doctests.
    if isinstance(request.node, DoctestItem):

        # Get the fixture dynamically by its name.
        tmpdir = request.getfixturevalue('tmpdir')

        # Chdir only for the duration of the test.
        olddir = os.getcwd()
        tmpdir.chdir()
        yield
        os.chdir(olddir)

    else:
        # For normal tests, we have to yield, since this is a yield-fixture.
        yield