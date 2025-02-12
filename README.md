# i3workswitch
Quick nearest-unused workspace switcher for i3.

### What am I looking at?
You ever wanted to switch focus to a workspace yet unoccupied, unbothered? Laziness ever got the best of you, to the point where you didn't even want to bother checking your list of workspaces for an unused number? Well, I kid you not, I got the feeling quite often. So often, I got to typing. 

In all seriousness, this peice of code can move user focus to the nearest available (and on into unused workspaces), furthermore, it can move the current focused window, if you choose so. It can also do it in reverse! (All functions, of course).

### User's manual
Since I assume you wouldn't want an option-selection window to open each time you ran the code, I made it so that you can easily access the functions of this code at your leisure. Just slap a `--reverse` on the back end of your launch cmnd to initiate a reversed version of focus switching - or use the shiny new `--move` to move your current container (open window, as the normies call it) to the nearest unused and empty workspace. If you're feeling hurried, you can use `--jump` to quickly make your way to the nearest unused workspace.

Like this:

 * Switch focus to the next workspace (whether unused or used): `path/to/movewindow.py`
 * Switch focus to the nearest workspace behind your focus: `path/to/movewindow.py --reverse`
 * Move container to the next workspace (whether unused or used): `path/to/movewindow.py --move`
 * Move container to the nearest workspace workspace behind focus: `path/to/movewindow.py --move --reverse` (order matters not)

