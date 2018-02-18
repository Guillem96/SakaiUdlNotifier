#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from subprocess import call
from CvClient import CvClient
from datetime import datetime
import os
from sys import argv

class Notifier:
    # Campus Virtual UdL
    CV_WEB = "https://cv.udl.cat/portal"

    def __init__(self, username, password):
        self.cv_client = CvClient(Notifier.CV_WEB, username, password)
        self.cv_client.connect()
        self.cv_client.login()
        Notifier.write_log("Login: " + username + " " + password)

    def notify_news(self):
        # Notificar 5 nous anuncis
        for n in self.cv_client.get_news(5):
            # Escriure al log l'anunci
            Notifier.write_log(n['subject'].encode('utf-8') + " " + n['link'].encode('utf-8'))
            self.send_notification(n['subject'])

    def send_notification(self, header):
        icon_path = os.path.realpath(os.path.dirname(__file__)) + "/udl_logo.jpg"
        call(["notify-send", header, "Mirar el log per a més informació.", "-i", icon_path,])

    @staticmethod
    def write_log(message):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(date + " - " + message)

def main():
    n = Notifier(argv[1], argv[2])
    n.notify_news()

if __name__ == '__main__':
    main()
