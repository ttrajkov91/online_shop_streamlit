# HTML Components for BookVibe Application
import streamlit as st

def render_header():
    """Render the header section"""
    st.markdown("""
        <div class="header-container">
            <div class="header-title">📚 BookVibe</div>
            <div class="header-subtitle">Your Gateway to Literary Worlds - Discover, Explore, and Own Your Next Favorite Book</div>
        </div>
    """, unsafe_allow_html=True)

def render_filter_summary(total_books, current_page, total_pages):
    """Render filter summary section"""
    st.markdown(f"""
        <div class="filter-section">
            <div class="filter-title">📊 Results</div>
            Found <strong>{total_books}</strong> books | Page <strong>{current_page}</strong> of <strong>{total_pages if total_pages > 0 else 1}</strong>
        </div>
    """, unsafe_allow_html=True)

def render_product_card(book):
    """Render a single product card"""
    html = f"""
        <div class="product-card">
            <div class="product-image">{book['image']}</div>
            <div class="product-author">by {book['author']}</div>
            <div style="color: #90caf9; font-size: 0.85rem; margin-bottom: 0.5rem;">📅 {book['year_published']}</div>
            <div class="product-category">{book['category']}</div>
            <div class="product-description">{book['description'][:100]}...</div>
            <div class="product-rating">⭐ {book['rating']}/5.0</div>
            <div class="product-price">${book['price']:.2f}</div>
        </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_book_details_header(book):
    """Render book details header"""
    st.markdown(f"""
        <div class="book-preview-modal">
            <div class="book-preview-title">{book['title']}</div>
            {f'<div class="book-preview-subtitle">{book["subtitle"]}</div>' if book.get('subtitle') else ''}
            <div class="book-preview-author">by {book['author']}</div>
        </div>
    """, unsafe_allow_html=True)

def render_book_info_grid(book):
    """Render book information in a grid"""
    info_html = f"""
        <div class="book-info-grid">
            <div class="book-info-item">
                <div class="book-info-label">Category</div>
                <div class="book-info-value">{book['category']}</div>
            </div>
            <div class="book-info-item">
                <div class="book-info-label">Rating</div>
                <div class="book-info-value">⭐ {book['rating']}/5.0</div>
            </div>
            <div class="book-info-item">
                <div class="book-info-label">Price</div>
                <div class="book-info-value" style="color: #81c784;">${book['price']:.2f}</div>
            </div>
            <div class="book-info-item">
                <div class="book-info-label">Published Year</div>
                <div class="book-info-value">{book['year_published']}</div>
            </div>
            <div class="book-info-item">
                <div class="book-info-label">Pages</div>
                <div class="book-info-value">{book.get('num_pages', 'N/A')}</div>
            </div>
            <div class="book-info-item">
                <div class="book-info-label">Ratings Count</div>
                <div class="book-info-value">{book.get('ratings_count', 0):,}</div>
            </div>
        </div>
    """
    st.markdown(info_html, unsafe_allow_html=True)

def render_book_isbn_info(book):
    """Render ISBN information"""
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

def render_book_description(book):
    """Render full book description"""
    st.markdown("#### 📝 Description")
    st.markdown(f"""
        <div class="book-description-full">
            <p>{book['description']}</p>
        </div>
    """, unsafe_allow_html=True)

def render_featured_card(book):
    """Render a featured book card"""
    featured_html = f"""
        <div class="featured-card">
            <div class="featured-badge">⭐ BESTSELLER</div>
            <div class="product-image">{book['image']}</div>
            <div class="product-author">by {book['author']}</div>
            <div class="product-category">{book['category']}</div>
            <div class="product-description">{book['description'][:150]}...</div>
            <div class="product-rating">Rating: ⭐ {book['rating']}/5.0</div>
            <div class="product-price">${book['price']:.2f}</div>
        </div>
    """
    st.markdown(featured_html, unsafe_allow_html=True)

def render_featured_carousel(featured_books, carousel_key="featured_carousel"):
    """Render a sophisticated slideshow carousel with fade effect and synchronized navigation"""
    import time
    
    if not featured_books:
        return None
    
    # Initialize session state for carousel
    if f"{carousel_key}_index" not in st.session_state:
        st.session_state[f"{carousel_key}_index"] = 0
    if f"{carousel_key}_last_update" not in st.session_state:
        st.session_state[f"{carousel_key}_last_update"] = time.time()
    
    # Auto-advance every 3 seconds
    current_time = time.time()
    if current_time - st.session_state[f"{carousel_key}_last_update"] > 3:
        st.session_state[f"{carousel_key}_index"] = (st.session_state[f"{carousel_key}_index"] + 1) % len(featured_books)
        st.session_state[f"{carousel_key}_last_update"] = current_time
        st.rerun()
    
    st.markdown("#### 🌟 Top Featured Picks")
    
    current_book = featured_books[st.session_state[f"{carousel_key}_index"]]
    current_position = st.session_state[f"{carousel_key}_index"] + 1
    
    # Create carousel HTML for current book
    carousel_html = f"""
    <div class="carousel-main-wrapper slider-1">
        <div class="carousel-fade-container">
            <div class="carousel-container-image">
                <div class="carousel-slide-wrapper" style="cursor: pointer;">
                    <div class="carousel-card">
                        <div class="carousel-badge">#{current_position} of {len(featured_books)} • TOP PICK</div>
                        <div class="carousel-book-image">{current_book['image']}</div>
                        <div class="carousel-book-title">{current_book['title']}</div>
                        <div class="carousel-book-author">by {current_book['author']}</div>
                        <div class="carousel-book-category">{current_book['category']}</div>
                        <div class="carousel-book-description">{current_book['description'][:200]}...</div>
                        <div class="carousel-book-rating">⭐ {current_book['rating']}/5.0 • {current_book.get('ratings_count', 0):,} reviews</div>
                        <div class="carousel-book-price">${current_book['price']:.2f}</div>
                    </div>
                </div>
                <div class="carousel-arrow carousel-arrow-left"></div>
                <div class="carousel-arrow carousel-arrow-right"></div>
            </div>
        </div>
    </div>
    """
    
    st.markdown(carousel_html, unsafe_allow_html=True)
    
    # Navigation dots (visual indicators only)
    dots_html = '<div class="carousel-nav-wrapper slider-2"><div class="carousel-indicators">'
    for i in range(len(featured_books)):
        active_class = "active" if i == st.session_state[f"{carousel_key}_index"] else ""
        dots_html += f'<span class="carousel-dot {active_class}" style="cursor: pointer;"></span>'
    dots_html += '</div></div>'
    
    st.markdown(dots_html, unsafe_allow_html=True)
    
    # Auto-advance carousel using Streamlit's rerun
    time.sleep(0.1)
    if current_time - st.session_state[f"{carousel_key}_last_update"] >= 3.0:
        st.session_state[f"{carousel_key}_index"] = (st.session_state[f"{carousel_key}_index"] + 1) % len(featured_books)
        st.session_state[f"{carousel_key}_last_update"] = time.time()
        st.rerun()
    
    return current_book

def render_no_results(category=None):
    """Render no results message"""
    message = f"😔 No books found in {category}. Try selecting a different category!" if category else "😔 No books found. Try adjusting your filters!"
    st.markdown(f"""
        <div class="no-results">
            {message}
        </div>
    """, unsafe_allow_html=True)

def render_info_box(title, content):
    """Render an info box"""
    st.markdown(f"""
        <div class="info-box">
            <div class="info-title">{title}</div>
            <p>{content}</p>
        </div>
    """, unsafe_allow_html=True)
