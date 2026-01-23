import streamlit as st
import pandas as pd
from books_data import BOOKS_CATALOG, CATEGORIES
from styles import CUSTOM_CSS
from components import *
import math

# Page configuration
st.set_page_config(
    page_title="BookVibe - Online Book Shop",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1
if 'wishlist' not in st.session_state:
    st.session_state.wishlist = []
if 'selected_book' not in st.session_state:
    st.session_state.selected_book = None
if 'show_book_details' not in st.session_state:
    st.session_state.show_book_details = False
if 'show_preview' not in st.session_state:
    st.session_state.show_preview = False
if 'preview_book' not in st.session_state:
    st.session_state.preview_book = None
if 'show_search' not in st.session_state:
    st.session_state.show_search = False
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None

# Header
render_header()

# Create navigation with search button
nav_left, nav_right = st.columns([0.88, 0.12])

with nav_left:
    st.write("")  # Spacing

with nav_right:
    if st.button("🔍", help="Search books", key="search_btn", use_container_width=True):
        st.session_state.show_search = not st.session_state.show_search

# Display search box if activated
if st.session_state.show_search:
    st.session_state.search_query = st.text_input(
        "Search books by title or author",
        value=st.session_state.search_query,
        placeholder="Enter book title or author name...",
        label_visibility="collapsed"
    )

# Tabs (not inside columns)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🏪 Shop", "📚 Categories", "⭐ Featured", "📖 About Us", "💬 Contact", "❓ Help"])

# Function to display book details modal
def display_book_details(book, key_prefix=""):
    """Display detailed book information in a modal-style view"""
    st.markdown(f"""
        <div class="book-preview-modal">
            <div class="book-preview-title">{book['title']}</div>
            {f'<div class="book-preview-subtitle">{book["subtitle"]}</div>' if book.get('subtitle') else ''}
            <div class="book-preview-author">by {book['author']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if book.get('thumbnail') and book['thumbnail'] != '':
            st.image(book['thumbnail'], use_column_width=True)
        else:
            st.markdown(f"""
                <div style="text-align: center; font-size: 6rem; padding: 2rem; background: #1a1a2e; border-radius: 8px;">
                    {book['image']}
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Book information grid
        st.markdown("#### 📊 Book Information")
        
        info_col1, info_col2 = st.columns(2)
        
        with info_col1:
            st.markdown(f"""
                <div class="book-info-item">
                    <div class="book-info-label">Category</div>
                    <div class="book-info-value">{book['category']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="book-info-item">
                    <div class="book-info-label">Rating</div>
                    <div class="book-info-value">⭐ {book['rating']}/5.0</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="book-info-item">
                    <div class="book-info-label">Price</div>
                    <div class="book-info-value" style="color: #81c784;">${book['price']:.2f}</div>
                </div>
            """, unsafe_allow_html=True)
        
        with info_col2:
            st.markdown(f"""
                <div class="book-info-item">
                    <div class="book-info-label">Published Year</div>
                    <div class="book-info-value">{book['year_published']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="book-info-item">
                    <div class="book-info-label">Pages</div>
                    <div class="book-info-value">{book.get('num_pages', 'N/A')}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="book-info-item">
                    <div class="book-info-label">Ratings Count</div>
                    <div class="book-info-value">{book.get('ratings_count', 0):,}</div>
                </div>
            """, unsafe_allow_html=True)
        
        # ISBN Information
        if book.get('isbn13') or book.get('isbn10'):
            st.markdown("#### 📖 ISBN Information")
            isbn_col1, isbn_col2 = st.columns(2)
            
            with isbn_col1:
                if book.get('isbn13'):
                    st.markdown(f"""
                        <div class="book-info-item">
                            <div class="book-info-label">ISBN-13</div>
                            <div class="book-info-value">{book['isbn13']}</div>
                        </div>
                    """, unsafe_allow_html=True)
            
            with isbn_col2:
                if book.get('isbn10'):
                    st.markdown(f"""
                        <div class="book-info-item">
                            <div class="book-info-label">ISBN-10</div>
                            <div class="book-info-value">{book['isbn10']}</div>
                        </div>
                    """, unsafe_allow_html=True)
    
    # Description
    st.markdown("#### 📝 Description")
    st.markdown(f"""
        <div class="book-description-full">
            <p>{book['description']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🛒 Add to Cart", key=f"{key_prefix}modal_cart_{book['id']}", use_container_width=True):
            st.session_state.cart.append(book)
            st.success("Added to cart!", icon="✅")
    
    with col2:
        if st.button("❤️ Add to Wishlist", key=f"{key_prefix}modal_wish_{book['id']}", use_container_width=True):
            if book not in st.session_state.wishlist:
                st.session_state.wishlist.append(book)
                st.success("Added to wishlist!", icon="💝")
    
    with col3:
        if st.button("← Back to Shop", key=f"{key_prefix}back_{book['id']}", use_container_width=True):
            st.session_state.show_book_details = False
            st.session_state.selected_book = None
            st.rerun()

# Sidebar - Shop filters and cart (always visible)
st.sidebar.markdown("### � Filters")

# Price range slider
st.sidebar.markdown("#### Price Range")
col1, col2 = st.sidebar.columns(2)
with col1:
    min_price = st.number_input("Min Price ($)", min_value=0, max_value=30, value=0, step=1)
with col2:
    max_price = st.number_input("Max Price ($)", min_value=0, max_value=30, value=30, step=1)

# Ensure min is less than max
if min_price > max_price:
    min_price, max_price = max_price, min_price

# Category filters
st.sidebar.markdown("#### Categories")
selected_categories = []
for category in CATEGORIES:
    if st.sidebar.checkbox(category, value=True):
        selected_categories.append(category)

# Rating filter
st.sidebar.markdown("#### Minimum Rating")
min_rating = st.sidebar.slider("", 0.0, 5.0, 0.0, 0.1)

# Items per page
st.sidebar.markdown("#### Display")
items_per_page = st.sidebar.selectbox("Items per page", [6, 9, 12, 15])

# Sort options
st.sidebar.markdown("#### Sort By")
sort_option = st.sidebar.selectbox(
    "Sort books by", 
    ["Title (A-Z)", "Price (Low to High)", "Price (High to Low)", "Rating (High to Low)", "Rating (Low to High)", "Year (Newest First)", "Year (Oldest First)"]
)

# Get search query from session state
search_query = st.session_state.search_query

# Cart summary in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 🛒 Shopping Cart")
if st.session_state.cart:
    cart_df = pd.DataFrame(st.session_state.cart)
    st.sidebar.write(f"Items: {len(st.session_state.cart)}")
    st.sidebar.write(f"Total: ${sum(book['price'] for book in st.session_state.cart):.2f}")
    
    if st.sidebar.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()
    
    if st.sidebar.button("View Cart Details"):
        st.sidebar.dataframe(cart_df[['title', 'author', 'price']])
else:
    st.sidebar.write("Your cart is empty")

# TAB 1: SHOP - Main catalog with filters
with tab1:
    # Set active tab for tracking
    if 'last_active_tab' not in st.session_state:
        st.session_state.last_active_tab = None
    st.session_state.last_active_tab = 'shop'
    
    st.markdown("### 🏪 Browse Our Collection")
    
    # Filter books based on criteria
    filtered_books = BOOKS_CATALOG.copy()

    # Apply search filter
    if search_query:
        search_query_lower = search_query.lower()
        filtered_books = [
            book for book in filtered_books
            if search_query_lower in book['title'].lower() or 
               search_query_lower in book['author'].lower()
        ]

    # Apply category filter
    if selected_categories:
        filtered_books = [
            book for book in filtered_books
            if book['category'] in selected_categories
        ]

    # Apply price filter
    filtered_books = [
        book for book in filtered_books
        if min_price <= book['price'] <= max_price
    ]

    # Apply rating filter
    filtered_books = [
        book for book in filtered_books
        if book['rating'] >= min_rating
    ]

    # Apply sorting
    if sort_option == "Title (A-Z)":
        filtered_books = sorted(filtered_books, key=lambda x: x['title'].lower())
    elif sort_option == "Price (Low to High)":
        filtered_books = sorted(filtered_books, key=lambda x: x['price'])
    elif sort_option == "Price (High to Low)":
        filtered_books = sorted(filtered_books, key=lambda x: x['price'], reverse=True)
    elif sort_option == "Rating (High to Low)":
        filtered_books = sorted(filtered_books, key=lambda x: x['rating'], reverse=True)
    elif sort_option == "Rating (Low to High)":
        filtered_books = sorted(filtered_books, key=lambda x: x['rating'])
    elif sort_option == "Year (Newest First)":
        filtered_books = sorted(filtered_books, key=lambda x: x['year_published'], reverse=True)
    elif sort_option == "Year (Oldest First)":
        filtered_books = sorted(filtered_books, key=lambda x: x['year_published'])

    # Pagination logic
    total_books = len(filtered_books)
    total_pages = math.ceil(total_books / items_per_page)

    # Ensure current page is valid
    if st.session_state.current_page > total_pages and total_pages > 0:
        st.session_state.current_page = total_pages
    elif st.session_state.current_page < 1:
        st.session_state.current_page = 1

    # Get books for current page
    start_idx = (st.session_state.current_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_books = filtered_books[start_idx:end_idx]

    # Display filter summary
    st.markdown(f"""
        <div class="filter-section">
            <div class="filter-title">📊 Results</div>
            Found <strong>{total_books}</strong> books | Page <strong>{st.session_state.current_page}</strong> of <strong>{total_pages if total_pages > 0 else 1}</strong>
        </div>
    """, unsafe_allow_html=True)

    # Show preview modal if active
    if st.session_state.show_preview and st.session_state.preview_book:
        book = st.session_state.preview_book
        
        # Modal overlay
        st.markdown("""
            <style>
                .modal-overlay {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100vh;
                    background: rgba(0, 0, 0, 0.85);
                    z-index: 9999;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 2rem;
                }
                .modal-content {
                    background: #2a2a4e;
                    max-width: 800px;
                    width: 100%;
                    max-height: 90vh;
                    overflow-y: auto;
                    padding: 2rem;
                    border-radius: 15px;
                    border: 2px solid #667eea;
                    position: relative;
                }
            </style>
        """, unsafe_allow_html=True)
        
        with st.container():
            col_close = st.columns([9, 1])
            with col_close[1]:
                if st.button("✖", key="close_preview_top"):
                    st.session_state.show_preview = False
                    st.session_state.preview_book = None
                    st.rerun()
            
            st.markdown(f"## {book['title']}")
            if book.get('subtitle'):
                st.markdown(f"*{book['subtitle']}*")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if book.get('thumbnail') and book['thumbnail'] != '':
                    st.image(book['thumbnail'], use_column_width=True)
                else:
                    st.markdown(f"""
                        <div style="text-align: center; font-size: 5rem; padding: 1.5rem; background: #1a1a2e; border-radius: 8px;">
                            {book['image']}
                        </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"**Author:** {book['author']}")
                st.markdown(f"**Rating:** ⭐ {book['rating']}/5.0 ({book.get('ratings_count', 0):,} ratings)")
                st.markdown(f"**Price:** 💰 ${book['price']:.2f}")
                st.markdown(f"**Category:** 📚 {book['category']}")
                st.markdown(f"**Published:** 📅 {book['year_published']}")
                if book.get('num_pages'):
                    st.markdown(f"**Pages:** 📖 {book.get('num_pages', 'N/A')}")
                if book.get('isbn13'):
                    st.markdown(f"**ISBN-13:** {book['isbn13']}")
            
            st.markdown("---")
            st.markdown("#### 📝 Description")
            st.write(book['description'][:400] + "..." if len(book['description']) > 400 else book['description'])
            
            st.markdown("---")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                if st.button("🛒 Add to Cart", key=f"preview_cart_{book['id']}", use_container_width=True):
                    st.session_state.cart.append(book)
                    st.success("Added to cart!")
            
            with col2:
                if st.button("❤️ Wishlist", key=f"preview_wish_{book['id']}", use_container_width=True):
                    if book not in st.session_state.wishlist:
                        st.session_state.wishlist.append(book)
                        st.success("Added to wishlist!")
            
            with col3:
                if st.button("📖 Full Details", key=f"preview_full_{book['id']}", use_container_width=True):
                    st.session_state.selected_book = book
                    st.session_state.show_book_details = True
                    st.session_state.show_preview = False
                    st.session_state.preview_book = None
                    st.rerun()
            
            with col4:
                if st.button("✖ Close", key=f"preview_close_{book['id']}", use_container_width=True):
                    st.session_state.show_preview = False
                    st.session_state.preview_book = None
                    st.rerun()
    
    # Check if we need to show book details
    elif st.session_state.show_book_details and st.session_state.selected_book:
        display_book_details(st.session_state.selected_book, key_prefix="shop_")
    else:

        # Display products
        if current_books:
            cols = st.columns(3)
            for idx, book in enumerate(current_books):
                with cols[idx % 3]:
                    # Create clickable title that opens full details
                    if st.button(f"📖 {book['title']}", key=f"title_{book['id']}", use_container_width=True):
                        st.session_state.selected_book = book
                        st.session_state.show_book_details = True
                        st.rerun()
                    
                    st.markdown(f"""
                        <div class="product-card">
                            <div class="product-image">{book['image']}</div>
                            <div class="product-author">by {book['author']}</div>
                            <div class="product-category">{book['category']}</div>
                            <div class="product-description">{book['description'][:100]}...</div>
                            <div class="product-rating">⭐ {book['rating']}/5.0</div>
                            <div class="product-price">${book['price']:.2f}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button("👁️ Quick Preview", key=f"preview_{book['id']}", use_container_width=True):
                        st.session_state.show_preview = True
                        st.session_state.preview_book = book
                        st.rerun()
                    
                    col_cart, col_wish = st.columns(2)
                    with col_cart:
                        if st.button("🛒 Cart", key=f"cart_{book['id']}"):
                            st.session_state.cart.append(book)
                            st.success(f"Added to cart!", icon="✅")
                    with col_wish:
                        if st.button("❤️ Wish", key=f"wish_{book['id']}"):
                            if book not in st.session_state.wishlist:
                                st.session_state.wishlist.append(book)
                                st.success(f"Added to wishlist!", icon="💝")
            
            # Show recommendations when search query returns results
            if search_query and current_books:
                st.markdown("---")
                st.markdown("### 💡 Recommended For You")
                
                # Get the category of the first search result
                first_result_category = current_books[0]['category']
                
                # Get books from the same category (excluding the current search results)
                recommendations = [
                    book for book in BOOKS_CATALOG
                    if book['category'] == first_result_category and book not in current_books
                ]
                
                # Sort by rating to show best recommendations first
                recommendations = sorted(recommendations, key=lambda x: x['rating'], reverse=True)[:6]
                
                if recommendations:
                    st.markdown(f"Based on your search in **{first_result_category}** category, you might also like:")
                    rec_cols = st.columns(3)
                    
                    for idx, book in enumerate(recommendations):
                        with rec_cols[idx % 3]:
                            # Clickable title
                            if st.button(f"📖 {book['title']}", key=f"rec_title_{book['id']}", use_container_width=True):
                                st.session_state.selected_book = book
                                st.session_state.show_book_details = True
                                st.rerun()
                            
                            st.markdown(f"""
                                <div class="product-card">
                                    <div class="product-image">{book['image']}</div>
                                    <div class="product-author">by {book['author']}</div>
                                    <div class="product-category">{book['category']}</div>
                                    <div class="product-description">{book['description'][:100]}...</div>
                                    <div class="product-rating">⭐ {book['rating']}/5.0</div>
                                    <div class="product-price">${book['price']:.2f}</div>
                                </div>
                            """, unsafe_allow_html=True)
                            
                            if st.button("👁️ Quick Preview", key=f"rec_preview_{book['id']}", use_container_width=True):
                                st.session_state.show_preview = True
                                st.session_state.preview_book = book
                                st.rerun()
                            
                            col_cart, col_wish = st.columns(2)
                            with col_cart:
                                if st.button("🛒 Cart", key=f"rec_cart_{book['id']}"):
                                    st.session_state.cart.append(book)
                                    st.success(f"Added to cart!", icon="✅")
                            with col_wish:
                                if st.button("❤️ Wish", key=f"rec_wish_{book['id']}"):
                                    if book not in st.session_state.wishlist:
                                        st.session_state.wishlist.append(book)
                                        st.success(f"Added to wishlist!", icon="💝")
        else:
            st.markdown("""
                <div class="no-results">
                    😔 No books found matching your criteria. Try adjusting your filters!
                </div>
            """, unsafe_allow_html=True)

        # Pagination controls
        if total_pages > 1:
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Create pagination layout: First, Previous, Page Numbers, Next, Last
            pag_col_first, pag_col_prev, pag_cols_container, pag_col_next, pag_col_last = st.columns([0.12, 0.12, 0.52, 0.12, 0.12], gap="small")
            
            # First button (only show if not on first page)
            with pag_col_first:
                if st.session_state.current_page > 1:
                    if st.button("⏮ First", key="page_first", use_container_width=True):
                        st.session_state.current_page = 1
                        st.rerun()
                else:
                    st.write("")  # Empty space when button is not shown
            
            # Previous button (only show if not on first page)
            with pag_col_prev:
                if st.session_state.current_page > 1:
                    if st.button("← Back", key="page_prev", use_container_width=True):
                        st.session_state.current_page -= 1
                        st.rerun()
                else:
                    st.write("")  # Empty space when button is not shown
            
            # Page numbers
            with pag_cols_container:
                pagination_cols = st.columns([1] * min(total_pages, 8), gap="small")
                
                for page_num in range(1, min(total_pages + 1, 9)):
                    with pagination_cols[page_num - 1]:
                        is_current = st.session_state.current_page == page_num
                        if st.button(
                            f"{page_num}",
                            key=f"page_{page_num}",
                            use_container_width=True,
                            disabled=is_current
                        ):
                            st.session_state.current_page = page_num
                            st.rerun()
            
            # Next button (only show if not on last page)
            with pag_col_next:
                if st.session_state.current_page < total_pages:
                    if st.button("Next →", key="page_next", use_container_width=True):
                        st.session_state.current_page += 1
                        st.rerun()
                else:
                    st.write("")  # Empty space when button is not shown
            
            # Last button (only show if not on last page)
            with pag_col_last:
                if st.session_state.current_page < total_pages:
                    if st.button("Last ⏭", key="page_last", use_container_width=True):
                        st.session_state.current_page = total_pages
                        st.rerun()
                else:
                    st.write("")  # Empty space when button is not shown

# TAB 2: CATEGORIES - Browse books by category
with tab2:
    # Reset book details when entering this tab
    if 'last_active_tab' not in st.session_state:
        st.session_state.last_active_tab = None
    
    # If we just switched to this tab, reset book details
    if st.session_state.last_active_tab != 'categories':
        st.session_state.show_book_details = False
        st.session_state.selected_book = None
        st.session_state.last_active_tab = 'categories'
    
    # If a book is selected, display its details
    if st.session_state.show_book_details and st.session_state.selected_book:
        display_book_details(st.session_state.selected_book, key_prefix="cat_")
    else:
        st.markdown("### 📚 Browse by Category")
        
        # Create category buttons in a grid layout (4 columns)
        st.markdown("#### Select Category")
        
        num_cols = 4
        
        # Create rows of category buttons
        for i in range(0, len(CATEGORIES), num_cols):
            cols = st.columns(num_cols)
            for idx, category in enumerate(CATEGORIES[i:i+num_cols]):
                with cols[idx]:
                    # Count books in category
                    cat_count = len([b for b in BOOKS_CATALOG if b['category'] == category])
                    if st.button(f"{category}\n({cat_count} books)", key=f"cat_btn_{category}", use_container_width=True):
                        st.session_state.selected_category = category
                        st.rerun()
        
        if st.session_state.selected_category:
            st.markdown(f"#### 📖 {st.session_state.selected_category} Books")
            
            # Filter books by category only
            category_books = [
                book for book in BOOKS_CATALOG
                if book['category'] == st.session_state.selected_category
            ]
            
            # Sort by rating
            category_books = sorted(category_books, key=lambda x: x['rating'], reverse=True)
            
            if category_books:
                cols = st.columns(3)
                for idx, book in enumerate(category_books):
                    with cols[idx % 3]:
                        # Clickable title
                        if st.button(f"📖 {book['title']}", key=f"cat_title_{book['id']}", use_container_width=True):
                            st.session_state.selected_book = book
                            st.session_state.show_book_details = True
                            st.rerun()
                        
                        st.markdown(f"""
                            <div class="product-card">
                                <div class="product-image">{book['image']}</div>
                                <div class="product-author">by {book['author']}</div>
                                <div style="color: #90caf9; font-size: 0.85rem; margin-bottom: 0.5rem;">📅 {book['year_published']}</div>
                                <div class="product-category">{book['category']}</div>
                                <div class="product-description">{book['description'][:100]}...</div>
                                <div class="product-rating">⭐ {book['rating']}/5.0</div>
                                <div class="product-price">${book['price']:.2f}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button("👁️ Quick Preview", key=f"cat_preview_{book['id']}", use_container_width=True):
                            st.session_state.show_preview = True
                            st.session_state.preview_book = book
                            st.rerun()
                        
                        col_cart, col_wish = st.columns(2)
                        with col_cart:
                            if st.button("🛒 Cart", key=f"cat_cart_{book['id']}"):
                                st.session_state.cart.append(book)
                                st.success(f"Added to cart!", icon="✅")
                        with col_wish:
                            if st.button("❤️ Wish", key=f"cat_wish_{book['id']}"):
                                if book not in st.session_state.wishlist:
                                    st.session_state.wishlist.append(book)
                                    st.success(f"Added to wishlist!", icon="💝")
            else:
                st.markdown(f"""
                    <div class="no-results">
                        😔 No books found in {st.session_state.selected_category}. Try selecting a different category!
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("👆 Select a category above to browse books")

# TAB 3: FEATURED - Bestsellers and top rated books
with tab3:
    # Reset book details when entering this tab
    if st.session_state.last_active_tab != 'featured':
        st.session_state.show_book_details = False
        st.session_state.selected_book = None
        st.session_state.last_active_tab = 'featured'
        
    st.markdown("### ⭐ Featured & Bestsellers")
    
    # Get top rated books
    featured_books = sorted(BOOKS_CATALOG, key=lambda x: x['rating'], reverse=True)[:8]
    
    col1, col2 = st.columns(2)
    
    for idx, book in enumerate(featured_books):
        with col1 if idx % 2 == 0 else col2:
            # Clickable title
            if st.button(f"📖 {book['title']}", key=f"feat_title_{book['id']}", use_container_width=True):
                st.session_state.selected_book = book
                st.session_state.show_book_details = True
                st.rerun()
            
            st.markdown(f"""
                <div class="featured-card">
                    <div class="featured-badge">⭐ BESTSELLER</div>
                    <div class="product-image">{book['image']}</div>
                    <div class="product-author">by {book['author']}</div>
                    <div class="product-category">{book['category']}</div>
                    <div class="product-description">{book['description'][:150]}...</div>
                    <div class="product-rating">Rating: ⭐ {book['rating']}/5.0</div>
                    <div class="product-price">${book['price']:.2f}</div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("👁️ Quick Preview", key=f"featured_preview_{book['id']}", use_container_width=True):
                st.session_state.show_preview = True
                st.session_state.preview_book = book
                st.rerun()
            
            col_cart, col_wish = st.columns(2)
            with col_cart:
                if st.button("🛒 Add to Cart", key=f"featured_cart_{book['id']}"):
                    st.session_state.cart.append(book)
                    st.success(f"Added '{book['title']}' to cart!", icon="✅")
            with col_wish:
                if st.button("❤️ Add to Wishlist", key=f"featured_wish_{book['id']}"):
                    if book not in st.session_state.wishlist:
                        st.session_state.wishlist.append(book)
                        st.success(f"Added to wishlist!", icon="💝")

# TAB 4: ABOUT US
with tab4:
    # Reset book details when entering this tab
    if st.session_state.last_active_tab != 'about':
        st.session_state.show_book_details = False
        st.session_state.selected_book = None
        st.session_state.last_active_tab = 'about'
    st.markdown("### 📖 About BookVibe")
    
    st.markdown("""
        <div class="info-box">
            <div class="info-title">🚀 Our Mission</div>
            <p>At BookVibe, we believe in the transformative power of reading. Our mission is to make quality literature accessible to readers worldwide, 
            fostering a vibrant community of book lovers and lifelong learners.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="info-box">
            <div class="info-title">📚 What We Offer</div>
            <p>
            • <strong>Extensive Catalog:</strong> Thousands of books across all genres and categories<br>
            • <strong>Competitive Pricing:</strong> Best prices on all your favorite titles<br>
            • <strong>Fast Shipping:</strong> Quick and reliable delivery to your doorstep<br>
            • <strong>Customer Support:</strong> Dedicated team ready to help<br>
            • <strong>Quality Assurance:</strong> All books are carefully curated and inspected<br>
            • <strong>Community:</strong> Join thousands of readers sharing recommendations
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="info-box">
            <div class="info-title">✨ Why Choose BookVibe?</div>
            <p>
            We're not just a bookstore - we're a literary community. Whether you're searching for a bestseller, 
            an indie gem, or a classic you've always wanted to read, BookVibe has you covered. Our platform makes 
            discovering your next favorite book effortless with smart recommendations and intuitive browsing.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📕 Books", "10,000+")
    with col2:
        st.metric("👥 Readers", "50,000+")
    with col3:
        st.metric("⭐ Rating", "4.8/5.0")

# TAB 5: CONTACT
with tab5:
    # Reset book details when entering this tab
    if st.session_state.last_active_tab != 'contact':
        st.session_state.show_book_details = False
        st.session_state.selected_book = None
        st.session_state.last_active_tab = 'contact'
    st.markdown("### 💬 Contact Us")
    
    st.markdown("""
        <div class="info-box">
            <div class="info-title">Get in Touch</div>
            <p>Have questions? We'd love to hear from you! Fill out the form below and we'll get back to you shortly.</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Full Name *")
        email = st.text_input("Email Address *")
        subject = st.selectbox("Subject *", ["General Inquiry", "Complaint", "Partnership", "Feedback", "Other"])
        message = st.text_area("Message *", height=150)
        
        submitted = st.form_submit_button("📤 Send Message")
        
        if submitted:
            if name and email and message:
                st.success("Thank you! Your message has been sent successfully. We'll get back to you soon! 📧")
            else:
                st.error("Please fill in all required fields marked with *")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="info-box">
                <div class="info-title">📧 Email</div>
                <p>support@bookvibe.com<br>
                hello@bookvibe.com</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="info-box">
                <div class="info-title">📞 Phone</div>
                <p>+1 (555) 123-4567<br>
                Mon-Fri: 9AM-6PM EST</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="info-box">
                <div class="info-title">📍 Office</div>
                <p>123 Book Street<br>
                New York, NY 10001</p>
            </div>
        """, unsafe_allow_html=True)

# TAB 6: HELP & FAQ
with tab6:
    # Reset book details when entering this tab
    if st.session_state.last_active_tab != 'help':
        st.session_state.show_book_details = False
        st.session_state.selected_book = None
        st.session_state.last_active_tab = 'help'
    st.markdown("### ❓ Help & FAQs")
    
    with st.expander("📦 How long does delivery take?", expanded=False):
        st.write("Standard delivery typically takes 5-7 business days. Express shipping is available for 2-3 day delivery.")
    
    with st.expander("💳 What payment methods do you accept?", expanded=False):
        st.write("We accept all major credit cards, PayPal, Apple Pay, Google Pay, and bank transfers.")
    
    with st.expander("🔄 What is your return policy?", expanded=False):
        st.write("Books can be returned within 30 days of purchase in original condition. We offer a full refund or store credit.")
    
    with st.expander("📚 Do you have a wishlist feature?", expanded=False):
        st.write("Yes! Use the ❤️ button on any book to add it to your wishlist. Access your wishlist anytime from the Featured tab.")
    
    with st.expander("🎁 Do you offer gift cards?", expanded=False):
        st.write("Absolutely! Gift cards are available in denominations from $10 to $500. Perfect for any book lover!")
    
    with st.expander("📧 How can I get book recommendations?", expanded=False):
        st.write("Our AI-powered recommendation engine suggests books based on your browsing and purchase history. You'll also get personalized emails!")
    
    with st.expander("🆓 Is there a membership program?", expanded=False):
        st.write("Yes! Join BookVibe Premium to get discounts, early access to new releases, and exclusive content.")
    
    with st.expander("🔐 Is my data secure?", expanded=False):
        st.write("Your privacy and security are our top priorities. We use industry-standard encryption and never share your data with third parties.")
    
    st.markdown("---")
    
    st.markdown("""
        <div class="info-box">
            <div class="info-title">🤝 Community Guidelines</div>
            <p>
            BookVibe is a community for book lovers. We encourage respectful discussions, honest reviews, 
            and sharing your love of reading. Please be kind to fellow members!
            </p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>© 2026 BookVibe - Your Online Book Store | Made with ❤️ using Streamlit</p>
        <p style="font-size: 0.9rem;">Browse, Filter, and Discover Amazing Books Today!</p>
    </div>
""", unsafe_allow_html=True)
