import requests
import json
from datetime import datetime

class FacebookGraphAPI:
    """
    Facebook Graph API Implementation for Page Analytics (Robust & Comprehensive)
    - Fetches a wide range of metrics for pages and posts.
    - Gracefully handles unavailable metrics for individual posts.
    - Formats data for both raw archival and clean summary outputs.
    """
    def __init__(self, page_id, page_access_token):
        self.page_id = page_id
        self.page_access_token = page_access_token
        self.base_url = "https://graph.facebook.com/v19.0"

    def get_page_insights_raw(self, period='days_28'):
        """
        Gets the raw, unformatted page-level insights from the API.
        The 'period' parameter (e.g., 'day', 'week', 'days_28') determines the time-series window.
        """
        print("\n--- Fetching Raw Facebook Page-Level Insights ---")
        metrics = 'page_impressions,page_post_engagements,page_fans,page_actions_post_reactions_total'
        url = f"{self.base_url}/{self.page_id}/insights"
        params = {'metric': metrics, 'period': period, 'access_token': self.page_access_token}
        return self._handle_response(requests.get(url, params=params))

    def get_page_posts(self, limit=10):
        """Gets a list of recent posts from the Facebook Page."""
        print("\n--- Fetching Recent Facebook Page Posts ---")
        url = f"{self.base_url}/{self.page_id}/posts"
        params = {'fields': 'id,message,created_time,permalink_url', 'limit': limit, 'access_token': self.page_access_token}
        return self._handle_response(requests.get(url, params=params))

    def get_post_insights(self, post_id):
        """
        Gets all available insights for a specific post by querying metrics individually.
        Uses 'period=lifetime' for total, cumulative stats.
        """
        # A comprehensive list of potential metrics based on documentation.
        all_possible_metrics = [
            'post_impressions', 'post_impressions_unique', 'post_engaged_users', 'post_clicks',
            'post_reactions_like_total', 'post_reactions_love_total', 'post_reactions_wow_total',
            'post_reactions_haha_total', 'post_reactions_sad_total', 'post_reactions_angry_total'
        ]
        
        formatted_insights = {}
        for metric in all_possible_metrics:
            url = f"{self.base_url}/{post_id}/insights"
            params = {'metric': metric, 'period': 'lifetime', 'access_token': self.page_access_token}
            response = requests.get(url, params=params)
            
            insight_data = self._handle_response(response, supress_error_print=True)
            if insight_data and 'data' in insight_data and insight_data['data']:
                value = insight_data['data'][0].get('values', [{}])[0].get('value', 0)
                formatted_insights[metric] = value
            else:
                # If metric is invalid for this post, set to 0 as it's a numeric count.
                formatted_insights[metric] = 0
        
        return formatted_insights
        
    def get_comprehensive_post_analytics(self, post_data):
        """Creates a structured summary for a single post."""
        print(f"--- Analyzing Post ID: {post_data['id']} ---")
        insights = self.get_post_insights(post_data['id'])
        
        return {
            "post_details": post_data,
            "insights": insights,
            "summary": {
                "impressions": insights.get('post_impressions', 0),
                "reach": insights.get('post_impressions_unique', 0),
                "engaged_users": insights.get('post_engaged_users', 0),
                "clicks": insights.get('post_clicks', 0),
                "total_likes": insights.get('post_reactions_like_total', 0)
            }
        }

    def _handle_response(self, response, supress_error_print=False):
        """Shared error handling method."""
        if response.status_code == 200:
            return response.json()
        if not supress_error_print:
            try:
                error_data = response.json()
                print(f"API Error ({response.status_code}): {error_data.get('error', {}).get('message', 'No error message provided.')}")
            except json.JSONDecodeError:
                print(f"API Error ({response.status_code}): {response.text}")
        return None

def setup_api():
    """Replace placeholders with your actual Facebook Page credentials."""
    
        # --- Facebook Credentials ---
    FACEBOOK_PAGE_ID = "654529707751538" #YOUR_FACEBOOK_PAGE_ID
    FACEBOOK_PAGE_ACCESS_TOKEN = "EAAJsRK4bgtYBO83LpCVXdgvdCJJb4rJeTPFvWzEZAQlBlZAfsZCLVjPTGQDRAWHEn3VdmFQ7zOuaBuTgnrgrNIHZBkUrsjlZCEAUB4STf5QEgRdq86CZASZAUZCFIUQXThaWa3hcyt5CjTqBu66bQBPQCEOD8XZCYwsyisNuaJ1jc6zepX3F8eNDDvnlJpEjkGooMf09WwqASrGZCEfKjKaBU1BR4y"     # This is the token you get specifically for your page.

    
    if "YOUR" in FACEBOOK_PAGE_ID or "YOUR" in FACEBOOK_PAGE_ACCESS_TOKEN:
        print("!!! ERROR: Facebook credentials are not set in setup_api() !!!")
        return None
    return FacebookGraphAPI(FACEBOOK_PAGE_ID, FACEBOOK_PAGE_ACCESS_TOKEN)

if __name__ == "__main__":
    print("\n" + "="*25 + " FACEBOOK ANALYTICS " + "="*26)
    fb_api = setup_api()

    if fb_api:
        # --- 1. Fetch Raw Data ---
        raw_page_insights = fb_api.get_page_insights_raw()
        page_posts = fb_api.get_page_posts(limit=3)

        # --- 2. Process and Generate Comprehensive Analytics ---
        comprehensive_analytics = []
        if page_posts and 'data' in page_posts:
            print("\n--- Fetching Comprehensive Insights for each Facebook Post ---")
            for post in page_posts['data']:
                analytics = fb_api.get_comprehensive_post_analytics(post)
                if analytics:
                    comprehensive_analytics.append(analytics)
        
        # --- 3. Format a Clean Summary for Page-Level Insights ---
        clean_page_insights = {}
        if raw_page_insights and 'data' in raw_page_insights:
            for metric in raw_page_insights['data']:
                metric_name = metric['name']
                metric_value = metric.get('values', [{}])[-1].get('value', 0)
                clean_page_insights[metric_name] = metric_value

        # --- 4. Print Clean Data to Terminal ---
        print("\n--- Clean Page-Level Summary ---")
        print(json.dumps(clean_page_insights, indent=4))
        print("\n--- Comprehensive Post Analytics ---")
        print(json.dumps(comprehensive_analytics, indent=4))

        # --- 5. Save the Two Required JSON Files ---
        
        # File 1: The clean, processed data
        clean_data_to_save = {
            "page_level_summary": clean_page_insights,
            "comprehensive_post_analytics": comprehensive_analytics
        }
        with open("facebook_analytics.json", 'w') as f:
            json.dump(clean_data_to_save, f, indent=4)
        print("\n==================================================")
        print("SUCCESS: Clean summary saved to facebook_analytics.json")
        
        # File 2: The full, raw API data
        all_raw_data_to_save = {
            "raw_page_insights": raw_page_insights,
            "page_posts_list": page_posts
        }
        with open("facebook_analytics_all_data.json", 'w') as f:
            json.dump(all_raw_data_to_save, f, indent=4)
        print("SUCCESS: Full raw data saved to facebook_analytics_all_data.json")

        print("==================================================")
