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

from phpbb.utf.data import confusables

import re

OTHER_CONTROL_CHARACTERS_RE = re.compile('(?:[\x00-\x1F\x7F]+|(?:\xC2[\x80-\x9F])+)')
MULTIPLE_SPACES_RE = re.compile(' {2,}')

def utf8_clean_string(text):
    # XXX: this just isn't the same thing as utf8_case_fold_nfkc
    text = text.lower()

    text = "".join(confusables.get(i, i) for i in text)
    text = OTHER_CONTROL_CHARACTERS_RE.sub('', text)
    text = MULTIPLE_SPACES_RE.sub(' ', text)
    return text.strip()
