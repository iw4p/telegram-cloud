.. _signing-in:

==========
Signing In
==========

Before working with Telegram's API, you need to get your own API ID and hash:

1. `Login to your Telegram account <https://my.telegram.org/>`_ with the
   phone number of the developer account to use.

2. Click under API Development tools.

3. A *Create new application* window will appear. Fill in your application
   details. There is no need to enter any *URL*, and only the first two
   fields (*App title* and *Short name*) can currently be changed later.

4. Click on *Create application* at the end. Remember that your
   **API hash is secret** and Telegram won't let you revoke it.
   Don't post it anywhere!

.. note::

    This API ID and hash is the one used by *your application*, not your
    phone number. You can use this API ID and hash with *any* phone number
    or even for bot accounts.

Signing In
==========

Now you can signin by running: 

.. code-block:: sh

    tglogin

Enter the ``api_id`` and ``api_hash`` and give it a ``unique name`` for your client, when you want to download/upload any file you need to know you want to send it with which account (maybe you signin multiple accounts).
Also you must enter your phone number, thanks to Telethon it supports 2FA password.
The config files and sessions save in ``~/.telegam-cloud/`` directory.