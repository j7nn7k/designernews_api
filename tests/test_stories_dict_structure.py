from dn import DN


def test_stories_dict_structure():
    """
    This test checks if the scraping worked in general
    by testing if the stories dict is filled with all
    the values one might expect. It might be better to
    check each value in a separate test but to get
    started this will have to do.
    """
    dn = DN()
    for story in dn.get_stories():
        assert type(story['rank']) == str
        assert type(story['story_id']) == unicode
        assert type(story['title']) == unicode
        assert type(story['link']) == unicode
        assert type(story['domain']) == str
        assert type(story['points']) == str
        assert type(story['num_comments']) == str
        assert type(story['is_self']) == bool
