========================
Telegram-cloud's Documentation
========================

.. .. code-block:: python

..    from telethon.sync import TelegramClient, events

..    with TelegramClient('name', api_id, api_hash) as client:
..       client.send_message('me', 'Hello, myself!')
..       print(client.download_profile_photo('me'))

..       @client.on(events.NewMessage(pattern='(?i).*Hello'))
..       async def handler(event):
..          await event.reply('Hey!')

..       client.run_until_disconnected()


.. * Are you new here? Jump straight into :ref:`installation`!
.. * Looking for the method reference? See :ref:`client-ref`.
.. * Did you upgrade the library? Please read :ref:`changelog`.
.. * Used Telethon before v1.0? See :ref:`compatibility-and-convenience`.
.. * Coming from Bot API or want to create new bots? See :ref:`botapi`.
.. * Need the full API reference? https://tl.telethon.dev/.


What is this?
-------------

It's a python library for Telegram messenger, which can give you an ability to download, upload, and more options to do with your Telegram account on CLI.


How should I use the documentation?
-----------------------------------

If you are getting started with the commands, you should follow the
documentation in order by pressing the "Next" button at the bottom-right
of every page.

You can also use the menu on the left to quickly skip over sections.

.. toctree::
    :hidden:
    :caption: First Steps

    basic/installation
    basic/signing-in
    basic/quick-start

.. toctree::
    :hidden:
    :caption: Full Command Examples

    commands/tglogin
    commands/tgcloud
    commands/tginfo