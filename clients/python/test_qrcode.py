#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from queue import Empty
from threading import Thread
from time import sleep

from wcferry import Wcf

logging.basicConfig(level='DEBUG', format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
LOG = logging.getLogger("Demo")





def test_qrcode():
    LOG.info("Start demo...")
    wcf = Wcf(debug=True,block=False)            

    qr_url = wcf.get_qrcode()

    LOG.info(f"qr_url: {qr_url}")
  



if __name__ == "__main__":
    test_qrcode()

