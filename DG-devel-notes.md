
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


