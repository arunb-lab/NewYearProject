import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_quotes():
    """Scrape quotes from quotes.toscrape.com"""
    url = "http://quotes.toscrape.com/"
    
    try:
        print(f"\nFetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        print(f"Found {len(quotes)} quotes!\n")
        print("="*80)
        
        scraped_data = []
        
        for i, quote in enumerate(quotes, 1):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            print(f"\nQuote #{i}:")
            print(f"Text: {text}")
            print(f"Author: {author}")
            print(f"Tags: {', '.join(tags)}")
            print("-"*80)
            
            scraped_data.append({
                'quote': text,
                'author': author,
                'tags': ', '.join(tags)
            })
        
        return scraped_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return []

def scrape_news_headlines():
    """Scrape headlines from a simple news site"""
    url = "http://quotes.toscrape.com/tag/inspirational/"
    
    try:
        print(f"\nFetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        
        print(f"Found {len(quotes)} inspirational quotes!\n")
        print("="*80)
        
        for i, quote in enumerate(quotes, 1):
            print(f"{i}. {quote.text}")
        
        print("="*80)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")

def save_to_csv(data, filename):
    """Save scraped data to CSV file"""
    if not data:
        print("No data to save!")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename}_{timestamp}.csv"
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        print(f"\n✓ Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def display_menu():
    """Display the main menu"""
    print("\n" + "="*80)
    print(" "*25 + "WEB SCRAPER CLI")
    print("="*80)
    print("\n1. Scrape Quotes (quotes.toscrape.com)")
    print("2. Scrape Inspirational Quotes")
    print("3. Save Last Scraped Data to CSV")
    print("4. Exit")
    print("\n" + "="*80)

def main():
    """Main function to run the scraper"""
    last_scraped_data = []
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            last_scraped_data = scrape_quotes()
        
        elif choice == '2':
            scrape_news_headlines()
        
        elif choice == '3':
            if last_scraped_data:
                save_to_csv(last_scraped_data, 'scraped_quotes')
            else:
                print("\nNo data to save! Please scrape some data first (Option 1).")
        
        elif choice == '4':
            print("\nThank you for using Web Scraper CLI!")
            print("Goodbye! 👋\n")
            break
        
        else:
            print("\n❌ Invalid choice! Please enter a number between 1-4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()