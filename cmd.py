#!/usr/bin/python

import sys, getopt

from lib.gmail import read_email_from_gmail

if __name__ == '__main__':
    argv = sys.argv[1:]
    email = ''
    password = ''
    folder = 'inbox'
    try:
        opts, args = getopt.getopt(argv, "e:p:f", ["email=", "password=", "folder="])
    except getopt.GetoptError:
        print 'cmd.py -e <email address> -p <password> [<folder>]'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'cmd.py -e <email address> -p <password> [<folder>]'
            sys.exit()
        elif opt in ("-e", "--email"):
            email = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-f", "--folder"):
            folder = arg

    read_email_from_gmail(email, password, folder)