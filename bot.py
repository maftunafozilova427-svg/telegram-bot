from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8200127104:AAHOGTkVXrOvPAd3rQJtQJ3ERPaBCObXkKw"

# start komandasi
async def start(update, context):
    await update.message.reply_text(
        "Salom 👋\nIsmingni yoz, men saqlab qo‘yaman 🙂"
    )

# foydalanuvchi yozgan matnni ushlash
async def save_name(update, context):
    name = update.message.text

    # faylga yozish
    with open("users.txt", "a", encoding="utf-8") as file:
        file.write(name + "\n")

    await update.message.reply_text(
        f"Rahmat, {name}! Isming saqlandi ✅"
    )

# botni ishga tushirish
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_name))

print("Bot ishga tushdi...")
app.run_polling()