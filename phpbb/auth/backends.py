# encoding: utf-8
# vim: shiftwidth=4 expandtab
#
# phpbb-python © Copyright 2010 Santtu Pajukanta
# http://pajukanta.fi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://opensource.org/licenses/gpl-license.php>.
#

from django.contrib.auth.models import User
from django.conf import settings

from phpbb.auth.auth_db import login_db
from phpbb.auth.sql import setup, is_setup

def connect_to_database():
    if is_setup():
        return

    db_module = __import__(settings.PHPBB_AUTH_DB_MODULE, globals(), locals(), [], -1)
    conn = db_module.connect(**settings.PHPBB_AUTH_DB_PARAMS)
    setup(conn)

class PhpbbBackend(object):
    def __init__(self):
        connect_to_database()

    def authenticate(self, username=None, password=None):
        if username is None or password is None:
            return None

        status, user_row = login_db(username, password)
        if status != "LOGIN_SUCCESS":
            return None

        user, created = User.objects.get_or_create(
            username=user_row["username"],
            email=user_row.get("user_email", None)
        )

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesDotExist:
            return None
