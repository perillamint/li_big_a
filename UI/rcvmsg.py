#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Slixmpp: The Slick XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of Slixmpp.

    See the file LICENSE for copying permission.
"""

import logging
from getpass import getpass
from argparse import ArgumentParser

import slixmpp

class rcvmsg(slixmpp.ClientXMPP):
	def __init__(self, jid, password):
		slixmpp.ClientXMPP.__init__(self, jid, password)
		self.add_event_handler("session_start", self.start)
		self.add_event_handler("message", self.message)
	def start(self, event):
		self.send_presence()
		self.get_roster()
	def message(self, msg):
		if msg['type'] in ('chat', 'normal'):
			#print(msg['body'])     #msg['body'] is the message recieved


if __name__ == '__main__':
	jid = input("Username:")
	password = getpass("Password:")
	
	xmpp = rcvmsg(jid, password)
	xmpp.register_plugin('xep_0030')
	xmpp.register_plugin('xep_0004')
	xmpp.register_plugin('xep_0060')
	xmpp.register_plugin('xep_0199')
	
	xmpp.connect()
	xmpp.process()
