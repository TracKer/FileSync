import argparse
from argparse import ArgumentParser, Namespace
from typing import Dict


class CommandLineHandler:
    __ARGUMENTS = {
        '--primary': {
            'flag': True,
            'description':
                'Used for conflicts resolution, primary will have highest priority. Conflicts between two primaries will be ' +
                'solved in prior of latest changes. Used by default if "--secondary" is not set.'
        },

        '--secondary': {
            'flag': True,
            'description':
                'Used for conflicts resolution, secondary will have lowest priority.'
        },

        '--link': {
            'flag': False,
            'description':
                'Attached address'
        }
    }

    __parser: ArgumentParser
    __parsedData: Namespace

    def __init__(self) -> None:
        self.__initArgumentsParser()
        self.__parse()

    def __initArgumentsParser(self) -> None:
        self.__parser = argparse.ArgumentParser(description='File sync')

        self.__parser.add_argument(
            'action',
            choices=['init', 'watch'],
            type=str,
            help='Action identifier, may be "init" or "watch"'
        )

        self.__parser.add_argument(
            
        )

        # self.__parser.add_argument(
        #     'conflict-solver',
        #     required=
        # )
        #
        # self.__parser.add_argument(
        #     '--primary',
        #     action='store_true',
        #     help='Used for conflicts resolution, primary will have highest priority. Conflicts between two primaries will be ' +
        #          'solved in prior of latest changes. Used by default if "--secondary" is not set.'
        # )
        #
        # self.__parser.add_argument(
        #     '--secondary',
        #     action='store_true',
        #     help='Used for conflicts resolution, secondary will have lowest priority.'
        # )

    def __parse(self):
        self.__parsedData = self.__parser.parse_args()

    def getAction(self) -> str:
        return self.__parsedData.action
