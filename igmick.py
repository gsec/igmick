#!/usr/bin/env python
# coding: utf-8
""" igmick - Image mickery and mockery :))

    gsec (2020) <o0v0o.ix@gmail.com>

    Feel free to use it as open source. If in doubt, take GPL 2.
"""
from time import sleep
from sys import exit
from numpy import array, sum, s_
from pyscreenshot import grab


def igmick(sleeptime: int = 10, cut: slice = None) -> array:
    """ Compare two consecutive screenshots and return if they differ too much.
    """
    TOLERANCE = 10
    if cut is None:
        cut = s_[540:570, 10:350]
    try:
        print("Taking precut")
        pre = array(grab())
        precut = pre[cut]
        while True:
            print("Taking postcut")
            post = array(grab())
            postcut = post[cut]
            diff = postcut - precut
            if (deviation := sum(diff)) > TOLERANCE:
                print("Total difference: ", deviation)
                return diff
            sleep(sleeptime)
            precut = postcut
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":

    ig = igmick(1)
    if True:
        from matplotlib import pyplot as plt
        plt.imshow(ig)
        plt.show()
