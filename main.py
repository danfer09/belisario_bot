from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv
from pathlib import Path

# cargar ruta actual
current_path = Path(__file__).resolve().parent 

# Cargar ruta .env
env_path = current_path / ".env"

# --- 1️⃣ Cargar variables del archivo .env si existe (solo en local)
if os.path.exists(env_path):
    load_dotenv()
    print("🔹 Archivo .env cargado (modo local)")
else:
    print("⚙️ Usando variables de entorno del sistema (Render u otro servidor)")

# --- 2️⃣ Leer la variable TOKEN del entorno (ya sea del .env o del sistema)
TOKEN = os.getenv("TOKEN")

# --- 3️⃣ Verificar que realmente se haya cargado
if not TOKEN:
    raise ValueError("❌ No se encontró TOKEN en el entorno ni en .env")

print("✅ Token cargado correctamente:", TOKEN[:10] + "..." if TOKEN else "(vacío)")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot! 😊")

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
