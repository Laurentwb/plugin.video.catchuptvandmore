# -*- coding: utf-8 -*-
"""
    Catch-up TV & More
    Copyright (C) 2018  SylvainCecchetto

    This file is part of Catch-up TV & More.

    Catch-up TV & More is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Catch-up TV & More is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with Catch-up TV & More; if not, write to the Free Software Foundation,
    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from resources.lib import utils
from resources.lib import common

# TO DO

# Live
# https://www.cgtn.com/public/bundle/js/live.js
URL_LIVE_CGTN = 'https://news.cgtn.com/resource/live/%s/cgtn-%s.m3u8'
# Channel (FR|ES|AR|EN|RU|DO(documentary))


def channel_entry(params):
    """Entry function of the module"""
    if 'replay_entry' == params.next:
        params.next = "list_shows_1"
        params["page"] = "0"
        return list_shows(params)
    elif 'list_shows' in params.next:
        return list_shows(params)
    elif 'list_videos' in params.next:
        return list_videos(params)
    elif 'play' in params.next:
        return get_video_url(params)


@common.PLUGIN.mem_cached(common.CACHE_TIME)
def list_shows(params):
    """Build categories listing"""
    return None

@common.PLUGIN.mem_cached(common.CACHE_TIME)
def list_videos(params):
    """Build videos listing"""
    return None


@common.PLUGIN.mem_cached(common.CACHE_TIME)
def start_live_tv_stream(params):
    params['next'] = 'play_l'
    return get_video_url(params)


def get_video_url(params):
    """Get video URL and start video player"""
    if params.next == 'play_l':
        desired_language = common.PLUGIN.get_setting(
            params.channel_name + '.language')

        url_live = ''
        if params.channel_name == 'cgtndocumentary':
            url_live = URL_LIVE_CGTN % ('document', 'doc')
        else:
            if desired_language == 'FR':
                url_live = URL_LIVE_CGTN % ('french', 'f')
            elif desired_language == 'EN':
                url_live = URL_LIVE_CGTN % ('english', 'news')
            elif desired_language == 'AR':
                url_live = URL_LIVE_CGTN % ('arabic', 'r')
            elif desired_language == 'ES':
                url_live = URL_LIVE_CGTN % ('espanol', 'e')
            elif desired_language == 'RU':
                url_live = URL_LIVE_CGTN % ('russian', 'r')
        return url_live