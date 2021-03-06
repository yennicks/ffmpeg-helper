# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse

from .cropdetect.cli import cli as cropdetect_cli
from .transcode.cli import cli as transcode_cli


def cli():
    parser = argparse.ArgumentParser(description='An opinionated command line ffmpeg script.')
    subparsers = parser.add_subparsers(help='All available commands',
                                       required=True,
                                       dest='command')
    cropdetect_cli(subparsers)
    transcode_cli(subparsers)

    args = parser.parse_args()
    args.func(args)
