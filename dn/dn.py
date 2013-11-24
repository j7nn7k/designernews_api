#!/usr/bin/env python
"""
Python API for Hacker News.
@author Karan Goel
@email karan@goel.im

The MIT License (MIT)
Copyright (c) 2013 Karan Goel

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import string

from bs4 import BeautifulSoup
import requests


BASE_URL = 'http://news.layervault.com/'


class DN(object):
    """
    The class that parses the DN page, and builds up all stories
    """

    def _get_soup(self, page=''):
        """
        Returns a bs4 object of the page requested
        """
        content = requests.get('%s/%s' % (BASE_URL, page)).text
        return BeautifulSoup(content)

    def _build_story(self, soup):
        """
        Builds and returns a list of stories (dicts) from the passed source.
        """

        wrapper = soup.find(class_='InnerPage').findChildren('ol')[0]  # get wrapper around the stories
        rows = wrapper.find_all(class_='Story')  # get stories

        all_stories = []  # list to hold all stories

        # break up stories into pieces
        for index, row in enumerate(rows):

            link = row.find(class_='StoryUrl')['href']

            if link.find('http') is -1 : # the link doesn't contain "http" so it's an internal link
                link = '%s/%s' % (BASE_URL, link)
                domain = BASE_URL
                is_self = True
            else:
                domain = str(row.find(class_='Domain').contents[0]).translate(None, '()')
                is_self = False

            rank = str(index + 1)
            # strip newlines and whitespaces
            title = unicode(row.find(class_='StoryUrl').contents[0]).strip()
            story_id = row['data-id']

            # extract numbers from a string
            # http://stackoverflow.com/a/1451407/268125
            all = string.maketrans('', '')
            nodigs = all.translate(all, string.digits)

            points = str(row.find(class_='PointCount').contents[0]).translate(all, nodigs)
            num_comments = str(row.find(class_='CommentCount').contents[0]).translate(all, nodigs)

            story = {
                "rank": rank,
                "story_id": story_id,
                "title": title,
                "link": link,
                "domain": domain,
                "points": points,
                "num_comments": num_comments,
                "is_self": is_self
            }
            all_stories.append(story)

        return all_stories

    def get_stories(self, story_type=''):
        """
        Returns a list of stories from the passed page
        of DN. 'story_type' can be:
        '' = top stories (homepage)
        'new' = most recent stories
        """
        return self._build_story(self._get_soup(page=story_type))
