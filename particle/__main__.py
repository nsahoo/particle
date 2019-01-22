#!/usr/bin/env python

from __future__ import absolute_import,  print_function

from .particle import Particle
from .pdgid import PDGID

import argparse

parser = argparse.ArgumentParser(description='Particle utility')

subparsers = parser.add_subparsers(help="Subcommands")

search = subparsers.add_parser('search', help='Look up particles by PID or name')
search.add_argument('particle', nargs='+', help='Name(s) or ID(s)')

pdgid = subparsers.add_parser('pdgid', help='Print info from PID')
pdgid.add_argument('pdgid', nargs='+', help='ID(s)')

opts = parser.parse_args()

if 'particle' in opts:
    for cand in opts.particle:
        if hasattr(cand, 'decode'):
            cand = cand.decode('utf-8')

        try:
            value = int(cand)
        except ValueError:
            value = 0

        if value:
            particle = Particle.from_pdgid(value)
        else:
            particle = Particle.from_string(cand)

        print(particle.describe())
        print()

if 'pdgid' in opts:
    for value in opts.pdgid:
        p = PDGID(value)
        print(p)
        print(PDGID(value).info())

