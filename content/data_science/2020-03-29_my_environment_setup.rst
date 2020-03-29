My work-from-home environment setup
###################################

:date: 2020-03-29
:tags: data_science
:slug: my-work-from-home-environment-setup
:authors: I-Kang Ding
:summary: Documenting my environment setup, including shell, text editor, and more.


I have been working as a data scientist for almost 8 years now, and have been working from home majority of the time for the past 5 years. I also started a new job recently and had to set up my new work laptop, so I am using this post to document the environments I use, for future reference:


Standing Desk
-------------

My work place typically provides desks that I can adjust the height between standing and sitting. While I'd love to have the same setup at home, I didn't want to spend upwards of $500 - $1,000 to get full-fledged standing desk, so I'm going with of-the-shelf standing desk using IKEA parts for $22. The drawback is that I can _only_ stand at my desk. (Reference: `A standing desk for $22 <https://alphacolin.com/ikea-standing-desk-for-22-dollars/>`_)


Computer accessories
--------------------

I am not very picky about keyboards, so I've been sticking with Apple's `Magic Keyboard with Numeric Keypad <https://www.apple.com/shop/product/MQ052LL/A/magic-keyboard-with-numeric-keypad-us-english-silver>`_ and `Magic Trackpad 2 <https://www.apple.com/shop/product/MRMF2LL/A/magic-trackpad-2-space-gray>`_.

As for the screen, I find a wide screen super helpful for my own productivity. The one I used is `Dell 3415W 34-in Curved Ultrawide Monitor <https://www.dell.com/en-us/work/shop/dell-ultrasharp-34-curved-ultrawide-monitor-u3415w/apd/210-adtr>`_.


My physical setup looks like below. (Cat is sold separately)

.. image:: https://user-images.githubusercontent.com/7269845/77851142-636f4300-71a5-11ea-9c09-707de8320e48.jpg
    :align: center
    :alt: standing-desk
    :width: 500 px


Shell
-----

I use ``zsh`` shell with `Powerlevel10k <https://github.com/romkatv/powerlevel10k>`_ theme.

I am also storing my dotfiles in a repo. The dotfiles in my home directory are symlinked to my local repo, so I can keep my dotfiles version controlled. The repo available here: `ikding/dotfiles <https://github.com/ikding/dotfiles>`_.


Text editor
-----------

I have been using `Visual Studio code <https://code.visualstudio.com>`_ as my main text editor for a few years now, and has enjoyed the experience a lot. Below are the vscode extensions that I use on a regular basis. (My primary programming language is Python).

* `autoDocstring <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_: Generates python docstrings
* `Code Spell Checker <https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker>`_: Spelling checker for source code
* `GitHub Pull Requests <https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github>`_: Pull Request Provider for GitHub
* `GitLens <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_: Supercharge the Git capabilities built into Visual Studio Code
* `Python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_: Linting, Debugging (multi-threaded, remote), Intellisense, Jupyter Notebooks, code formatting, refactoring, unit tests, snippets, and more.
* `Remote Development <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack>`_: Linting, Debugging (multi-threaded, remote), Intellisense, Jupyter Notebooks, code formatting, refactoring, unit tests, snippets, and more.
* `reStructuredText <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_: reStructuredText language support (RST/ReST linter, preview, IntelliSense and more)
* `Table Formatter <https://marketplace.visualstudio.com/items?itemName=shuworks.vscode-table-formatter>`_: Format table syntax of Markdown, Textile and reStructuredText.
* `vscode-icons <https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons>`_: Icons for Visual Studio Code

Here is a screen shot of my vscode window.

.. image:: https://user-images.githubusercontent.com/7269845/77852673-e5636a00-71ad-11ea-9d80-c73b53e4c466.png
    :align: center
    :alt: vscode-screen-shot
    :width: 500 px
