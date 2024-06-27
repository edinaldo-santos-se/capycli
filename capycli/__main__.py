# -------------------------------------------------------------------------------
# Copyright (c) 2019-23 Siemens
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (c) 2019-2023 Siemens
# -------------------------------------------------------------------------------

"""Module allowing for ``python -m CaPyCli ...``."""
import sys
from capycli.setup.no_ssl_verification import no_ssl_verification
from capycli.main import cli

sslVerify = '--no-ssl-verify' not in sys.argv

if not sslVerify:
    with no_ssl_verification():
        cli.main()
else:
    cli.main()
