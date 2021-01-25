"""
Embedded tweet plugin for Pelican
=================================

This plugin allows you to embed Twitter tweets into your articles.
And also provides a link for Twitter username.

    i.e.

        t#username

        will be replaced by a link to Twitter username page.

        t#username/status/tweetid

        will be replaced by a `Embedded-tweet`_ API.

.. _Embedded-tweet: https://developer.twitter.com/en/docs/twitter-for-websites/embedded-tweets/overview.html
"""

import re

from pelican import signals


def embed_tweet(instance):
    if not instance._content:
        return

    instance._content = (
        re.sub(
            r"(^|[^/])(t)#(\w{1,15})(\b[^\/])",
            '\\1<a href="https://twitter.com/\\3">@\\3</a>\\4',
            re.sub(
                r"(^|[^/])(t)#(\w{1,15})/status/(\d+)\b",
                (
                    # Check twitter API page for more customization options:
                    # https://developer.twitter.com/en/docs/twitter-for-websites/embedded-tweets/guides/embedded-tweet-parameter-reference
                    # This site is helpful too:
                    # https://github.com/fundor333/pelican-advance-embed-tweet/blob/4b0f39dafb86c5d8b245a5bba2772621c6529f2e/pelican_advance_embed_tweet/advance_embed_tweet.py
                    '\\1<blockquote class="twitter-tweet" align="center" data-conversation="none">'
                    '<a href="https://twitter.com/\\3/status/\\4">Tweet of \\3/\\4</a></blockquote>'
                ),
                instance._content,
            ),
        )
        + '<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>'
    )


def register():
    signals.content_object_init.connect(embed_tweet)
