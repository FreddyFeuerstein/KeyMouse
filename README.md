# KeyMouse
A simple solution for mouse control in linux using a keyboard
#
How to use:

Simply run
```
keymouse
```
in your linux terminal.

The keymapping is as follows:
```
             Up -. .- Right click
                 | |
Right click -> U I O P <- Middle click
       Left -> J K L <- Right
                 |
                Down
```
#
Installation:
On Debian / Ubuntu / Linux Mint:
```
git clone http://github.com/FreddyFeuerstein/KeyMouse.git
cd KeyMouse
sudo apt install ./keymouse_0.0.2-0_i386.deb
```
On other distros:
unpack the "bin-i386.zip" file and run the keymouse binary file.
#
Building from source:
If you want to build your own (maybe modified) version, follow the following instructions:

Make sure that you have pyinstaller for python 3 installed. If not, install it with the following command:
```
pip3 install pyinstaller
```
Then you can build the source using
```
pyinstaller keymouse.py
```
