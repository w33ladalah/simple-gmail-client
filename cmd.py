#!/usr/bin/python

import sys, getopt

from lib.gmail import read_email_from_gmail

if __name__ == '__main__':
    try:
        argv = sys.argv[1:]

        email = ''
        password = ''
        folder = 'inbox'
        pattern = ''
        limit = 1

        opts, args = getopt.getopt(argv, "e:p:f:t:l", ["email=", "password=", "folder=", "pattern=", "limit="])

        for opt, arg in opts:
            if opt == '-h':
                print 'cmd.py -e <email address> -p <password> [<folder> [<pattern> [<limit number>]]]'
                sys.exit()
            elif opt in ("-e", "--email"):
                email = arg
            elif opt in ("-p", "--password"):
                password = arg
            elif opt in ("-f", "--folder"):
                folder = arg
            elif opt in ("-t", "--pattern"):
                pattern = arg
            elif opt in ("-l", "--limit"):
                limit = arg

        mails = read_email_from_gmail(email, password, folder, pattern, limit)

        print mails
    except getopt.GetoptError:
        print 'cmd.py -e <email address> -p <password> [<folder> [<pattern> [<limit number>]]'
        sys.exit(2)