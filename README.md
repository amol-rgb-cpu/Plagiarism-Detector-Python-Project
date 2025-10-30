# Advanced Single-File Plagiarism Detector

A comprehensive web-based plagiarism detection system built with Flask and Python. This application analyzes a single file against a database of previously uploaded documents, supports multiple file types, and generates detailed plagiarism reports with advanced similarity analysis.

## 🚀 Features

### Core Functionality

  - **Single-File Analysis**: Upload one file to check against ALL previously uploaded documents.
  - **Database Comparison**: Compares against a growing database of previously stored documents.
  - **Multi-Format Support**: Supports **TXT, PDF, DOCX, XLSX, and Images** (PNG, JPG, etc.).
  - **Advanced Text Analysis**: Utilizes **Cosine Similarity** (thematic) and **Sequence Matching** (verbatim) algorithms.
  - **OCR Support**: Extracts text from images using **Tesseract OCR**.
  - **Persistent Storage**: Uses an **SQLite database** to store processed document content for future comparisons.

### User Interface

  - **Modern UI**: Beautiful, responsive design using **Bootstrap 5**.
  - **Tabbed Interface**: Separate tabs for text input, file upload, and reports history.
  - **Comprehensive Analysis**: Provides detailed statistics, common words, and similar sentences found.
  - **Interactive Results**: Features animated progress bars and clear color-coded risk levels.
  - **Export Functionality**: Allows users to download detailed **JSON reports**.

### Report System

  - **Detailed Reports**: Generates comprehensive analysis with suggested revisions and grammatical checks.
  - **Report History**: Users can view and manage all previously generated reports.
  - **Print Support**: Includes print-friendly report layouts for easy documentation.
  - **Risk Assessment**: Classifies results using **CRITICAL, HIGH, MEDIUM,** and **LOW** risk levels.
  - **Recommendations**: Provides targeted suggestions for content improvement and paraphrase strategies.

### Privacy & Security

  - **Local Processing**: All sensitive text analysis is performed locally on the server.
  - **File Cleanup**: Uploaded source files are automatically deleted from the temporary storage area after processing.
  - **Secure Storage**: Document content is stored securely in the local database.
  - **No External APIs**: Guarantees complete privacy protection by avoiding third-party services.

## How It Works

The plagiarism detector uses a robust, two-tiered algorithmic approach to maximize accuracy:

1.  **Cosine Similarity (70% Weight)**: Measures the angle between text vectors, identifying **thematic and semantic similarity** (even if words are paraphrased).
2.  **Sequence Similarity (30% Weight)**: Uses `difflib` to compare word and character sequences, detecting **exact or verbatim duplication**.

The **final similarity score** is calculated as a weighted average of **70% Cosine** and **30% Sequence** results.

## 📦 Installation

### Prerequisites

  - Python 3.8 or higher.
  - **Tesseract OCR** (required for image text extraction).

### Setup Instructions

1.  **Clone or download** this repository to your local machine.

2.  **Install Python dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Tesseract OCR** (for image processing):

      - **Windows**: Download the installer from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki).
      - **macOS**: `brew install tesseract`
      - **Linux**: `sudo apt-get install tesseract-ocr`

4.  **Run the application**:

    ```bash
    python app.py
    ```

5.  **Open your browser** and navigate to `http://localhost:5000`.

### First Run

  - The application will automatically create the required SQLite databases (`plagiarism_detector.db`, `user.db`).
  - The `uploads/` directory will be created automatically.
  - **No additional configuration required.**

## 📖 Usage

### Text Input Method

1.  **Navigate to Text Input tab.**
2.  **Enter Texts**: Paste your original text and the suspected text into the dedicated fields.
3.  **Click Check**: Press **"Check for Plagiarism."**
4.  **View Results**: See detailed similarity analysis with a comprehensive breakdown.

### Single-File Upload Method

1.  **Navigate to File Upload tab.**
2.  **Select File**: Choose one supported file to analyze.
3.  **Upload & Analyze**: Click **"Analyze for Plagiarism."**
4.  **View Results**: Get a comprehensive report comparing the file against all documents currently in the database.
5.  **Document Saved**: Your newly uploaded file is automatically processed and saved to the database for use in all future comparisons.

### Reports Management

1.  **Navigate to Reports tab.**
2.  **View History**: See all generated report summaries and similarity scores.
3.  **Access Details**: Click the eye icon to view the full, detailed report.
4.  **Download**: Export report data as **JSON** files for external use.

## Similarity Levels

| Range | Score | Risk Level | Color Code |
| :---: | :---: | :---: | :---: |
| 0% - 29% | Low | **Original Content** | Green |
| 30% - 59% | Medium | **Low Plagiarism Risk** | Blue |
| 60% - 79% | High | **Moderate Plagiarism Risk** | Yellow |
| 80% - 100% | Critical | **High Plagiarism Risk** | Red |

## API Endpoint

The application provides a REST API endpoint for programmatic plagiarism checks:

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
    "details": "Similarity Score (75.0%) based on 70% Cosine and 30% Sequence weighting."
}
```

## File Structure

```
plagiarism-detector/
├── app.py               # Main Flask application (including core logic and routes)
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── templates/
│   └── index.html       # Main application dashboard
└── static/
     ├── style.css        # Custom CSS styles
     └── script.js        # JavaScript functionality
```

## Technologies Used

  - **Backend**: Python 3.x, Flask
  - **Frontend**: HTML5, CSS3, JavaScript (ES6+)
  - **UI Framework**: Bootstrap 5
  - **Icons**: Font Awesome 6
  - **Algorithms**: Cosine Similarity, Sequence Matching (`difflib`)
  - **Database**: SQLite

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

This tool is for educational and research purposes. While it provides useful similarity analysis, it should **not** be the sole method for determining plagiarism. Always use multiple verification methods and consider the context of the texts being compared.
