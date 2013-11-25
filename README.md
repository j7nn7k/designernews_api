# Designernews API [![Build Status](https://api.travis-ci.org/j7nn7k/designernews_api.png)](https://travis-ci.org/j7nn7k/designernews_api)


Python API for [Designer News](https://news.layervault.com/). Inspired by the [`HackerNewsAPI`](https://github.com/karan/HackerNewsAPI/)


# Install

Via pip (recommended)

```
pip install designernews_api
```

Or download from [PyPi](https://pypi.python.org/pypi/designernews_api)


# Usage


See [`example.py`](https://github.com/j7nn7k/designernews_api/blob/master/example.py)


# Class `DN`

The class `DN` parses the Designer News page, and builds up all stories.

#### Methods

`get_stories()` - Returns a list of the **top stories** from the home page of Designer News.

`get_stories(story_type='new')`  - Returns a list of the **most recent stories** from the /new page of Designer News.

#### Available values in the `story` dict which is returned by `get_stories()`

* **rank** - the rank of story on the page
* **story_id** - the story's id
* **title** - the title of the story
* **is_self** - no external link but article on designer news
* **link** - the url it points to (None for self posts)
* **domain** - the domain of the link (None for self posts)
* **points** - the points/karma on the story
* **num_comments** - the number of comments of the story


```python
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
```


# Contribute
New features, or improve existing ones? Send a pull request.


# Tests
To run the tests locally just install the requirements by running `pip install -r requirements.txt`.

Then run the command `nosetests` in the command line from within the project's root directory.
