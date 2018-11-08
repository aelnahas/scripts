#! /usr/bin/env python3
# This script listen for events from i3 ( any kind of event and notifies polybar )
from i3ipc import Connection
from subprocess import call

def windownotify(i3, event):
    command = ['polybar-msg', 'cmd']
    if event.container.fullscreen_mode == 0:
       command.append('show')
    else:
        command.append('hide')
    call(command)

if __name__ == '__main__':
    i3 = Connection()
    i3.on('window', windownotify)
    i3.main()
