os: mac
app: iterm2
-
tag(): terminal
# todo: filemanager support
#tag(): user.file_manager
tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl
tag(): user.tabs
tag(): user.readline

clear word: key(alt-backspace)
tab previous: key(cmd-shift-[)
tab next: key(cmd-shift-])

history: key(ctrl-r)
files: key(ctrl-t)
(vim | vin) mode: key(cmd-shift-c)
