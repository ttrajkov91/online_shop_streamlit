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
            font-size: 2.75rem !important;
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
        
        .carousel-click-indicator {
            position: absolute;
            bottom: 15px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.6);
            color: #64b5f6;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            opacity: 0.9;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(-8px); }
        }
        
        /* Slick Carousel Style Implementation */
        
        /* Main Carousel Wrapper (slider-1) */
        .carousel-main-wrapper.slider-1 {
            width: 100%;
        }
        
        .carousel-fade-container {
            position: relative;
            width: 100%;
            overflow: hidden;
        }
        
        /* Navigation Carousel Wrapper (slider-2) */
        .carousel-nav-wrapper.slider-2 {
            width: 100%;
            margin-top: 1rem;
        }
        
        /* Fade Transition Effect */
        .carousel-container-image {
            position: relative;
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            overflow: visible;
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
            min-height: 450px;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: fadeIn 1s ease-in-out;
            padding: 2rem;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        .carousel-slide-wrapper {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            animation: fadeInSlick 1s ease-in-out;
        }
        
        @keyframes fadeInSlick {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        
        /* Side Arrows - Large and Visible */
        .carousel-arrow {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            font-size: 48px;
            color: white;
            cursor: pointer;
            padding: 16px 20px;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 8px;
            transition: all 0.3s ease;
            z-index: 100;
            user-select: none;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 60px;
            height: 60px;
            line-height: 1;
        }
        
        .carousel-arrow:hover {
            background: rgba(0, 0, 0, 0.9);
            transform: translateY(-50%) scale(1.15);
            box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
        }
        
        .carousel-arrow::before {
            content: '';
            display: block;
        }
        
        .carousel-arrow-left {
            left: 15px;
        }
        
        .carousel-arrow-left::before {
            content: '❮';
        }
        
        .carousel-arrow-right {
            right: 15px;
        }
        
        .carousel-arrow-right::before {
            content: '❯';
        }
        
        /* Synchronized Indicators (slider-2) */
        .carousel-indicators {
            display: flex;
            justify-content: center;
            gap: 14px;
            padding: 1.5rem 2rem;
            background: rgba(42, 42, 78, 0.6);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            width: fit-content;
            margin: 1rem auto 0;
        }
        
        .carousel-dot {
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.35);
            border: 2px solid rgba(255, 255, 255, 0.6);
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        
        .carousel-dot:hover {
            background: rgba(255, 255, 255, 0.55);
            transform: scale(1.2);
            border-color: rgba(255, 255, 255, 0.9);
        }
        
        .carousel-dot.active {
            background: white;
            border-color: white;
            box-shadow: 0 0 16px rgba(255, 255, 255, 0.9);
            width: 16px;
            height: 16px;
        }
        
        /* Carousel Card */
        .carousel-card {
            background: rgba(26, 26, 46, 0.95);
            border-radius: 12px;
            padding: 2.5rem;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            animation: slideInCard 1s ease;
            max-width: 500px;
            width: 100%;
        }
        
        @keyframes slideInCard {
            from {
                opacity: 0;
                transform: scale(0.95);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        .carousel-badge {
            background: linear-gradient(135deg, #ffc107 0%, #ff8f00 100%);
            color: #1a1a2e;
            padding: 0.6rem 1.4rem;
            border-radius: 25px;
            font-weight: bold;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
            display: inline-block;
            box-shadow: 0 4px 16px rgba(255, 193, 7, 0.4);
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
        
        .carousel-book-image {
            font-size: 6.5rem;
            margin-bottom: 1.5rem;
            text-shadow: 0 4px 12px rgba(0,0,0,0.4);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.08); }
        }
        
        .carousel-book-title {
            font-size: 2rem;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 0.8rem;
            text-shadow: 0 2px 6px rgba(0,0,0,0.4);
        }
        
        .carousel-book-author {
            font-size: 1.1rem;
            color: #cfd8e3;
            margin-bottom: 1rem;
            font-style: italic;
            font-weight: 500;
        }
        
        .carousel-book-category {
            background: rgba(102, 126, 234, 0.85);
            color: white;
            padding: 0.5rem 1.2rem;
            border-radius: 25px;
            font-size: 0.9rem;
            margin: 1rem auto;
            display: inline-block;
            font-weight: 600;
        }
        
        .carousel-book-description {
            font-size: 1rem;
            color: #dce4f0;
            line-height: 1.7;
            margin: 1.5rem 0;
            max-width: 450px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .carousel-book-rating {
            color: #ffc107;
            font-size: 1.1rem;
            margin-bottom: 1.2rem;
            font-weight: bold;
            letter-spacing: 0.5px;
        }
        
        .carousel-book-price {
            font-size: 2.2rem;
            font-weight: bold;
            color: #81c784;
            text-shadow: 0 2px 6px rgba(0,0,0,0.3);
        }
        
        /* W3.CSS Style Carousel */
        .w3-content {
            max-width: 100%;
            position: relative;
            margin: auto;
        }
        
        .w3-display-container {
            position: relative;
        }
        
        .w3-display-bottommiddle {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
        }
        
        .w3-center {
            text-align: center;
        }
        
        .w3-left {
            float: left !important;
        }
        
        .w3-right {
            float: right !important;
        }
        
        .w3-badge {
            background-color: rgba(255, 255, 255, 0.3);
            color: white;
            display: inline-block;
            padding: 8px 12px;
            text-align: center;
            border-radius: 50%;
            margin: 0 4px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .w3-badge.active {
            background-color: #ffc107;
            transform: scale(1.2);
        }
        
        .w3-border {
            border: 2px solid rgba(255, 255, 255, 0.5);
        }
        
        /* Carousel Container */
        .carousel-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
            min-height: 400px;
        }
        
        .carousel-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 0%, rgba(255,255,255,0.1) 50%, transparent 100%);
            animation: shimmer 3s infinite;
        }
        
        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        
        /* Slides */
        .carousel-slide {
            display: none;
            animation: fadeIn 0.5s ease-in-out;
        }
        
        .carousel-slide:first-child {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateX(30px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .carousel-card {
            background: rgba(26, 26, 46, 0.95);
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            margin-bottom: 60px;
        }
        
        .carousel-badge {
            background: linear-gradient(135deg, #ffc107 0%, #ff8f00 100%);
            color: #1a1a2e;
            padding: 0.5rem 1.2rem;
            border-radius: 25px;
            font-weight: bold;
            font-size: 0.85rem;
            margin-bottom: 1.5rem;
            display: inline-block;
            box-shadow: 0 4px 12px rgba(255, 193, 7, 0.3);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .carousel-book-image {
            font-size: 6rem;
            margin-bottom: 1.5rem;
            text-shadow: 0 4px 8px rgba(0,0,0,0.3);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .carousel-book-title {
            font-size: 1.8rem;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 0.8rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .carousel-book-author {
            font-size: 1.2rem;
            color: #b0bec5;
            margin-bottom: 1rem;
            font-style: italic;
        }
        
        .carousel-book-category {
            background: rgba(102, 126, 234, 0.8);
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            margin: 0.8rem auto;
            display: inline-block;
        }
        
        .carousel-book-description {
            font-size: 1rem;
            color: #e0e0e0;
            line-height: 1.6;
            margin: 1.5rem 0;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .carousel-book-rating {
            color: #ffc107;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            font-weight: bold;
        }
        
        .carousel-book-price {
            font-size: 2rem;
            font-weight: bold;
            color: #81c784;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Navigation */
        .carousel-controls {
            padding: 20px;
        }
        
        .carousel-arrow {
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            border: none;
            padding: 12px 16px;
            cursor: pointer;
            font-size: 24px;
            user-select: none;
            transition: all 0.3s ease;
            border-radius: 4px;
        }
        
        .carousel-arrow:hover {
            background-color: rgba(0, 0, 0, 0.8);
            transform: scale(1.1);
        }
        
        .carousel-dots-container {
            margin-top: 20px;
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
