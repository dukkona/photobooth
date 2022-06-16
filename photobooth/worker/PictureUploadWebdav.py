#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Photobooth - a flexible photo booth software
# Copyright (C) 2018  Balthasar Reuter <photobooth at re - web dot eu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import logging
import requests

from pathlib import Path

from .WorkerTask import WorkerTask


class PictureUploadWebdav(WorkerTask):

    def __init__(self, config):

        super().__init__()

    def do(self, picture, filename):

        s = requests.session()
        url_login = "https://www.dukkon.com/setpin"
        headers={"Content-Type":"text", "pin": "1994"}
        s.get(url_login, headers=headers)
        logging.info('Uploading picture as %s', filename)
        response = s.request("POST", "https://www.dukkon.com/wedding/upload_pb", data=picture.getbuffer())

        if response.status_code in range(200, 300):
            logging.warn(('PictureUploadWebdav: Upload failed with '
                          'status code {}').format(response.status_code))