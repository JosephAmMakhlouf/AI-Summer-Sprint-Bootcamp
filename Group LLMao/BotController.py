from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

BOT_TOKEN = "7489397285:AAEuClrePs7RByJL3ST0Secrdd8RlQBdGPo"

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /news [category] or /news [keywords]\nExample: /news football, /news barcelona vs real madrid, etc.")
        return
    keywords = " ".join(context.args)

    await update.message.reply_text(f"Fetching and summarizing news about *{keywords}*...", parse_mode="Markdown")
    summary = get_summarized_news( keywords)
    await update.message.reply_text(summary, parse_mode="Markdown")

def get_summarized_news(keywords):
    # Placeholder: scraping or API + LLM summarization
    #if category is found(https://www.aljazeera.com/tag/category or https://www.aljazeera.com/category doesn't give PAGE NOT FOUND)
    #then go to the site, sort by DATE, then scrabe the data
    #else, use the keywords as searching keywords(https://www.aljazeera.com/search/keyword%20keyword%20keyword)
    return f"📰 Here's a fake summary for *{keywords}*. Real content coming soon 😉"

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("news", news))

print("Bot is running...")
app.run_polling()
