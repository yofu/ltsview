#! /usr/bin/env python
#-*- coding: utf-8 -*-

import os
import argparse as ap
from collections import OrderedDict

__separator__='---'

def view(fn,keys=None,level=None):
    with open(fn) as f:
        for l in f:
            sep=False
            data=OrderedDict([x.split(':',1) for x in l.rstrip().split('\t')])
            if level is None or data['levelname'] in level:
                for k,v in data.items():
                    if keys is None or k in keys:
                        print '{}: {}'.format(k,v)
                        sep=True
                if sep:
                    print __separator__

if __name__ == '__main__':
    parser=ap.ArgumentParser(description='LTSV Viewer')
    parser.add_argument('-k','--key',metavar='KEY',type=str,nargs='+',default=None,help='specify the keys of data')
    parser.add_argument('-l','--level',metavar='LEVEL',type=str,nargs='+',default=None,help='specify the level of data')
    parser.add_argument('inp',metavar='INP',type=str,help='Input File Name')
    args=parser.parse_args()
    if os.path.exists(args.inp):
        print 'INPUT: {}'.format(args.inp)
        print __separator__
        view(args.inp,args.key,args.level)
    else:
        print "{} doesn't exist".format(args.inp)
