import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

BOT_TOKEN = "8361594853:AAEdigwA_lxMUSafYSOGR1RoWC-vJRCKRQw"
ADMIN_ID = 7796277987  

# Приветственное сообщение
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Приветствую тебя! Сюда ты загружаешь свою домашнюю работу по английскому языку. 💡🎓"
    )

# Обработка домашки
async def receive_homework(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    username = f"@{user.username}" if user.username else f"{user.first_name} ({user.id})"
    caption_text = f"От {username}"

    # Документ
    if update.message.document:
        file = update.message.document
        await context.bot.send_document(chat_id=ADMIN_ID, document=file.file_id,
                                        caption=f"📄 {caption_text}")

    # Фото
    elif update.message.photo:
        photo = update.message.photo[-1]
        await context.bot.send_photo(chat_id=ADMIN_ID, photo=photo.file_id,
                                     caption=f"🖼️ {caption_text}")

    # Аудио
    elif update.message.audio:
        audio = update.message.audio
        await context.bot.send_audio(chat_id=ADMIN_ID, audio=audio.file_id,
                                     caption=f"🎵 {caption_text}")

    # Голосовое сообщение
    elif update.message.voice:
        voice = update.message.voice
        await context.bot.send_voice(chat_id=ADMIN_ID, voice=voice.file_id,
                                     caption=f"🎤 {caption_text}")

    # Видео
    elif update.message.video:
        video = update.message.video
        await context.bot.send_video(chat_id=ADMIN_ID, video=video.file_id,
                                     caption=f"🎬 {caption_text}")

    # Кружочек (video note)
    elif update.message.video_note:
        vnote = update.message.video_note
        await context.bot.send_video_note(chat_id=ADMIN_ID, video_note=vnote.file_id)

    # Текст
    else:
        await context.bot.send_message(chat_id=ADMIN_ID,
                                       text=f"📝 {caption_text}:\n{update.message.text or ''}")

    # Ответ ученику
    await update.message.reply_text("✅ Спасибо! Направил твою домашнюю работу преподавателю!")

# Создаём приложение
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, receive_homework))

print("🤖 Бот запущен...")
app.run_polling()

