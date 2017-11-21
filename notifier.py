#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import call
from CvClient import CvClient
from datetime import datetime
import os

class Notifier:
    # Campus Virtual UdL
    CV_WEB = "https://cv.udl.cat/portal"

    def __init__(self):
        self.cv_client = CvClient(Notifier.CV_WEB, "got2", "<pass>")
        self.cv_client.connect()
        self.cv_client.login()

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
        print date + " - " + message

def main():
    n = Notifier()
    n.notify_news()

if __name__ == '__main__':
    main()
