from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import asyncio

BOT_TOKEN = "7489397285:AAEuClrePs7RByJL3ST0Secrdd8RlQBdGPo"
CATEGORIES = ["news", "sports", "economy", "politics", "technology","health", "opinion", "human rights", "palestine", "israel", "gaza", "war", "conflict"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the News4LazyDudes Bot!\n\n"
        "Commands:\n"
        "📂 /categories: List all supported categories\n"
        "🔍 /category [category name]: Search Latest news in a specific category\n"
        "🔍 /search [keywords]: Search for specific keywords\n"
        "✏️ Example: /category politics\n"
        "✏️ Example: /search barcelona vs real madrid\n"
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /search [keywords]\nExample: /search barcelona vs real madrid")
        return
    keywords = " ".join(context.args)

    await update.message.reply_text(f"Fetching and summarizing news about *{keywords}*...", parse_mode="Markdown")
    summary = get_summarized_news(keywords)
    translation= get_translated_news(summary)
    await update.message.reply_text(summary+"\nTranslated to Arabic: "+translation, parse_mode="Markdown")

async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(cat.title(), callback_data=f"category_{cat}")]
        for cat in CATEGORIES])
    await update.message.reply_text("📚 Choose a category or tag:", reply_markup=keyboard)

async def handle_category_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data.startswith("category_"):
        selected = query.data.replace("category_", "")
        await query.edit_message_text(f"📂 Fetching news for *{selected.title()}*...", parse_mode="Markdown")
        summary = get_summarized_news(selected)
        translation = get_translated_news(summary)
        await query.message.reply_text(summary + "\nTranslated to Arabic: " + translation, parse_mode="Markdown")

async def category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or context.args.len!=1:
        await update.message.reply_text("Usage: /category [category name]\nExample: /category sports")
        return
    category = context.args[0]
    await update.message.reply_text(f"Fetching and summarizing news about *{category}*...", parse_mode="Markdown")
    summary = get_summarized_category_news(category)
    translation= get_translated_news(summary)
    await update.message.reply_text(summary+"\nTranslated to Arabic: "+translation, parse_mode="Markdown")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("search", search))
app.add_handler(CommandHandler("categories", categories))
app.add_handler(CommandHandler("category", category))
app.add_handler(CallbackQueryHandler(handle_category_button))

print("Bot is running...")
app.run_polling()


######################################################################################
# you can move the below functions to a different file then import it to use it here #
######################################################################################


def get_summarized_news(keywords):
    # Placeholder: scraping or API + LLM summarization
    #else, use the keywords as searching keywords(https://www.aljazeera.com/search/keyword%20keyword%20keyword)
    return f"📰 Here's a fake summary for *{keywords}*. Real content coming soon 😉"

def get_summarized_category_news(category):
    # Use category to search in one of these 2 urls (https://www.aljazeera.com/tag/{category} or https://www.aljazeera.com/{category}
    #   then go to the site, sort by DATE, then scrabe the data
    return f"📰 Here's a fake summary for *{category}*. Real content coming soon 😉"

def get_translated_news(context):
    # Placeholder: translating news using DeepL
    return "translated text sample"

