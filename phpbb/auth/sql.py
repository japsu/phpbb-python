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

DEFAULT_PARAM_STYLE = '%s'
DEFAULT_USERS_TABLE = 'phpbb_users'

USER_ROW_FIELDS = [
    'user_id',
    'username',
    'user_password',
    'user_passchg',
    'user_pass_convert',
    'user_email',
    'user_type',
    'user_login_attempts'
]

GET_USER_ROW_SQL = 'SELECT %s FROM %s WHERE username_clean = %s'

class GetUserRow(object):
    def __init__(self, *args, **kwargs):
        self.conn = None
        self.sql = None

        if args or kwargs:
            self.setup(*args, **kwargs)

    def setup(self, conn, param_style=DEFAULT_PARAM_STYLE, users_table=DEFAULT_USERS_TABLE):
        self.conn = conn
        self.sql = GET_USER_ROW_SQL % (", ".join(USER_ROW_FIELDS), users_table, param_style)

    def is_setup(self):
        return self.conn is not None

    def __call__(self, username_clean):
        c = self.conn.cursor()
        c.execute(self.sql, [username_clean,])

        user_row = c.fetchone()

        if user_row:
            return dict(zip(USER_ROW_FIELDS, user_row))
        else:
            return None

get_user_row = GetUserRow()
setup = get_user_row.setup
is_setup = get_user_row.is_setup
