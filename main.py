from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# 🔑 Sustituye por tu token
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot en dev pero en la rama de git!! 😊")

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos disponibles:\n/start - saludar\n/frase - obtener una frase motivadora")

async def frase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    frases = [
        "El código es poesía.",
        "Divide y vencerás (también en programación).",
        "No cometas el mismo bug dos veces."
    ]
    import random
    await update.message.reply_text(random.choice(frases))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler(["ayuda","help"], ayuda))
app.add_handler(CommandHandler("frase", frase))

print("Bot en marcha... Ctrl+C para detenerlo.")
app.run_polling()
