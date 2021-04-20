from pyrogram import Client, filters
from pyrogram.types import Message

from Akarimusicbot import player
from helpers.decorators import errors
from helpers.filters import sudo_only


@Client.on_message(filters.command(["clear", "clearqueue", "clear_queue", "cq"]) & sudo_only)
@errors
def clear_queue(_, message: Message):
    if player.queue.empty():
        message.reply_text("<b>❌ The queue is empty</b>", quote=False)
    else:
        with player.queue.mutex:
            player.queue.queue.clear()
        message.reply_text("<b>✅ Queue cleared</b>", quote=False)


@Client.on_message(filters.command("queue"))
@errors
def queue(_, message: Message):
    if player.queue.empty():
        message.reply_text("<b>❌ The queue is empty</b>", quote=False)
    else:
        message.reply_text(
            "<b>🔢 Total items in the queue:</b> {}\n\n<b>🔟 First 10 items:</b>\n{}".format(
                player.queue.qsize(),
                "\n".join(
                    [
                        "    <b>—</b> {} ({})".format(
                            '<a href="{}">{}</a>'.format(
                                item["url"],
                                item["title"],
                            ),
                            item["duration"],
                        ) for item in player.queue.queue]
                )
            ),
            quote=False
        )
