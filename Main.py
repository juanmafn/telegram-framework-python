#!/usr/bin/env python3
# coding: utf8
__author__ = "Juan Manuel Fernández Nácher"
__version__ = "0.0.1"

# Clase que maneja la api de telegram
from api.TelegramApi import TelegramApi
from ComandosConfig import config

def main():
	TOKEN = open('token', 'r').read().strip()
	bot = TelegramApi(TOKEN, config())
	bot.startBot()

if __name__ == "__main__":
	main()
