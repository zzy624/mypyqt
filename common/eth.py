# -*-coding:utf-8-*-


import sys,time
# import cgitb
# cgitb.enable( format = 'text')
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from ethjsonrpc import EthJsonRpc

def get_ethclient(host):
    if host == "":
        return None
    if "https" in host:
        _port = 443
        _host = host.split(':')[1].split('//')[1]
    else:
        _port = host.split(':')[2]
        _host = host.split(':')[1].split('//')[1]
    try:
        client = EthJsonRpc(host=_host, port=_port, tls=True)
    except Exception as e:
        QMessageBox.information(self,"Information",str(e))
        return
    if client.net_listening():
        return client
    else:
        return