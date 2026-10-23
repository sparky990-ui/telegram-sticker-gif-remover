import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def delete_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if message and (message.sticker or message.animation):
        try:
            await message.delete()
            print("Deleted sticker/GIF")
        except Exception as e:
            print(f"Delete error: {e}")


def main():
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    app.add_handler(
        MessageHandler(
            filters.Sticker.ALL | filters.ANIMATION,
            delete_media
        )
    )

    print("Sticker/GIF remover is running...")
    app.run_polling(
        drop_pending_updates=True,
        allowed_updates=["message", "channel_post"]
    )


if __name__ == "__main__":
    main()
