/**
 * Elmsnest Homepage JavaScript for Shopify
 * High-conversion wooden bear figurine e-commerce
 */

// Mobile Sticky CTA Management
function handleMobileStickyDisplay() {
    const stickyBar = document.querySelector('.mobile-sticky-cta');
    const heroSection = document.querySelector('.hero');
    const isMobile = window.innerWidth <= 768;
    
    if (!isMobile || !stickyBar || !heroSection) return;
    
    const heroHeight = heroSection.offsetHeight;
    const scrollPosition = window.scrollY;
    
    if (scrollPosition > heroHeight * 0.8) {
        stickyBar.style.display = 'block';
    } else {
        stickyBar.style.display = 'none';
    }
}

// Enhanced Cart Integration for Shopify
function addToCart(variantId) {
    const button = event.target;
    const originalText = button.innerHTML;
    
    // Add visual feedback
    button.style.transform = 'scale(0.95)';
    button.innerHTML = 'Adding...';
    button.disabled = true;
    
    setTimeout(() => {
        button.style.transform = '';
    }, 150);
    
    // Shopify Cart API
    fetch('/cart/add.js', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({
            quantity: 1,
            id: variantId,
            properties: {
                '_custom_message': 'From homepage conversion'
            }
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Success feedback
        button.innerHTML = 'Added! ✓';
        button.style.background = 'linear-gradient(135deg, #28a745, #20c997)';
        
        // Show success animation
        button.style.animation = 'none';
        
        // Redirect to cart after short delay
        setTimeout(() => {
            window.location.href = '/cart';
        }, 1000);
    })
    .catch(error => {
        console.error('Error adding to cart:', error);
        
        // Error handling
        button.innerHTML = 'Try Again';
        button.style.background = 'linear-gradient(135deg, #dc3545, #c82333)';
        button.disabled = false;
        
        // Reset button after delay
        setTimeout(() => {
            button.innerHTML = originalText;
            button.style.background = 'linear-gradient(135deg, #8B4513, #A0522D)';
        }, 2000);
        
        // Fallback: redirect to product page
        setTimeout(() => {
            if (typeof productHandle !== 'undefined') {
                window.location.href = `/products/${productHandle}`;
            }
        }, 3000);
    });
}

// Intersection Observer for scroll animations
function initScrollAnimations() {
    // Check if browser supports Intersection Observer
    if (!('IntersectionObserver' in window)) {
        return;
    }
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                // Unobserve after animation to improve performance
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Animate value points with stagger
    const valuePoints = document.querySelectorAll('.value-point');
    valuePoints.forEach((point, index) => {
        point.style.opacity = '0';
        point.style.transform = 'translateY(30px)';
        point.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(point);
    });
    
    // Animate customer images with stagger
    const customerImages = document.querySelectorAll('.customer-image');
    customerImages.forEach((image, index) => {
        image.style.opacity = '0';
        image.style.transform = 'translateY(30px)';
        image.style.transition = `opacity 0.6s ease ${index * 0.2}s, transform 0.6s ease ${index * 0.2}s`;
        observer.observe(image);
    });
    
    // Animate comparison columns
    const comparisonColumns = document.querySelectorAll('.comparison-column');
    comparisonColumns.forEach((column, index) => {
        column.style.opacity = '0';
        column.style.transform = 'translateY(30px)';
        column.style.transition = `opacity 0.6s ease ${index * 0.3}s, transform 0.6s ease ${index * 0.3}s`;
        observer.observe(column);
    });
    
    // Animate product card
    const productCard = document.querySelector('.product-card');
    if (productCard) {
        productCard.style.opacity = '0';
        productCard.style.transform = 'scale(0.95)';
        productCard.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(productCard);
    }
}

// Performance optimization: Throttle scroll events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Enhanced mobile experience
function optimizeMobileExperience() {
    // Improve touch targets on mobile
    if (window.innerWidth <= 768) {
        const buttons = document.querySelectorAll('.cta-button');
        buttons.forEach(button => {
            button.style.minHeight = '48px';
            button.style.minWidth = '120px';
        });
    }
    
    // Prevent zoom on input focus (if you add forms later)
    const viewport = document.querySelector('meta[name=viewport]');
    if (viewport && window.innerWidth <= 768) {
        viewport.setAttribute('content', 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no');
    }
}

// Google Fonts optimization
function loadGoogleFonts() {
    // Preconnect to Google Fonts
    const preconnectLink = document.createElement('link');
    preconnectLink.rel = 'preconnect';
    preconnectLink.href = 'https://fonts.gstatic.com';
    preconnectLink.crossOrigin = 'anonymous';
    document.head.appendChild(preconnectLink);
    
    // Load Poppins font with display swap
    const fontLink = document.createElement('link');
    fontLink.rel = 'stylesheet';
    fontLink.href = 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap';
    document.head.appendChild(fontLink);
}

// Analytics integration (Google Analytics 4 / Shopify Analytics)
function trackConversion(event, value) {
    // Google Analytics 4
    if (typeof gtag !== 'undefined') {
        gtag('event', event, {
            event_category: 'ecommerce',
            event_label: 'wooden-bear-homepage',
            value: value
        });
    }
    
    // Shopify Analytics
    if (typeof ShopifyAnalytics !== 'undefined') {
        ShopifyAnalytics.lib.track(event, {
            value: value,
            currency: 'USD'
        });
    }
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Core functionality
    window.addEventListener('scroll', throttle(handleMobileStickyDisplay, 100));
    window.addEventListener('resize', throttle(() => {
        handleMobileStickyDisplay();
        optimizeMobileExperience();
    }, 250));
    
    // Initialize features
    initScrollAnimations();
    optimizeMobileExperience();
    
    // Initial checks
    handleMobileStickyDisplay();
    
    // Load fonts asynchronously
    loadGoogleFonts();
    
    // Page load animation
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
    
    // Track page view
    trackConversion('page_view', 0);
});

// Shopify theme events
document.addEventListener('shopify:section:load', function(event) {
    // Reinitialize when sections are loaded via theme customizer
    initScrollAnimations();
    handleMobileStickyDisplay();
});

// Additional utility functions for Shopify
window.ElmsnestHomepage = {
    addToCart: addToCart,
    trackConversion: trackConversion,
    init: function() {
        initScrollAnimations();
        handleMobileStickyDisplay();
        optimizeMobileExperience();
    }
};