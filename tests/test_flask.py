# Imports
import os
import tempfile

import pytest

from personal_site import personal_site


@pytest.fixture
def client():
    #db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    personal_site.app.config['TESTING'] = True
    client = personal_site.app.test_client()

    #with app.app_context():
    #    app.init_db()

    yield client

    #os.close(db_fd)
    #os.unlink(app.config['DATABASE'])