# Facebook Page & Post Analytics and Insights Extractor 📊

This project is a robust Python script designed to automatically extract, process, and analyze data from the Facebook Graph API. It provides deep insights into Facebook Page performance and individual post engagement, offering both raw API data for archival and structured summaries for quick analysis.

## 🚀 Project Overview

In today's digital landscape, understanding social media performance is crucial for effective marketing and audience engagement. This tool automates the retrieval of key metrics directly from your Facebook Page's data, empowering you to make data-driven decisions.

**Key Features:**
*   **Page-Level Insights:** Fetches metrics like impressions, post engagements, fan growth, and reaction breakdowns.
*   **Post-Level Analytics:** Retrieves detailed data for each post, including reach, clicks, engagement users, and specific reaction types.
*   **Data Structuring:** Organizes data into clean JSON files for easy integration and analysis.
*   **Raw Data Archival:** Saves original API responses for comprehensive historical tracking.
*   **Graceful Error Handling:** Manages API errors and gracefully handles unavailable metrics for individual posts.

## 🔗 Live Demonstration & Portfolio

For a detailed look at the project's implementation, features, challenges, and outcomes, please visit my portfolio:

*   **Facebook Analytics Portfolio:** [https://damilareadekeye.com/works/software/facebook-analytics/](https://damilareadekeye.com/works/software/facebook-analytics/)

## 📋 Features

*   **Page Insights Extraction:** Retrieves core performance metrics over specified time periods (e.g., `days_28`).
    *   `page_impressions`
    *   `page_post_engagements`
    *   `page_fans`
    *   `page_actions_post_reactions_total`
*   **Post Data Retrieval:** Fetches recent posts with details like `id`, `message`, `created_time`, and `permalink_url`.
*   **Comprehensive Post Insights:** Gathers detailed metrics per post:
    *   `post_impressions`, `post_impressions_unique`
    *   `post_engaged_users`
    *   `post_clicks`
    *   `post_reactions_like_total`, `post_reactions_love_total`, `post_reactions_wow_total`, `post_reactions_haha_total`, `post_reactions_sad_total`, `post_reactions_angry_total`
*   **Structured Output:** Generates `facebook_analytics.json` with a summarized overview and `facebook_analytics_all_data.json` containing raw API responses.

## 💡 Technologies & Tools

*   **Language:** Python 3.x
*   **API:** Facebook Graph API (v19.0)
*   **Libraries:**
    *   `requests` for HTTP API calls
    *   `json` for data handling
    *   `datetime` for timestamp management
*   **Development Environment:** Visual Studio Code

## ⚙️ Getting Started

### Prerequisites

1.  **Python 3.x:** Ensure you have Python installed.
2.  **Facebook Page Access Token:** You'll need a valid Page Access Token with necessary permissions to access your Facebook Page data.
3.  **Facebook Page ID:** The unique identifier for the Facebook Page you want to analyze.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/damilarelekanadekeye/Facebook-Page-Post-Analytics-Automated-Data-Extraction-and-Insights.git
    cd Facebook-Page-Post-Analytics-Automated-Data-Extraction-and-Insights
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

### Configuration

1.  **Edit `facebook_analytics.py`:**
    Open the `facebook_analytics.py` file and replace the placeholder credentials in the `setup_api()` function:
    ```python
    FACEBOOK_PAGE_ID = "YOUR_FACEBOOK_PAGE_ID" # Replace with your Page ID
    FACEBOOK_PAGE_ACCESS_TOKEN = "YOUR_FACEBOOK_PAGE_ACCESS_TOKEN" # Replace with your Page Access Token
    ```

### Running the Script

Execute the script from your terminal:

```bash
python facebook_analytics.py
```

The script will fetch the data and save two JSON files in the same directory:
*   `facebook_analytics.json`: Clean, processed data.
*   `facebook_analytics_all_data.json`: Raw API responses.

## ⚠️ Challenges & Solutions

*   **API Rate Limiting:** Facebook's Graph API has rate limits. This script includes basic error handling for non-200 status codes. For production use, implementing robust retry mechanisms with exponential backoff is recommended.
*   **Metric Availability:** Some metrics might not be available for all posts (e.g., older posts, specific content types). The script gracefully handles this by defaulting missing metrics to `0`.
*   **Understanding API Metrics:** Extensive research and testing were required to identify and correctly utilize the relevant Facebook Graph API metrics for comprehensive analysis.

## 📈 Future Enhancements

*   **Automated Scheduling:** Implement a scheduler for regular data fetching (daily, weekly).
*   **Data Visualization:** Integrate with dashboarding tools (e.g., Tableau, Power BI, Streamlit) for visual representation of insights.
*   **Advanced Metrics:** Fetch more granular data like comments and individual reaction types.
*   **Cross-Platform Analysis:** Expand to include analytics from other social media platforms.

## 🤝 Contribution & Support

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

