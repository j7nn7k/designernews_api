#!/usr/bin/env python

from dn import DN

dn = DN()

# print top 10 stories from homepage
for story in dn.get_stories()[:10]:
    print story["points"], story["title"]
    print '**********************'
    print ''

# print 10 latest stories
for story in dn.get_stories(story_type='new')[:10]:
    print story["points"], story["title"]
    print '**********************'
    print ''
