os: mac
user.running: aerospace
-
focus left: key("alt-n")
focus down: key("alt-e")
focus up: key("alt-i")
focus right: key("alt-o")

(win|window) move left: key("alt-shift-n")
(win|window) move down: key("alt-shift-e")
(win|window) move up: key("alt-shift-i")
(win|window) move right: key("alt-shift-o")

(win|window) (lay|layout) (tile|tiles): key("alt-/")
(win|window) (lay|layout) (cord|accord|accordion): key("alt-,")

^outer space <user.letter>$: user.aerospace_workspace("{user.letter}")
# ^aero space <user.number>$: user.aerospace_workspace("{user.number_key}")

