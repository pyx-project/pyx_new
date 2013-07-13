# -*- encoding: utf-8 -*-
#
#
# Copyright (C) 2013 Jörg Lehmann <joergl@users.sourceforge.net>
# Copyright (C) 2013 André Wobst <wobsta@users.sourceforge.net>
#
# This file is part of PyX (http://pyx.sourceforge.net/).
#
# PyX is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# PyX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyX; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

class writer:

    def __init__(self, file, encoding="ascii"):
        self.file = file
        self.encoding = encoding

    def write(self, s):
        self.file.write(s.encode(self.encoding))

    def write_bytes(self, b):
        self.file.write(b)

    def tell(self):
        return self.file.tell()

    def close(self):
        self.file.close()