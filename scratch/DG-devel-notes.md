
Sun 01 Oct 2023 07:43:41 AM PDT

https://github.com/dagent/amixer-webui -- forked from https://github.com/JiriSko/amixer-webui

git clone git@github.com:dagent/amixer-webui.git

## Goal:
Add functionality:

* Ability to display only capture devices.
* Save alsa setup
* Show other info -- input peak meter, what process using device

### Setup

From this `$DEVEL_ROOT` ( currently /home/gent/Development/amixer-webui)
```
pyenv local 3.6.9 # What runs on Mint19 for the fitlet
python -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install pip-tools
pip-sync
# flask etc intalled

python alsamixer_webui.py  # works on bilbao

```
A bit of:
* .gitignore update
* start these notes
* `git checkout -b addCaptureOnlyArgument`

#### capture devices in alsamixer_webui.py

get_controls (line 93) basically runs (per card):
`amixer -c 1 | grep -e control -e channels`
and
`amixer -c 1 contents`
and then tries to make sense of that

I want to only select for capture mixer controls, and here is a command that will return the numid's only for capture (I think):
`amixer -c 0 controls | grep MIXER |  grep -vi playback | sed -n 's/^.*=\([0-9]\+\),.*$/\1/p'`

#### use pyalsaaudio ?

alsa-capture-select.py after `pip install pyalsaaudio`
Damnit -- no way to get the numid, which is what I need.  (there is a
Mixer.mixerid() method, but it only returns what has been set, which is
0 by default)

#### working hack
Thu 05 Oct 2023 09:47:40 PM PDT

Hacked in a function to generate numid's in the main Handler, and used it to filter out playback interfaces