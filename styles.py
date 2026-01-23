# CSS Styling for BookVibe Application
CUSTOM_CSS = """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .main {
            background-color: #1a1a2e;
        }
        
        /* Tab styling */
        [data-testid="stTabs"] {
            background-color: transparent;
        }
        
        [data-testid="stTabs"] [role="tablist"] button {
            font-size: 1.2rem !important;
            padding: 1rem 2rem !important;
            font-weight: bold !important;
            color: #e0e0e0 !important;
            background-color: #2a2a4e !important;
            border: 2px solid #667eea !important;
            border-radius: 8px !important;
            margin-right: 0.5rem !important;
            transition: all 0.3s ease !important;
        }
        
        [data-testid="stTabs"] [role="tablist"] button:hover {
            background-color: #667eea !important;
            color: white !important;
            transform: translateY(-2px) !important;
        }
        
        [data-testid="stTabs"] [role="tablist"] [aria-selected="true"] {
            background-color: #667eea !important;
            color: white !important;
            border-color: #764ba2 !important;
        }
        
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }
        
        .header-title {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .header-subtitle {
            font-size: 1rem;
            opacity: 0.95;
        }
        
        .filter-section {
            background: #2a2a4e;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            border: 1px solid #667eea;
        }
        
        .filter-title {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 1rem;
            color: #64b5f6;
        }
        
        .product-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .product-card {
            background: #2a2a4e;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid #667eea;
        }
        
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);
        }
        
        .product-image {
            font-size: 4rem;
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .product-title {
            font-size: 1.1rem;
            font-weight: bold;
            color: #64b5f6;
            margin-bottom: 0.5rem;
            min-height: 2.5rem;
        }
        
        .product-author {
            font-size: 0.9rem;
            color: #b0bec5;
            margin-bottom: 0.5rem;
        }
        
        .product-category {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            margin-bottom: 1rem;
        }
        
        .product-description {
            font-size: 0.85rem;
            color: #b0bec5;
            margin-bottom: 1rem;
            min-height: 2.5rem;
        }
        
        .product-rating {
            color: #ffc107;
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        
        .product-price {
            font-size: 1.3rem;
            font-weight: bold;
            color: #81c784;
            margin-bottom: 1rem;
        }
        
        .add-to-cart-btn {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.7rem;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: opacity 0.3s ease;
        }
        
        .add-to-cart-btn:hover {
            opacity: 0.9;
        }
        
        .pagination-container {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin-top: 2rem;
            flex-wrap: wrap;
        }
        
        .pagination-btn {
            padding: 0.5rem 1rem;
            border: 1px solid #667eea;
            background: #2a2a4e;
            color: #64b5f6;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .pagination-btn:hover {
            background: #667eea;
            color: white;
        }
        
        .pagination-btn.active {
            background: #667eea;
            color: white;
        }
        
        .no-results {
            text-align: center;
            padding: 3rem;
            font-size: 1.2rem;
            color: #b0bec5;
        }
        
        .sidebar-section {
            margin-bottom: 1.5rem;
        }
        
        .sidebar-title {
            font-weight: bold;
            font-size: 1rem;
            color: #64b5f6;
            margin-bottom: 0.8rem;
        }
        
        .info-box {
            background: #2a2a4e;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            margin-bottom: 1.5rem;
            border-left: 4px solid #667eea;
        }
        
        .info-title {
            font-size: 1.3rem;
            font-weight: bold;
            color: #64b5f6;
            margin-bottom: 0.8rem;
        }
        
        .info-box p {
            color: #b0bec5;
            font-size: 1rem;
            line-height: 1.6;
        }
        
        .contact-form {
            background: #2a2a4e;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        }
        
        .featured-card {
            background: #2a2a4e;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            border: 2px solid #ffc107;
            margin-bottom: 1rem;
        }
        
        .featured-badge {
            background: #ffc107;
            color: #1a1a2e;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 0.8rem;
            font-size: 0.9rem;
        }
        
        /* Book Preview Modal */
        .book-preview-modal {
            background: #2a2a4e;
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid #667eea;
            margin: 1rem 0;
        }
        
        .book-preview-header {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
            gap: 1.5rem;
        }
        
        .book-preview-image {
            max-width: 150px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        
        .book-preview-title {
            font-size: 1.8rem;
            font-weight: bold;
            color: #64b5f6;
            margin-bottom: 0.5rem;
        }
        
        .book-preview-subtitle {
            font-size: 1.2rem;
            color: #90caf9;
            margin-bottom: 0.5rem;
        }
        
        .book-preview-author {
            font-size: 1.1rem;
            color: #b0bec5;
        }
        
        .book-info-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin: 1.5rem 0;
        }
        
        .book-info-item {
            background: #1a1a2e;
            padding: 1rem;
            border-radius: 8px;
            border-left: 3px solid #667eea;
        }
        
        .book-info-label {
            font-size: 0.85rem;
            color: #90caf9;
            margin-bottom: 0.3rem;
        }
        
        .book-info-value {
            font-size: 1.1rem;
            color: #e0e0e0;
            font-weight: bold;
        }
        
        .book-description-full {
            background: #1a1a2e;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1rem 0;
            border-left: 3px solid #667eea;
        }
        
        .book-description-full p {
            color: #b0bec5 !important;
            line-height: 1.8;
            font-size: 1rem;
        }
        
        /* Expander styling */
        [data-testid="stExpander"] {
            background-color: #2a2a4e !important;
            border: 1px solid #667eea !important;
        }
        
        [data-testid="stExpander"] summary {
            color: #64b5f6 !important;
            font-size: 1.1rem !important;
            font-weight: bold !important;
        }
        
        /* General text color fixes */
        p, li, span {
            color: #b0bec5 !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #64b5f6 !important;
        }
        
        /* Input styling */
        input, textarea, select {
            background-color: #1a1a2e !important;
            color: #e0e0e0 !important;
            border: 1px solid #667eea !important;
        }
        
        input::placeholder {
            color: #666 !important;
        }
    </style>
"""
