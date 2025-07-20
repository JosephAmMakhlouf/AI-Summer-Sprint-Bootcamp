from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

BOT_TOKEN = "7489397285:AAEuClrePs7RByJL3ST0Secrdd8RlQBdGPo"

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /news [category] [keywords]\nExample: /news football barcelona vs real madrid")
        return

    category = context.args[0]
    keywords = " ".join(context.args[1:])

    await update.message.reply_text(f"Fetching and summarizing news about *{keywords}* in *{category}*...", parse_mode="Markdown")
    summary = get_summarized_news(category, keywords)
    await update.message.reply_text(summary, parse_mode="Markdown")

def get_summarized_news(category, keywords):
    # Placeholder: scraping or API + LLM summarization
    return f"📰 Here's a fake summary for *{keywords}* in category *{category}*. Real content coming soon 😉"

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("news", news))

print("Bot is running...")
app.run_polling()
