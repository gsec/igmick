igmick
======
Image mickery and mockery :))

Takes consecutive screenshots and compares the contents. If they are equal send an email 
to specified recipient.

Dependencies
--------------------------------------------------------------------------------
Install dependencies using `pip`:
- `pip install -r requirements.txt`

Needs:
* pyscreenshot  (for grabbing the screen)
* numpy         (to do image processing)
* smtplib, ssl  (for sending mail)
* matplotlib    (to plot image deltas) [optional]


Configure
--------------------------------------------------------------------------------
* Copy `cfg_skel.py` to `cfg.py`
* Set email recipient and imap server in `[mail]`
* Configure the image grabbing:
    - `cut`: which part of the screen shall be considered in pixels
    - `sleeptime`: how many seconds in between two screenshots
    - `tolerance`: what is the max difference of two pictures to trigger
        the difference is the difference of two screenshots as numpy array,
        ten should be a good number


Running
--------------------------------------------------------------------------------
Just start somewhere in a shell `./igmick.py` and leave it running as long as you want to 
check your screen.

Author
--------------------------------------------------------------------------------
gsec (2020) <o0v0o.ix@gmail.com>

Feel free to use it as open source. If in doubt, take GPL 2.
