#    X-tra-Telegram (userbot for telegram)
#    Copyright (C) 2019-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from xtrabot import client, Var
from telethon import events
import re
xconfig = {}
func_name = {}

class Module():
    def __init__(self, funct):
        try:
            self.name
        except NameError:
            self.name = "untitled"
        if type(funct) is not list:
            funct = [funct]
        for i in funct:
            func = i
            if 1==1:
                funcmd = re.compile("^."+func.__name__)
                try:
                    func_name[self.name].append(func)
                except KeyError:
                    func_name.update({self.name: [func]})
                self.xconfig = xconfig
                self.client = client
                self.config = Var
                client.add_event_handler(func, events.NewMessage(pattern=funcmd, outgoing=True))

    def addxconfig(self, name, value, about=""):
        self.xconfig.update({name: [value, about]})

def command(**args):
    def decorator(func):
        client.add_event_handler(func, events.NewMessage(**args))
    return decorator
