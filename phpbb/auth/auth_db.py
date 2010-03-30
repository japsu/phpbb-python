# encoding: utf-8
# vim: shiftwidth=4 expandtab
#
# phpbb-python © Copyright 2010 Santtu Pajukanta
# http://pajukanta.fi
# 
# phpBB3 © Copyright 2000, 2002, 2005, 2007 phpBB Group
# http://www.phpbb.com
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

from phpbb.auth.sql import get_user_row
from phpbb.utf.utf_tools import utf8_clean_string
from phpbb.functions import phpbb_check_hash
from phpbb.constants import USER_INACTIVE, USER_IGNORE

def login_db(username=None, password=None):
    if not username:
        return "NO_USERNAME_SUPPLIED", None

    if not password:
        return "NO_PASSWORD_SUPPLIED", None

    if type(username) is unicode:
        username = username.encode("UTF-8")

    user_row = get_user_row(utf8_clean_string(username))
    if not user_row:
        return "LOGIN_ERROR_USERNAME", None

    if phpbb_check_hash(password, user_row["user_password"]):
        if user_row["user_type"] in (USER_INACTIVE, USER_IGNORE):
            return "LOGIN_ERROR_ACTIVE", user_row

        return "LOGIN_SUCCESS", user_row

    return "LOGIN_ERROR_PASSWORD", user_row

