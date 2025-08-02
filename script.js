// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Timer Functions
function updateTimer() {
    const now = new Date();
    const end = new Date();
    end.setHours(23, 59, 59, 999);
    
    const diff = end - now;
    const hours = Math.floor(diff / (1000 * 60 * 60));
    const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    
    const timerElement = document.getElementById('timer');
    if (timerElement) {
        timerElement.textContent = `20% OFF Ends in ${hours}h ${mins}m`;
    }
}

// Live Counter Functions
function updateLiveCounters() {
    const now = new Date();
    const baseCount = 12847;
    const todayBase = 23;
    
    // Update families count
    const familiesElement = document.getElementById('families');
    if (familiesElement) {
        const increment = Math.floor(now.getMinutes() / 10);
        familiesElement.textContent = (baseCount + increment).toLocaleString();
    }
    
    // Update today's orders
    const todayElement = document.getElementById('today');
    if (todayElement) {
        const todayIncrement = Math.floor(now.getHours() / 2);
        todayElement.textContent = todayBase + todayIncrement;
    }
    
    // Update viewers count
    const viewersElement = document.getElementById('viewers');
    if (viewersElement) {
        const viewersIncrement = Math.floor(Math.random() * 8) + 18;
        viewersElement.textContent = viewersIncrement;
    }
    
    // Update last purchase
    const lastPurchaseElements = document.querySelectorAll('[id*="last-purchase"]');
    const locations = ['Texas', 'California', 'New York', 'Florida', 'Illinois', 'Ohio', 'Georgia', 'Michigan'];
    const times = ['1 min ago', '2 min ago', '3 min ago', '4 min ago', '5 min ago'];
    
    const randomLocation = locations[Math.floor(Math.random() * locations.length)];
    const randomTime = times[Math.floor(Math.random() * times.length)];
    
    lastPurchaseElements.forEach(element => {
        element.textContent = `${randomTime} from ${randomLocation}`;
    });
}

// Live Activity Notifications
function showLiveActivity() {
    const activities = [
        "Sarah from California just ordered a Family Bear",
        "Michael from Texas ordered 2 Custom Bears",
        "Emma from New York just purchased a Wooden Bear",
        "David from Florida ordered a Personalized Bear",
        "Lisa from Oregon just bought a Family Bear",
        "Robert from Michigan ordered a Custom Bear",
        "Jennifer from Arizona just purchased a Bear",
        "Mark from Colorado ordered a Family Bear"
    ];
    
    const times = ["2 minutes ago", "5 minutes ago", "8 minutes ago", "12 minutes ago"];
    
    let notification = document.getElementById('live-notification');
    
    if (!notification) {
        notification = document.createElement('div');
        notification.id = 'live-notification';
        notification.style.cssText = `
            position: fixed;
            bottom: 20px;
            left: 20px;
            background: linear-gradient(135deg, #4CAF50, #45a049);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            font-size: 0.9rem;
            max-width: 300px;
            transform: translateX(-120%);
            transition: transform 0.3s ease;
        `;
        document.body.appendChild(notification);
    }
    
    const randomActivity = activities[Math.floor(Math.random() * activities.length)];
    const randomTime = times[Math.floor(Math.random() * times.length)];
    
    notification.innerHTML = `
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.2rem;">🔥</span>
            <div>
                <div style="font-weight: 600; margin-bottom: 2px;">${randomActivity}</div>
                <div style="font-size: 0.8rem; opacity: 0.9;">${randomTime}</div>
            </div>
        </div>
    `;
    
    notification.style.transform = 'translateX(0)';
    
    setTimeout(() => {
        notification.style.transform = 'translateX(-120%)';
    }, 4000);
}

// Sticky Bar Functions
function closeStickyBar() {
    const stickyBar = document.getElementById('sticky-bar');
    if (stickyBar) {
        stickyBar.style.display = 'none';
    }
}

function showStickyBar() {
    const bar = document.getElementById('sticky-bar');
    const hero = document.querySelector('.hero');
    
    if (!bar || !hero) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            bar.classList.toggle('show', !entry.isIntersecting);
        });
    }, { threshold: 0.1 });
    
    observer.observe(hero);
}

// Mobile CTA Functions
function initMobileCTA() {
    const cta = document.getElementById('mobile-cta');
    const hero = document.querySelector('.hero');
    
    if (!cta || !hero) return;
    
    if (window.innerWidth <= 768) {
        cta.style.display = 'block';
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                cta.style.transform = entry.isIntersecting ? 'translateY(100%)' : 'translateY(0)';
            });
        }, { threshold: 0.1 });
        
        observer.observe(hero);
    }
}

// FAQ Functions
function toggleFAQ(element) {
    const content = element.nextElementSibling;
    const icon = element.querySelector('.faq-icon');
    
    if (content.style.maxHeight && content.style.maxHeight !== '0px') {
        content.style.maxHeight = '0px';
        content.classList.remove('active');
        icon.textContent = '+';
        icon.style.transform = 'rotate(0deg)';
    } else {
        content.style.maxHeight = content.scrollHeight + 'px';
        content.classList.add('active');
        icon.textContent = '−';
        icon.style.transform = 'rotate(180deg)';
    }
}

// Smooth Scrolling
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute('href'));
            
            if (target) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const stickyBarHeight = document.querySelector('.sticky-bar').offsetHeight;
                const offset = headerHeight + stickyBarHeight + 20;
                
                window.scrollTo({
                    top: target.offsetTop - offset,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Intersection Observer for Animations
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
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.testimonial-card, .comparison-card, .faq-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Form Validation
function initFormValidation() {
    const selects = document.querySelectorAll('select');
    const radios = document.querySelectorAll('input[type="radio"]');
    
    selects.forEach(select => {
        select.addEventListener('change', () => {
            select.style.borderColor = '#4CAF50';
        });
    });
    
    radios.forEach(radio => {
        radio.addEventListener('change', () => {
            const radioGroup = radio.closest('.radio-group');
            if (radioGroup) {
                radioGroup.style.borderColor = '#4CAF50';
            }
        });
    });
}

// Performance Optimization
function initPerformanceOptimizations() {
    // Lazy load images if any
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // Debounce scroll events
    const debouncedScrollHandler = debounce(() => {
        // Handle scroll-based animations
    }, 16);
    
    window.addEventListener('scroll', debouncedScrollHandler);
}

// Analytics and Tracking
function initAnalytics() {
    // Track CTA clicks
    const ctaButtons = document.querySelectorAll('.cta-btn, .product-cta, .btn-large');
    ctaButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            // Track conversion event
            console.log('CTA clicked:', e.target.textContent);
        });
    });
    
    // Track FAQ interactions
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', (e) => {
            const questionText = e.target.querySelector('span').textContent;
            console.log('FAQ opened:', questionText);
        });
    });
}

// Error Handling
function initErrorHandling() {
    window.addEventListener('error', (e) => {
        console.error('JavaScript error:', e.error);
    });
    
    window.addEventListener('unhandledrejection', (e) => {
        console.error('Unhandled promise rejection:', e.reason);
    });
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize all functions
    initSmoothScrolling();
    initScrollAnimations();
    initFormValidation();
    initPerformanceOptimizations();
    initAnalytics();
    initErrorHandling();
    initMobileCTA();
    showStickyBar();
    
    // Start timers and intervals
    updateTimer();
    updateLiveCounters();
    
    // Set up intervals
    setInterval(updateTimer, 60000); // Update timer every minute
    setInterval(updateLiveCounters, 15000); // Update counters every 15 seconds
    setInterval(showLiveActivity, 25000); // Show live activity every 25 seconds
    
    // Show first live activity after 5 seconds
    setTimeout(showLiveActivity, 5000);
    
    // Handle window resize
    window.addEventListener('resize', debounce(() => {
        initMobileCTA();
    }, 250));
    
    // Add loading animation
    document.body.classList.add('loaded');
});

// Export functions for global access
window.closeStickyBar = closeStickyBar;
window.toggleFAQ = toggleFAQ;