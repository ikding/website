My work from home setup
#######################

:date: 2020-03-29
:tags: data_science
:slug: my-work-from-home-setup
:authors: I-Kang Ding
:summary: Documenting my work-from-home environment setup, including physical office, shell, text editor, and more.


I have been working as a data scientist for almost 8 years now, and have been working from home majority of the time for the past 5 years. I also started a new job recently and had to set up my new work laptop, so I am using this post to document the environments I use, for future reference:


Standing Desk
-------------

My work place provides adjustable standing desk that I can adjust the height between standing and sitting. While I'd love to have the same setup at home, I didn't want to spend upwards of $500 - $1,000 to get full-fledged, adjustable standing desk, so I'm going with off-the-shelf standing desk using IKEA parts for $22. The drawback is that I can *only* stand at my desk. (Reference: `A standing desk for $22 <https://alphacolin.com/ikea-standing-desk-for-22-dollars/>`_)


Computer accessories
--------------------

I've been using with Apple's `Magic Keyboard with Numeric Keypad <https://www.apple.com/shop/product/MQ052LL/A/magic-keyboard-with-numeric-keypad-us-english-silver>`_ and `Magic Trackpad 2 <https://www.apple.com/shop/product/MRMF2LL/A/magic-trackpad-2-space-gray>`_.

As for the external monitor, I find a wide screen super helpful for my own productivity. The one I used is `Dell 3415W 34-in Curved Ultrawide Monitor <https://www.dell.com/en-us/work/shop/dell-ultrasharp-34-curved-ultrawide-monitor-u3415w/apd/210-adtr>`_.


My physical setup looks like below. (Cat is not included in the bundle; sold separately)

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

Here is a screen shot of my vscode window.

.. image:: https://user-images.githubusercontent.com/7269845/77853344-b0591680-71b1-11ea-9488-a67385d67379.png
    :align: center
    :alt: vscode-screen-shot
    :width: 600 px

I have been using `Visual Studio code <https://code.visualstudio.com>`_ as my main text editor for a few years now, and has enjoyed the experience a lot. Below are the vscode extensions that I use on a regular basis.

* `autoDocstring <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_: Generates python docstrings

  .. image:: https://raw.githubusercontent.com/NilsJPWerner/autoDocstring/master/images/demo.gif
    :align: center
    :alt: vscode-autodocstring
    :width: 600 px

* `Code Spell Checker <https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker>`_: Spelling checker for source code

  .. image:: https://raw.githubusercontent.com/streetsidesoftware/vscode-spell-checker/master/packages/client/images/example.gif
    :align: center
    :alt: vscode-spell-checker
    :width: 600 px

* `GitHub Pull Requests <https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github>`_: Pull Request Provider for GitHub

  .. image:: https://github.com/Microsoft/vscode-pull-request-github/raw/master/.readme/demo.gif
    :align: center
    :alt: vscode-pull-request-github
    :width: 600 px

* `GitLens <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_: Supercharge the Git capabilities built into Visual Studio Code

  .. image:: https://raw.githubusercontent.com/eamodio/vscode-gitlens/master/images/docs/gitlens-preview.gif
    :align: center
    :alt: vscode-gitlens
    :width: 600 px

* `Python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_: Linting, Debugging (multi-threaded, remote), Intellisense, Jupyter Notebooks, code formatting, refactoring, unit tests, snippets, and more.

  .. image:: https://raw.githubusercontent.com/microsoft/vscode-python/master/images/ConfigureDebugger.gif
    :align: center
    :alt: vscode-python
    :width: 600 px

* `Remote Development <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack>`_: An extension pack that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set.

  .. image:: https://microsoft.github.io/vscode-remote-release/images/ssh-readme.gif
    :align: center
    :alt: vscode-remote-release
    :width: 600 px

* `reStructuredText <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_: reStructuredText language support (RST/ReST linter, preview, IntelliSense and more)

  .. image:: https://github.com/vscode-restructuredtext/vscode-restructuredtext/raw/master/images/main.gif
    :align: center
    :alt: vscode-restructuredtext
    :width: 600 px

* `Table Formatter <https://marketplace.visualstudio.com/items?itemName=shuworks.vscode-table-formatter>`_: Format table syntax of Markdown, Textile and reStructuredText.

  .. image:: https://raw.githubusercontent.com/shuGH/vscode-table-formatter/master/res/complex_demo.gif
    :align: center
    :alt: vscode-table-formatter
    :width: 600 px

* `vscode-icons <https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons>`_: Icons for Visual Studio Code

  .. image:: https://raw.githubusercontent.com/vscode-icons/vscode-icons/master/images/screenshot.gif
    :align: center
    :alt: vscode-icons
    :width: 600 px
