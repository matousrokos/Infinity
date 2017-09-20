#!/usr/bin/env python

import sys
import optparse


_USERNAME = 'admin'
_password = sys.argv[1]
hostname = sys.argv[5]
domain = sys.argv[6]


self._console.read_until('[sudo] password for {0}: '.format(self._USERNAME))
self._console.write('{0}\n'.format(self._password))
self._console.read_until('IP Address')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._config['base_ip']))self._console.read_until('Network mask')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._config['netmask']))
self._console.read_until('Gateway')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._config['gateway']))
self._console.read_until('Hostname')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._config['hostname']))
self._console.read_until('Domain suffix')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._config['domain']))
self._console.read_until('DNS servers')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._config['dns_server']))
self._console.read_until('NTP servers')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._config['ntp_server']))
self._console.read_until('Web administration username')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._USERNAME))
self._console.read_until('Web administration password')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._password))
self._console.read_until('Re-enter previous value')
self._console.read_until(': ')
self._console.write('{0}\n'.format(self._password))
self._console.read_until('Enable incident reporting (yes/no)')
self._console.read_until(': ')
self._console.write('yes\n')