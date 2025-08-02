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

// Smooth scrolling for CTA buttons
function handleCTAClicks() {
    const ctaButtons = document.querySelectorAll('.cta-button');
    
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Add a click animation
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
            
            // Here you would typically handle the purchase flow
            // For demo purposes, we'll show an alert
            setTimeout(() => {
                alert('Redirecting to checkout... (This is a demo)');
            }, 200);
        });
    });
}

// Intersection Observer for animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Animate value points
    const valuePoints = document.querySelectorAll('.value-point');
    valuePoints.forEach((point, index) => {
        point.style.opacity = '0';
        point.style.transform = 'translateY(30px)';
        point.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(point);
    });
    
    // Animate customer images
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

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Handle mobile sticky CTA
    window.addEventListener('scroll', throttle(handleMobileStickyDisplay, 100));
    window.addEventListener('resize', throttle(handleMobileStickyDisplay, 250));
    
    // Initialize CTA click handlers
    handleCTAClicks();
    
    // Initialize scroll animations
    initScrollAnimations();
    
    // Initial check for mobile sticky display
    handleMobileStickyDisplay();
    
    // Add loading fade-in effect
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

// Handle window resize events
window.addEventListener('resize', throttle(() => {
    handleMobileStickyDisplay();
}, 250));