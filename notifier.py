#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import call
from CvClient import CvClient
import os

class Notifier:
    # Campus Virtual UdL
    CV_WEB = "https://cv.udl.cat/portal"

    def __init__(self):
        self.cv_client = CvClient(Notifier.CV_WEB, "<username>", "<password>")
        self.cv_client.connect()
        self.cv_client.login()

    def notify_news(self):
        # Notificar 5 nous anuncis
        for n in self.cv_client.get_news(5):
            self.send_notification(n['subject'])

    def send_notification(self, header):
        icon_path = os.path.realpath(os.path.dirname(__file__)) + "/udl_logo.jpg"
        call(["notify-send", header, "-i", icon_path,])

def main():
    n = Notifier()
    n.notify_news()

if __name__ == '__main__':
    main()
