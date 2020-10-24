# Queusadilla
An extremely simple discord queue bot meant for self hosting or use in single servers
Currently the bot uses a global list to save the queue. This means that the list is essentially shared between servers, if the bot were to added to more than one
Commands:

!add
Adds oneself to the queue

!clear
Clears the ENTIRE list

!queue
Lists out any users in the queue

!leave
Removes yourself from the queue if possible

!remove *username str*
Attempts to find a user with the given name, and removes them from the queue

!next *number int def=1*
Pings the next *number* of people in the queue to join, and removes them from the queue
