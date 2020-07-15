#!/usr/bin/env python
# coding: utf-8
""" igmick - Image mickery and mockery :))

    gsec (2020) <o0v0o.ix@gmail.com>

    Feel free to use it as open source. If in doubt, take GPL 2.

Configuration:
1) Copy `cfg_skel.py` to `cfg.py`, this will be used for configuration.
2) Set the image boundaries in the `cut` variable
3) Choose the timing cycle in the `sleeptime` variable
4) Leave it running in background as long as screens should be compared.
"""
from time import sleep
from numpy import array, sum, s_
from pyscreenshot import grab
import smtplib, ssl

try:
    from cfg import CFG
    USER_CONFIG = True
except ImportError:
    from cfg_skel import CFG
    USER_CONFIG = False
    print(
        "Please copy `cfg_skel.py` to `cfg.py` and adjust "
        "your mail settings to enable notifications.\n"
    )

try:
    from matplotlib import pyplot as plt
except ImportError:
    plt = False
    print("Install matplotlib to output the screenshot.")


def igmick(params: dict) -> array:
    """ Compare two consecutive screenshots and return if they are too similar.
    """
    ((ys, ye), (xs, xe)) = params["cut"]
    cut = s_[ys:ye, xs:xe]

    print(f"Capturing screen box [y:({ys}, {ye}), x:({xs}, {xe})]")
    pre = array(grab())
    precut = pre[cut]
    cnt = 0.0
    while True:
        sleep(params["sleeptime"])
        cnt += 1.0
        print("Recap...", 1 / cnt)
        post = array(grab())
        postcut = post[cut]
        diff = postcut - precut
        if (deviation := sum(diff)) < params["tolerance"]:
            print("Total difference: ", deviation)
            return postcut
        precut = postcut


def sendmail(params: dict):
    """ from here:
    https://realpython.com/python-send-email/#starting-a-secure-smtp-connection
    """
    context = ssl.create_default_context()
    with smtplib.SMTP(params["smtp_server"], params["port"]) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(params["sender_email"], params["password"])
        server.sendmail(
            params["sender_email"], params["receiver_email"], params["message"]
        )


def main():
    mickery = igmick(CFG["image"])
    if USER_CONFIG:
        sendmail(CFG["mail"])
    if plt:
        plt.imshow(mickery)
        plt.show()


if __name__ == "__main__":
    main()
