import requests
import threading, sys, os
from pystyle import *
class Main:
    def buff():
        response = requests.get('https://www.mediafire.com/file/iygebn7qdzn7o9h/Li%25C3%25AAn_qu%25C3%25A2n_ModVip_s25.apk').text
        print(response)
    def run_share():
                threa = 100
                while True:
                    t = threading.Thread(target=Main.buff)
                    t.start()
                    while threading.active_count() > threa:
                        t.join()
if __name__ == "__main__":
        Main.run_share()