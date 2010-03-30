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

from hashlib import md5

ITOA64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def raw_md5(*args):
    m = md5()
    for i in args:
        m.update(i)
    return m.digest()

def hex_md5(*args):
    m = md5()
    for i in args:
        m.update(i)
    return m.hexdigest()

def phpbb_check_hash(password, password_hash):
    if len(password_hash) == 34:
        return hash_crypt_private(password, password_hash) == password_hash

    return hex_md5(password) == password_hash

def hash_encode64(raw_hash, count, itoa64=ITOA64):
    output = ''
    i = 0

    while True:
        value = ord(raw_hash[i])
        i += 1

        output += itoa64[value & 0x3f]

        if i < count:
            value |= ord(raw_hash[i]) << 8

        output += itoa64[(value >> 6) & 0x3f]

        i += 1
        if i >= count:
            break

        if i < count:
            value |= ord(raw_hash[i]) << 16

        output += itoa64[(value >> 12) & 0x3f]

        i += 1
        if i >= count:
            break

        output += itoa64[(value >> 18) & 0x3f]

        if not i < count:
            break

    return output

def hash_crypt_private(password, setting, itoa64=ITOA64):
    output = '*'

    if setting[0:0+3] != '$H$':
        return output

    count_log2 = itoa64.find(setting[3])
    if count_log2 < 7 or count_log2 > 30:
        return output

    count = 1 << count_log2
    salt = setting[4:4+8]

    if len(salt) != 8:
        return output

    raw_hash = raw_md5(salt, password)
    for i in xrange(count):
        raw_hash = raw_md5(raw_hash, password)
    
    output = setting[0:0+12]
    output += hash_encode64(raw_hash, 16, itoa64)
    
    return output
