# Advanced Single-File Plagiarism Detector

A comprehensive web-based plagiarism detection system built with Flask and Python. This application analyzes a single file against a database of previously uploaded documents, supports multiple file types, and generates detailed plagiarism reports with advanced similarity analysis.

## 🚀 Features

### Core Functionality
- **Single-File Analysis**: Upload one file to check against ALL previously uploaded documents
- **Database Comparison**: Compares against growing database of documents
- **Multi-Format Support**: TXT, PDF, DOCX, XLSX, Images (PNG, JPG, etc.)
- **Advanced Text Analysis**: Cosine similarity + sequence matching algorithms
- **OCR Support**: Extract text from images using Tesseract
- **Real-time Processing**: Instant plagiarism detection with detailed breakdowns
- **Persistent Storage**: SQLite database stores all documents for future comparisons

### User Interface
- **Modern UI**: Beautiful, responsive design with Bootstrap 5
- **Tabbed Interface**: Separate tabs for text input, file upload, and reports
- **Comprehensive Analysis**: Detailed statistics, common words, similar sentences
- **Interactive Results**: Animated progress bars and color-coded risk levels
- **Export Functionality**: Download detailed JSON reports

### Report System
- **Detailed Reports**: Comprehensive analysis with recommendations
- **Report History**: View and manage all generated reports
- **Print Support**: Print-friendly report layouts
- **Risk Assessment**: CRITICAL, HIGH, MEDIUM, LOW risk levels
- **Recommendations**: AI-powered suggestions for improvement

### Privacy & Security
- **Local Processing**: All analysis done locally
- **File Cleanup**: Uploaded files are automatically deleted after processing
- **Secure Storage**: Document hashes prevent duplicate storage
- **No External APIs**: Complete privacy protection

## How It Works

The plagiarism detector uses two main algorithms:

1. **Cosine Similarity**: Measures the angle between text vectors in a high-dimensional space
2. **Sequence Similarity**: Uses difflib to compare word sequences between texts

The final similarity score is a weighted average of both methods (70% cosine, 30% sequence).

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Tesseract OCR (for image text extraction)

### Setup Instructions

1. **Clone or download** this repository to your local machine

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR** (for image processing):
   - **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

### First Run
- The application will automatically create the SQLite database
- Uploads directory will be created automatically
- No additional configuration required

## 📖 Usage

### Text Input Method
1. **Navigate to Text Input tab**
2. **Enter Texts**: Paste your original text and suspected text
3. **Click Check**: Press "Check for Plagiarism" or use Ctrl+Enter
4. **View Results**: See detailed similarity analysis with comprehensive breakdown

### Single-File Upload Method
1. **Navigate to File Upload tab**
2. **Select File**: Choose one file to analyze (supports multiple formats)
3. **Upload & Analyze**: Click "Analyze for Plagiarism"
4. **View Results**: Get comprehensive report comparing against all database documents
5. **Document Saved**: Your file is automatically saved to database for future comparisons

### Reports Management
1. **Navigate to Reports tab**
2. **View History**: See all generated reports with similarity scores
3. **Access Details**: Click eye icon to view full report
4. **Download**: Download JSON reports for external use

### Supported File Types
- **Text Files**: .txt
- **Documents**: .pdf, .docx, .doc
- **Spreadsheets**: .xlsx, .xls
- **Images**: .png, .jpg, .jpeg, .gif, .bmp, .tiff (with OCR)

## Similarity Levels

- **0-29%**: Original Content (Green)
- **30-59%**: Low Plagiarism Risk (Blue)
- **60-79%**: Moderate Plagiarism Risk (Yellow)
- **80-100%**: High Plagiarism Risk (Red)

## API Endpoint

The application also provides a REST API endpoint for programmatic access:

```bash
POST /api/check
Content-Type: application/json

{
    "text1": "Your first text here",
    "text2": "Your second text here"
}
```

Response:
```json
{
    "similarity": 0.75,
    "percentage": 75.0,
    "status": "Moderate Plagiarism Risk",
    "color": "warning",
    "cosine_similarity": 78.5,
    "sequence_similarity": 68.2,
    "details": "Cosine Similarity: 78.5%, Sequence Similarity: 68.2%"
}
```

## File Structure

```
plagiarism-detector/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Custom CSS styles
    └── script.js         # JavaScript functionality
```

## Technologies Used

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Algorithms**: Cosine Similarity, Sequence Matching (difflib)

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this plagiarism detector.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for educational and research purposes. While it provides useful similarity analysis, it should not be the sole method for determining plagiarism. Always use multiple verification methods and consider the context of the texts being compared.
