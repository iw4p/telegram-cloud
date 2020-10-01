.. _installation:

============
Installation
============

Telegram-cloud is a Python script-library, which means you need to download and install
Python from https://www.python.org/downloads/ if you haven't already. Once
you have Python installed, for downloading the lastest version, run:

.. code-block:: sh

    pip3 install -U telegram-cloud --user


Verification
============

To verify that the library is installed correctly, run the following command:

.. code-block:: sh

    python3 -c "import telegramcloud""

If there's not any error, It means telegram-cloud installed successfully, but if you see invalid syntax error, try installing again.


Optional Dependencies (Source_)
=====================

If cryptg_ is installed, **the library will work a lot faster**, since
encryption and decryption will be made in C instead of Python. If your
code deals with a lot of updates or you are downloading/uploading a lot
of files, you will notice a considerable speed-up (from a hundred kilobytes
per second to several megabytes per second, if your connection allows it).
If it's not installed, pyaes_ will be used (which is pure Python, so it's
much slower).

If aiohttp_ is installed, the library will be able to download
:tl:`WebDocument` media files (otherwise you will get an error).

If hachoir_ is installed, it will be used to extract metadata from files
when sending documents. Telegram uses this information to show the song's
performer, artist, title, duration, and for videos too (including size).
Otherwise, they will default to empty values, and you can set the attributes
manually.

.. note::

    Some of the modules may require additional dependencies before being
    installed through ``pip``. If you have an ``apt``-based system, consider
    installing the most commonly missing dependencies:

    .. code-block:: sh

        apt update
        apt install clang lib{jpeg-turbo,webp}-dev python{,-dev} zlib-dev
        pip install -U --user setuptools
        pip install -U --user telethon cryptg pillow

    Thanks to `@bb010g`_ for writing down this nice list.

.. _Source: https://docs.telethon.dev/en/latest/basic/installation.html#optional-dependencies
.. _cryptg: https://github.com/cher-nov/cryptg
.. _pyaes: https://github.com/ricmoo/pyaes
.. _pillow: https://python-pillow.org
.. _aiohttp: https://docs.aiohttp.org
.. _hachoir: https://hachoir.readthedocs.io
