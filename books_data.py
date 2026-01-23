import pandas as pd
import os
import random

# Master category mapping - groups raw categories into organized buckets
CATEGORY_MAPPING = {
    "Fiction & Literature": [
        "Fiction", "FICTION", "American fiction", "English fiction", "Science fiction", 
        "Fantasy fiction", "Fantasy", "Historical fiction", "Domestic fiction", 
        "Experimental fiction", "Humorous fiction", "Short stories", "European fiction",
        "Australian fiction", "Czech fiction", "Indic fiction (English)", "Detective and mystery stories",
        "Adventure stories", "Adventure fiction", "Horror tales", "Horror stories", "Horror",
        "Occult fiction", "Young Adult Fiction", "Juvenile Fiction", "JUVENILE FICTION",
        "Children's stories", "Fairy tales", "Chick lit", "Thriller", "Political fiction",
        "Classical fiction"
    ],
    "Fantasy & Science Fiction": [
        "Fantasy", "Fantasy fiction", "Science fiction", "Life on other planets",
        "Interplanetary voyages", "Discworld (Imaginary place)", "Otherland (Imaginary place)",
        "Drenai (Imaginary place)", "Chrestomanci (Fictitious character)"
    ],
    "Mystery & Crime": [
        "Detective and mystery stories", "True Crime", "Crime investigation", "Crime investigations",
        "Organized Crime", "Murder", "Espionage", "Conspiracies"
    ],
    "History & Biography": [
        "Biography & Autobiography", "BIOGRAPHY & AUTOBIOGRAPHY", "History",
        "American essays", "English drama", "Authors", "Historical",
        "Great Britain", "China", "Ireland", "England", "American literature"
    ],
    "Non-Fiction & Reference": [
        "Reference", "Essays", "English essays", "Education", "Study Aids",
        "Mathematics", "Science", "Technology & Engineering", "Business", "Business enterprises",
        "Law", "Medical", "Health & Fitness", "Psychology", "Philosophy"
    ],
    "Self-Help & Personal Development": [
        "Self-help", "Personal development", "Conduct of life", "Leadership",
        "Meditation", "Spiritual life", "Christian life", "Religion",
        "Psychoanalysis and religion", "Buddhism", "Christianity"
    ],
    "Sports, Games & Recreation": [
        "Sports & Recreation", "Games", "Games & Activities", "Photography",
        "Gardening", "Crafts & Hobbies", "Antiques & Collectibles", "Design",
        "Architecture", "House & Home", "Cookery", "Cooking"
    ],
    "Arts & Music": [
        "Music", "Art", "Graphic novels", "Comic books", "Motion pictures",
        "Television", "Dance", "Ballet"
    ],
    "Travel & Nature": [
        "Travel", "Nature", "Gardening", "Pets", "Animals", "Zoology",
        "Environmental sciences", "Ecology", "Foreign Language Study"
    ],
    "Family & Relationships": [
        "Family & Relationships", "Family life", "Parenthood", "Marriage",
        "Friendship", "Love", "Childhood", "Children", "Adolescence",
        "Teenagers"
    ]
}

# Function to load books from CSV
def load_books_from_csv(csv_file="data.csv"):
    """Load books from a CSV file and convert to dictionary format"""
    try:
        # Get the directory where this file is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, csv_file)
        
        # Read CSV file
        df = pd.read_csv(csv_path)
        
        # Define emoji mapping for master categories
        emoji_map = {
            "Fiction & Literature": "📖",
            "Fantasy & Science Fiction": "🚀",
            "Mystery & Crime": "🔍",
            "History & Biography": "📜",
            "Non-Fiction & Reference": "📚",
            "Self-Help & Personal Development": "💡",
            "Sports, Games & Recreation": "🎮",
            "Arts & Music": "🎨",
            "Travel & Nature": "🌍",
            "Family & Relationships": "❤️"
        }
        
        # Convert dataframe to list of dictionaries
        books = []
        for idx, row in df.iterrows():
            # Get the raw category from CSV
            raw_category = str(row['categories']) if pd.notna(row['categories']) else "Fiction & Literature"
            
            # Map raw category to master category
            master_category = "Fiction & Literature"  # Default
            for master_cat, raw_cats in CATEGORY_MAPPING.items():
                if raw_category in raw_cats:
                    master_category = master_cat
                    break
            
            # Handle missing values
            price = round(random.uniform(9.99, 24.99), 2)  # Generate random price
            rating = float(row['average_rating']) if pd.notna(row['average_rating']) else 4.0
            num_pages = int(row['num_pages']) if pd.notna(row['num_pages']) else 0
            
            book = {
                "id": idx + 1,
                "isbn13": str(row['isbn13']) if pd.notna(row['isbn13']) else "",
                "isbn10": str(row['isbn10']) if pd.notna(row['isbn10']) else "",
                "title": str(row['title']) if pd.notna(row['title']) else "Unknown Title",
                "subtitle": str(row['subtitle']) if pd.notna(row['subtitle']) and row['subtitle'] != '' else None,
                "author": str(row['authors']) if pd.notna(row['authors']) else "Unknown Author",
                "category": master_category,  # Use master category instead of raw
                "price": price,
                "rating": rating,
                "description": str(row['description']) if pd.notna(row['description']) else "No description available.",
                "year_published": int(row['published_year']) if pd.notna(row['published_year']) else 2000,
                "thumbnail": str(row['thumbnail']) if pd.notna(row['thumbnail']) else "",
                "num_pages": num_pages,
                "ratings_count": int(row['ratings_count']) if pd.notna(row['ratings_count']) else 0,
                "image": emoji_map.get(master_category, "📕")
            }
            books.append(book)
        
        return books
    except FileNotFoundError:
        print(f"CSV file not found at {csv_path}. Using fallback data.")
        return get_fallback_books()
    except Exception as e:
        print(f"Error loading CSV: {e}. Using fallback data.")
        return get_fallback_books()

# Fallback data if CSV is not available
def get_fallback_books():
    """Fallback static book data"""
    return [
        {
            "id": 1,
            "isbn13": "9780000000000",
            "isbn10": "0000000000",
            "title": "Dune",
            "subtitle": None,
            "author": "Frank Herbert",
            "category": "Fantasy & Science Fiction",
            "price": 18.99,
            "rating": 4.8,
            "image": "🚀",
            "description": "An epic space opera about politics, religion, and ecology on a desert planet.",
            "year_published": 1965,
            "thumbnail": "",
            "num_pages": 688,
            "ratings_count": 50000
        },
    ]

# Load books from CSV file
BOOKS_CATALOG = load_books_from_csv()

# Get unique master categories (these are now organized groups)
CATEGORIES = sorted(list(set([book['category'] for book in BOOKS_CATALOG])))
