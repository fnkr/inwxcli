#!/usr/bin/env python
import argparse
from .inwx import domrobot, prettyprint


class Domrobot():
    def __init__(self, api_url, username, password):
        self.domrobot = domrobot(api_url, False)
        self.domrobot.account.login({'lang': 'en', 'user': username, 'pass': password})

    def call(self, method_name, vars):
        method = self.domrobot
        for method_name in method_name.split('.'):
            method = getattr(method, method_name)
        return method(vars)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--endpoint', help='API endpoint', default='https://api.domrobot.com/xmlrpc/')
    parser.add_argument('--username', help='Username', required=True)
    parser.add_argument('--password', help='Password', required=True)
    format_parser = parser.add_mutually_exclusive_group(required=False)
    format_parser.add_argument('--format', help='Format')
    format_parser.add_argument('--pretty', action='store_true', default=False, help='Attempt pretty print')
    parser.add_argument('vars', nargs=argparse.REMAINDER)
    return parser.parse_args()


def parse_vars(vars):
    parsed_vars = {}
    for var in vars:
        key, value = var.split('=', 1)
        parsed_vars[key] = value
    return parsed_vars


def main():
    args = parse_args()

    method_name = args.vars[0]
    vars = parse_vars(args.vars[1:])

    domrobot = Domrobot(args.endpoint, args.username, args.password)
    result = domrobot.call(method_name, vars)
    if args.format:
        print(args.format.format(**result))
    elif args.pretty:
        print(getattr(prettyprint, method_name.replace('.', '_'))(result))
    else:
        print(result)


if __name__ == '__main__':
    main()
