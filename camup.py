import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='block')

for action, device in monitor:
    if action == 'add':
        print("{0!r} added".format(device))
    elif action == 'remove':
        print("{0!r} removed".format(device))
