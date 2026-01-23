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
