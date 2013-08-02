# -*- encoding: utf-8 -*-
#
#
# Copyright (C) 2011-2012 Jörg Lehmann <joergl@users.sourceforge.net>
# Copyright (C) 2011-2012 André Wobst <wobsta@users.sourceforge.net>
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

import subprocess

class _marker: pass


class wait_pipe:

    def __init__(self, pipe, wait):
        self.pipe = pipe
        self.wait = wait

    def write(self, str):
        self.pipe.write(str)

    def close(self):
        self.pipe.close()
        self.wait()

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.close()


def popen(cmd, mode="r", bufsize=_marker):
    if mode[0] not in "rw" or "r" in mode[1:] or "w" in mode[1:]:
        raise ValueError("read or write mode expected")
    if mode[0] == "r":
        kwargs = {"stdout": subprocess.PIPE}
    else:
        kwargs = {"stdin": subprocess.PIPE}
    if bufsize is not _marker:
        kwargs["bufsize"] = bufsize
    pipes = subprocess.Popen(cmd, **kwargs)
    if mode[0] == "r":
        return pipes.stdout
    else:
        return wait_pipe(pipes.stdin, pipes.wait)

def popen2(cmd, mode="t", bufsize=_marker):
    kwargs = {"stdin": subprocess.PIPE,
              "stdout": subprocess.PIPE}
    if bufsize is not _marker:
        kwargs["bufsize"] = bufsize
    pipes = subprocess.Popen(cmd, **kwargs)
    return pipes.stdin, pipes.stdout

def popen4(cmd, mode="t", bufsize=_marker):
    kwargs = {"stdin": subprocess.PIPE,
              "stdout": subprocess.PIPE,
              "stderr": subprocess.STDOUT}
    if bufsize is not _marker:
        kwargs["bufsize"] = bufsize
    pipes = subprocess.Popen(cmd, **kwargs)
    return pipes.stdin, pipes.stdout