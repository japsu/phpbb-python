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

from phpbb.auth.auth_db import login_db

class PhpbbBackend:
    def authenticate(self, username=None, password=None):
        if username is None or password is None:
            return None

        status, user_row = login_db(username, password)
        if status != "LOGIN_SUCCESS":
            return None

        user, created = User.objects.get_or_create(
            username=user_row["username_clean"],
            email=user_row.get("user_email", None)
        )

        return user

