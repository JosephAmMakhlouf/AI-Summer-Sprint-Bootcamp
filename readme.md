# 🌙 AI Dream Interpreter - مفسر الأحلام الذكي

An intelligent Arabic dream interpretation system that combines classical Islamic dream interpretation books with modern AI technology to provide accurate and meaningful dream analysis.

![Dream Interpreter](https://img.shields.io/badge/Language-Arabic-green) ![AI Powered](https://img.shields.io/badge/AI-Gemini%20API-blue) ![Framework](https://img.shields.io/badge/Framework-Flask-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🤖 **AI-Powered Symbol Extraction**: Uses Google Gemini AI to intelligently extract dream symbols from Arabic text
- 📚 **Classical Book Integration**: Processes PDF books of traditional Islamic dream interpretation
- 🔍 **Multi-Level Matching System**:
  - Exact symbol matching
  - Partial/substring matching
  - Semantic similarity matching (using sentence transformers)
  - Synonym matching
  - Fuzzy text matching
- 🌐 **Beautiful Web Interface**: Responsive Arabic RTL interface with mystical theme
- 💾 **Smart Caching**: Automatically caches processed interpretations for faster responses
- 📊 **Confidence Scoring**: Shows match confidence levels and types
- 🔄 **Fallback Systems**: Multiple backup matching methods ensure reliable results

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   PDF Books     │───▶│  Text Extraction │───▶│   AI Processing │
│  (Classical)    │    │   & Chunking     │    │  (Gemini API)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                                         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Interface │◄───│  Dream Analysis  │◄───│  Symbol & Cache │
│    (Flask)      │    │    Engine        │    │   Management    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                    ┌──────────────────────┐
                    │  Multi-Level Matcher │
                    │  • Exact Match       │
                    │  • Semantic Match    │
                    │  • Fuzzy Match       │
                    └──────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key
- PDF books containing Arabic dream interpretations

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-dream-interpreter.git
cd ai-dream-interpreter
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

4. **Prepare your dream books**
```bash
mkdir dreams
# Place your Arabic dream interpretation PDF files in the dreams/ directory
```

5. **Run the application**
```bash
python app.py
```

6. **Access the web interface**
Open your browser and navigate to `http://localhost:5000`

## 📦 Dependencies

```txt
flask==2.3.3
google-generativeai==0.3.2
PyPDF2==3.0.1
python-dotenv==1.0.0
sentence-transformers==2.2.2
torch==2.1.0
```

## 📁 Project Structure

```
ai-dream-interpreter/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── dreams/               # Directory for PDF books
│   ├── book1.pdf
│   ├── book2.pdf
│   └── ...
├── dream_cache.json      # Auto-generated cache file
├── static/               # Static files (optional)
├── templates/            # HTML templates (optional)
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |

### Application Settings

You can modify these constants in `app.py`:

```python
DREAMS_DIR = "dreams"           # Directory containing PDF books
CACHE_FILE = "dream_cache.json" # Cache file location
MODEL_NAME = "gemini-1.5-flash" # Gemini model to use
```

## 🎯 Usage

### Adding Dream Books

1. Place Arabic dream interpretation PDF files in the `dreams/` directory
2. Supported formats: PDF with extractable text
3. Books should contain structured dream interpretations in Arabic

### Using the Web Interface

1. **Access**: Open `http://localhost:5000` in your browser
2. **Input**: Enter your dream in Arabic in the text area
3. **Analysis**: Click "فسر الحلم" (Interpret Dream)
4. **Results**: View categorized interpretations with confidence scores

### API Endpoints

#### `POST /api/interpret`
Interpret a dream text.

**Request:**
```json
{
  "dream": "رأيت في المنام أنني أطير فوق الماء"
}
```

**Response:**
```json
{
  "symbols": ["طيران", "ماء"],
  "interpretations": {
    "طيران": [
      {
        "meaning": "الطيران في المنام يدل على...",
        "source": "كتاب تفسير الأحلام",
        "match_type": "exact",
        "confidence": 1.0
      }
    ]
  },
  "total_entries": 1250
}
```

#### `GET /api/status`
Get system status and statistics.

## 🧠 AI Processing Pipeline

### 1. Symbol Extraction
```python
# The AI extracts key symbols from dream text
symbols = interpreter.extract_dream_symbols(dream_text)
# Result: ["طيران", "ماء", "أم"]
```

### 2. Multi-Level Matching
```python
# Enhanced matching with multiple fallback methods
interpretations = interpreter.find_interpretations_enhanced(symbols)
```

### 3. Confidence Scoring
Each match receives a confidence score based on:
- **Exact Match**: 100% confidence
- **Semantic Match**: 70-99% confidence
- **Partial Match**: 60-80% confidence
- **Fuzzy Match**: 40-60% confidence

## 🎨 Themes

The application comes with a beautiful "Mystic Dreams" theme featuring:

- 🌟 Animated starfield background
- 🌙 Mystical Arabic design elements
- 💫 Gold and navy color scheme
- 📱 Responsive RTL layout
- ✨ Smooth animations and transitions

## 🔍 Troubleshooting

### Common Issues

**1. "No interpretations found" message**
- Ensure PDF books contain Arabic text
- Check if cache file was generated properly
- Verify Gemini API key is valid

**2. PDF extraction fails**
- Make sure PDFs contain extractable text (not scanned images)
- Try different PDF files
- Check file permissions

**3. Semantic matching not working**
- Install sentence-transformers: `pip install sentence-transformers`
- The system will fallback to other matching methods

**4. API key errors**
- Verify your Gemini API key in `.env` file
- Check API quota and usage limits
- Ensure API key has proper permissions

### Debug Mode

Run the application in debug mode:
```bash
python app.py
```

Check logs for detailed error information.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code style
- Add comments for complex Arabic text processing
- Test with various Arabic dream texts
- Update documentation for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Classical Islamic Scholars**: For their invaluable dream interpretation wisdom
- **Google Gemini**: For providing powerful AI language processing
- **Sentence Transformers**: For semantic matching capabilities
- **Arabic NLP Community**: For tools and resources

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/ai-dream-interpreter/issues) page
2. Create a new issue with detailed description
3. Join our [Discord community](https://discord.gg/your-server) for live support

## 🔮 Future Enhancements

- [ ] Support for multiple languages
- [ ] Dream pattern analysis
- [ ] User accounts and dream history
- [ ] Mobile app development
- [ ] Voice input support
- [ ] Dream symbol visualization
- [ ] Integration with more classical books
- [ ] Advanced AI models fine-tuned for Arabic

---

<div align="center">

**Made with ❤️ for the Arabic-speaking community**

[🌟 Star this repo](https://github.com/yourusername/ai-dream-interpreter) • [🐛 Report Bug](https://github.com/yourusername/ai-dream-interpreter/issues) • [💡 Request Feature](https://github.com/yourusername/ai-dream-interpreter/issues)

</div>