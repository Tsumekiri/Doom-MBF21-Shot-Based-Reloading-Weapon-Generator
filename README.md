# Doom MBF21 Shot-Based Reloading Weapon Generator
Doom MBF21 Shot-Based Reloading Weapon Generator takes your ready and fire states, copies it by the number of shots desired, numbers them and adds a little code to make sure they're called in order. It is based on the reloading method from Terror Signal﻿ by SeaTree.

Be **careful** not to overwrite your weapon. This only copies the repeating `ready` and `fire` states. You still have to write the rest yourself, including the states `select`, `deselect`, `ready`, `fire` and finally, `reload`.

An example WAD is provided, alongside the appropriate `DECOHack`, `.deh` file, `ready_state.txt` and `fire_state.txt`. It uses sprites and sounds taken from Realm667, the UAC Battle Rifle. Credits to Firearms Source Team, Triune Digital, Navaro for the sounds and Mike12 for the sprites.

# What use is this?
If your reloading weapon uses dozens of shots before firing, copying and pasting by hand is exhaustive and error-prone. Especially so if all your weapons require reloading. This speeds up the process significantly, allowing you to quickly make a 24-round magazine for your rifle, for instance. Also, if you find any errors and need to fix it, all you have to do is change them once and rerun the script.

# How to use
1. You need to create two files: `ready_state.txt` and `fire_state.txt` on the same folder you have the script located;
2. Copy the contents of your `ready` state and `fire` state to the respective files;
3. Run the script, it uses Python3;
4. Write the number of shots you want before reloading and press `enter`. E.g. `6`;
5. The result will both be printed to the console and written to a file called `weapon_result.txt`;
6. Copy the contents of `weapon_result.txt` into your weapon's DECOHack. Make sure not to have `goto ready` or `A_ReFire` in your weapon's fire state. It also has to be right **before** the `reload` state, so it is called after the last shot.

# What's been generated?
Basically it adds `A_RefireTo` to the beginning of the `ready` states (E.g. `TNT1 A 0 A_RefireTo("fire2")`) and a loop at the end of each state. It also numbers each repetition (E.g. `fire6`) to be "refired" to.
