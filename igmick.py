#!/usr/bin/env python
# coding: utf-8
""" igmick - Image mickery and mockery :))

    gsec (2020) <o0v0o.ix@gmail.com>

    Feel free to use it as open source. If in doubt, take GPL 2.


1) Configure `cfg_skel.py` and rename to `cfg.py`
2) Check the image boundaries in the `cut` variable
3) check the timing cycle, in the `sleeptime` variable
4) let it run somewhere in the background

An email will be sent if in between the sleeptime nothing changes in the selected cut.
"""
from time import sleep
from numpy import array, sum, s_
from pyscreenshot import grab
import smtplib, ssl

try:
    from cfg import CFG
except ImportError:
    from cfg_skel import CFG

try:
    from matplotlib import pyplot as plt
except ImportError:
    plt = False
    print("Install matplotlib to output the screenshot.")


def igmick(handler) -> array:
    """ Compare two consecutive screenshots and return if they are too similar.
    """
    ((ys, ye), (xs, xe)) = handler["cut"]
    cut = s_[ys:ye, xs:xe]

    print(f"Capturing screen box [y:({ys}, {ye}), x:({xs}, {xe})]")
    pre = array(grab())
    precut = pre[cut]
    cnt = 0.0
    while True:
        cnt += 1.0
        print("Recap...", 1 / cnt)
        post = array(grab())
        postcut = post[cut]
        diff = postcut - precut
        if (deviation := sum(diff)) < handler["tolerance"]:
            print("Total difference: ", deviation)
            return postcut
        sleep(handler["sleeptime"])
        precut = postcut


def sendmail(handler):
    """ from here:
    https://realpython.com/python-send-email/#starting-a-secure-smtp-connection
    """
    context = ssl.create_default_context()
    with smtplib.SMTP(handler["smtp_server"], handler["port"]) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(handler["sender_email"], handler["password"])
        server.sendmail(
            handler["sender_email"], handler["receiver_email"], handler["message"]
        )


def main():
    mickery = igmick(CFG["image"])
    if plt:
        plt.imshow(mickery)
        plt.show()
    # uncomment to send mail notification:
    # sendmail(CFG["mail"])

if __name__ == "__main__":
    main()
