# Now let's create the JavaScript with the profile popover functionality
js_content = '''class AerospacePortfolio {
    constructor() {
        this.typingPhrase = "Aeronautical Engineer";
        this.profilePopoverVisible = false;
        this.init();
    }

    init() {
        this.setupTypingEffect();
        this.setupProfilePopover();
        this.setupSmoothScrolling();
        this.setupNavbarHighlight();
    }

    setupTypingEffect() {
        const typingElement = document.getElementById('typingText');
        if (!typingElement) return;

        let charIndex = 0;
        const phrase = this.typingPhrase;

        const type = () => {
            if (charIndex <= phrase.length) {
                typingElement.textContent = phrase.substring(0, charIndex);
                charIndex++;
                setTimeout(type, 150);
            }
        };
        
        // Start typing effect after a short delay
        setTimeout(type, 1000);
    }

    setupProfilePopover() {
        const nameElement = document.getElementById('nameClick');
        const popoverElement = document.getElementById('profilePopover');
        
        if (!nameElement || !popoverElement) return;

        // Click handler for showing/hiding popover
        nameElement.addEventListener('click', (e) => {
            e.stopPropagation();
            this.toggleProfilePopover();
        });

        // Click outside to close popover
        document.addEventListener('click', (e) => {
            if (!popoverElement.contains(e.target) && !nameElement.contains(e.target)) {
                this.hideProfilePopover();
            }
        });

        // Prevent popover from closing when clicked
        popoverElement.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.hideProfilePopover();
            }
        });
    }

    toggleProfilePopover() {
        const popoverElement = document.getElementById('profilePopover');
        if (!popoverElement) return;

        if (this.profilePopoverVisible) {
            this.hideProfilePopover();
        } else {
            this.showProfilePopover();
        }
    }

    showProfilePopover() {
        const popoverElement = document.getElementById('profilePopover');
        if (!popoverElement) return;

        popoverElement.classList.remove('hidden');
        // Trigger reflow to ensure the element is rendered
        popoverElement.offsetHeight;
        popoverElement.classList.add('show');
        
        this.profilePopoverVisible = true;
    }

    hideProfilePopover() {
        const popoverElement = document.getElementById('profilePopover');
        if (!popoverElement) return;

        popoverElement.classList.remove('show');
        
        // Hide after transition completes
        setTimeout(() => {
            if (!popoverElement.classList.contains('show')) {
                popoverElement.classList.add('hidden');
            }
        }, 300);
        
        this.profilePopoverVisible = false;
    }

    setupSmoothScrolling() {
        // Smooth scrolling for navigation links
        const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
        
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    const headerHeight = document.querySelector('.header').offsetHeight;
                    const targetPosition = targetElement.offsetTop - headerHeight - 20;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    setupNavbarHighlight() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
        
        window.addEventListener('scroll', () => {
            const scrollPosition = window.scrollY + 100;
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.offsetHeight;
                const sectionId = section.getAttribute('id');
                
                if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === `#${sectionId}`) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        });
    }
}

// Initialize the portfolio when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new AerospacePortfolio();
});

// Add some additional interactive features
document.addEventListener('DOMContentLoaded', () => {
    // Add loading animation
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease-in-out';
    
    window.addEventListener('load', () => {
        document.body.style.opacity = '1';
    });

    // Add scroll-triggered animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationPlayState = 'running';
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll('.timeline-item, .project-card');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.animation = 'fadeInUp 0.6s ease forwards paused';
        observer.observe(el);
    });
});'''

# Save the JavaScript file
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ Created app.js with profile popover functionality")