#!/usr/bin/env python3

from controller.XXXXXXXController import XXXXXXXController


def config():
    controller = XXXXXXXController()
    return {
        'commands': [
            {
                'command': 'start',
                'function': controller.start
            },
            {
                'command': 'help',
                'function': controller.help
            }
        ],
        'buttons': controller.buttonsController,
        'nocommands': [
            {
                'filter': 'text',
                'function': controller.processText
            },
			{
                'filter': 'photo',
                'function': controller.processImage
            }
        ]
    }
