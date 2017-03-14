#!/usr/bin/env python
#encoding: utf-8
#Author: Hantzley Tauckoor
#Date 12 March 2017
#Python version 3.X

def loadSettings(settingsFile):
    """Reads settings file into an list.

    :param settingsFile: the name of the settings file e.g. ``'settings.txt'``
    :type settingsFile: string
    :returns: the newly-created list
    """

    with open(settingsFile,'r') as f:
        settings = f.readlines()
    f.close()

    return settings


if __name__ == '__main__':
    appSettings = loadSettings("../settings.txt")

    firstSetting = appSettings[0].rstrip()
    secondSetting = appSettings[1].rstrip()


    print(firstSetting)
    print(secondSetting)
