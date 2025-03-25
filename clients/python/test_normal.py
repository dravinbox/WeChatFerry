#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from queue import Empty
from threading import Thread
from time import sleep

from wcferry import Wcf

logging.basicConfig(level='DEBUG', format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
LOG = logging.getLogger("Demo")


def process_msg(wcf: Wcf):
    """处理接收到的消息"""
    while wcf.is_receiving_msg():
        try:
            msg = wcf.get_msg()
            LOG.info(msg)  # 简单打印
        except Empty:
            continue  # Empty message
        except Exception as e:
            LOG.error(f"Receiving message error: {e}")


def main():
    LOG.info("Start demo...")
    wcf = Wcf(debug=True)             # 默认连接本地服务

    sleep(5)  # 等微信加载好，以免信息显示异常
    LOG.info(f"已经登录: {True if wcf.is_login() else False}")
    LOG.info(f"wxid: {wcf.get_self_wxid()}")

    # 允许接收消息
    # wcf.enable_recv_msg(LOG.info) # deprecated

    # 允许接收消息
    wcf.enable_receiving_msg(pyq=True)  # 同时允许接收朋友圈消息
    Thread(target=process_msg, name="GetMessage", args=(wcf,), daemon=True).start()

    # wcf.disable_recv_msg() # 当需要停止接收消息时调用
    sleep(5)
    ret = wcf.send_text("wh", "filehelper")
    LOG.info(f"send_text: {ret}")

    sleep(5)
    # 需要确保图片路径正确，建议使用绝对路径（使用双斜杠\\）
    ret = wcf.send_image("https://t7.baidu.com/it/u=2638406194,523661981&fm=193&f=GIF", "filehelper")
    LOG.info(f"send_image: {ret}")


    return wcf


if __name__ == "__main__":
    wcf = main()

    # 一直运行
    wcf.keep_running()
