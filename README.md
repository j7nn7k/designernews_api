Designernews API
================

Python API for [Designer News](https://news.layervault.com/). Inspired by the [`HackerNewsAPI`](https://github.com/karan/HackerNewsAPI/)

Class
=====

## `DN`

The class that parses the Designer News page, and builds up all stories.

#### Methods

`get_stories(story_type='')` - Returns a list of stories from the passed page of Designer News. 'story_type' can be: '' = top stories (homepage), 'new' = most recent stories

#### Story details (keys of `dict`)

* **rank** - the rank of story on the page
* **story_id** - the story's id
* **title** - the title of the story
* **is_self** - true for self/job stories
* **link** - the url it points to (None for self posts)
* **domain** - the domain of the link (None for self posts)
* **points** - the points/karma on the story
* **submitter** - the user who submitted the story
* **submitter_link** - the above user profile link
* **published_time** - the published time ago
* **num_comments** - the number of comments it has
* **comments_link** - the link to the comments page

Usage
=====

See [`example.py`](https://github.com/j7nn7k/designernews_api/blob/master/example.py)

Contribute
==========

New features, or improve existing ones? Send a pull request.
