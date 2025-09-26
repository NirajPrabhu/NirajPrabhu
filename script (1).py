# Updated JavaScript file with enhanced Formspree form handling
js_content = """// Professional Aerospace Portfolio JavaScript - Enhanced with Formspree Integration

class AerospacePortfolio {
    constructor() {
        this.currentTypeIndex = 0;
        this.isTyping = false;
        this.typingPhrases = [
            "Aeronautical Engineer"
        ];
        
        this.initializeApp();
    }

    initializeApp() {
        try {
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => this.init());
            } else {
                this.init();
            }
        } catch (error) {
            console.error('Failed to initialize application:', error);
        }
    }

    init() {
        try {
            this.setupNavigation();
            this.setupScrollEffects();
            this.setupTypingAnimation();
            this.setupAnimationObservers();
            this.setupSkillsAnimation();
            this.setupProjectCards();
            this.setupContactForm();
            this.setupMobileMenu();
            this.startInitialAnimations();
        } catch (error) {
            console.error('Initialization error:', error);
        }
    }

    // Navigation Setup
    setupNavigation() {
        try {
            this.navbar = document.getElementById('navbar');
            this.navLinks = document.querySelectorAll('.nav-link');
            this.lastScrollY = window.scrollY;
            
            if (!this.navbar || this.navLinks.length === 0) {
                console.warn('Navigation elements not found');
                return;
            }
            
            this.navLinks.forEach(link => {
                link.addEventListener('click', (e) => {
                    try {
                        e.preventDefault();
                        const targetId = link.getAttribute('href').substring(1);
                        this.scrollToSection(targetId);
                        this.updateActiveNavLink(targetId);
                        
                        // Close mobile menu if open
                        const navMenu = document.getElementById('navMenu');
                        if (navMenu && navMenu.classList.contains('active')) {
                            navMenu.classList.remove('active');
                        }
                    } catch (error) {
                        console.error('Navigation click error:', error);
                    }
                });
            });

            // Scroll handling with throttling
            window.addEventListener('scroll', this.throttle(() => {
                try {
                    this.handleNavbarScroll();
                    this.updateScrollProgress();
                    this.updateActiveNavLink();
                } catch (error) {
                    console.error('Scroll handling error:', error);
                }
            }, 16));
        } catch (error) {
            console.error('Navigation setup error:', error);
        }
    }

    handleNavbarScroll() {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > this.lastScrollY && currentScrollY > 100) {
            this.navbar.classList.add('hidden');
        } else {
            this.navbar.classList.remove('hidden');
        }
        
        this.lastScrollY = currentScrollY;
    }

    scrollToSection(targetId) {
        try {
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                const navbarHeight = this.navbar ? this.navbar.offsetHeight : 0;
                const targetPosition = targetSection.offsetTop - navbarHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        } catch (error) {
            console.error('Scroll to section error:', error);
        }
    }

    updateScrollProgress() {
        try {
            const scrollProgress = document.getElementById('scrollProgress');
            if (!scrollProgress) return;
            
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            
            scrollProgress.style.width = `${Math.min(scrollPercent, 100)}%`;
        } catch (error) {
            console.error('Scroll progress error:', error);
        }
    }

    updateActiveNavLink(activeId = null) {
        try {
            if (!activeId) {
                const sections = document.querySelectorAll('section[id]');
                const scrollPos = window.scrollY + 100;
                
                sections.forEach(section => {
                    const sectionTop = section.offsetTop;
                    const sectionHeight = section.offsetHeight;
                    
                    if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                        activeId = section.id;
                    }
                });
            }
            
            this.navLinks.forEach(link => {
                const linkTarget = link.getAttribute('href').substring(1);
                if (linkTarget === activeId) {
                    link.classList.add('active');
                } else {
                    link.classList.remove('active');
                }
            });
        } catch (error) {
            console.error('Active nav link update error:', error);
        }
    }

    // Scroll Effects
    setupScrollEffects() {
        try {
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate-in');
                    }
                });
            }, observerOptions);

            document.querySelectorAll('.timeline-item, .project-card, .skill-item, .stat-item').forEach(el => {
                observer.observe(el);
            });
        } catch (error) {
            console.error('Scroll effects setup error:', error);
        }
    }

    // Typing Animation
    setupTypingAnimation() {
        try {
            const typingElement = document.getElementById('typingText');
            if (!typingElement) return;

            let currentPhraseIndex = 0;
            let currentCharIndex = 0;
            let isDeleting = false;
            let typingSpeed = 100;

            const typeText = () => {
                try {
                    const currentPhrase = this.typingPhrases[currentPhraseIndex];
                    
                    if (isDeleting) {
                        typingElement.textContent = currentPhrase.substring(0, currentCharIndex - 1);
                        currentCharIndex--;
                        typingSpeed = 50;
                    } else {
                        typingElement.textContent = currentPhrase.substring(0, currentCharIndex + 1);
                        currentCharIndex++;
                        typingSpeed = 100;
                    }

                    if (!isDeleting && currentCharIndex === currentPhrase.length) {
                        typingSpeed = 2000;
                        isDeleting = true;
                    } else if (isDeleting && currentCharIndex === 0) {
                        isDeleting = false;
                        currentPhraseIndex = (currentPhraseIndex + 1) % this.typingPhrases.length;
                        typingSpeed = 500;
                    }

                    setTimeout(typeText, typingSpeed);
                } catch (error) {
                    console.error('Typing animation error:', error);
                }
            };

            typeText();
        } catch (error) {
            console.error('Typing animation setup error:', error);
        }
    }

    // Animation Observers
    setupAnimationObservers() {
        try {
            // Counter animation
            const counters = document.querySelectorAll('.stat-number[data-target]');
            const counterObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        this.animateCounter(entry.target);
                        counterObserver.unobserve(entry.target);
                    }
                });
            });

            counters.forEach(counter => counterObserver.observe(counter));
        } catch (error) {
            console.error('Animation observers setup error:', error);
        }
    }

    animateCounter(counter) {
        try {
            const target = parseInt(counter.getAttribute('data-target'));
            const increment = target / 50;
            let current = 0;

            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                counter.textContent = Math.ceil(current);
            }, 40);
        } catch (error) {
            console.error('Counter animation error:', error);
        }
    }

    // Skills Animation
    setupSkillsAnimation() {
        try {
            const skillBars = document.querySelectorAll('.skill-progress[data-progress]');
            const skillsObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const progress = entry.target.getAttribute('data-progress');
                        setTimeout(() => {
                            entry.target.style.width = `${progress}%`;
                        }, 200);
                        skillsObserver.unobserve(entry.target);
                    }
                });
            });

            skillBars.forEach(bar => skillsObserver.observe(bar));
        } catch (error) {
            console.error('Skills animation setup error:', error);
        }
    }

    // Project Cards
    setupProjectCards() {
        try {
            const projectCards = document.querySelectorAll('.project-card');
            
            projectCards.forEach(card => {
                card.addEventListener('mouseenter', () => {
                    card.style.transform = 'translateY(-8px)';
                });
                
                card.addEventListener('mouseleave', () => {
                    card.style.transform = 'translateY(0)';
                });
            });
        } catch (error) {
            console.error('Project cards setup error:', error);
        }
    }

    // Enhanced Contact Form with Formspree Integration
    setupContactForm() {
        try {
            const contactForm = document.getElementById('contactForm');
            const submitBtn = document.getElementById('submitBtn');
            const formMessage = document.getElementById('formMessage');
            
            if (!contactForm) {
                console.warn('Contact form not found');
                return;
            }

            contactForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                
                try {
                    // Show loading state
                    this.setFormLoading(true);
                    this.hideFormMessage();
                    
                    // Get form data
                    const formData = new FormData(contactForm);
                    
                    // Validate form
                    if (!this.validateForm(formData)) {
                        this.setFormLoading(false);
                        this.showFormMessage('Please fill in all required fields.', 'error');
                        return;
                    }
                    
                    // Submit to Formspree
                    const response = await fetch('https://formspree.io/f/xzzjzwda', {
                        method: 'POST',
                        body: formData,
                        headers: {
                            'Accept': 'application/json'
                        }
                    });
                    
                    if (response.ok) {
                        // Success
                        this.showFormMessage('Thank you for your message! I will get back to you soon.', 'success');
                        contactForm.reset();
                    } else {
                        // Error from Formspree
                        const errorData = await response.json();
                        console.error('Formspree error:', errorData);
                        this.showFormMessage('There was an error sending your message. Please try again or contact me directly.', 'error');
                    }
                    
                } catch (error) {
                    console.error('Form submission error:', error);
                    this.showFormMessage('There was an error sending your message. Please check your connection and try again.', 'error');
                } finally {
                    this.setFormLoading(false);
                }
            });

            // Real-time form validation
            const formInputs = contactForm.querySelectorAll('input, textarea');
            formInputs.forEach(input => {
                input.addEventListener('blur', () => {
                    this.validateField(input);
                });
                
                input.addEventListener('input', () => {
                    if (input.classList.contains('error')) {
                        this.validateField(input);
                    }
                });
            });

        } catch (error) {
            console.error('Contact form setup error:', error);
        }
    }

    validateForm(formData) {
        const requiredFields = ['name', 'email', 'subject', 'message'];
        
        for (const field of requiredFields) {
            const value = formData.get(field);
            if (!value || value.trim() === '') {
                return false;
            }
        }
        
        // Email validation
        const email = formData.get('email');
        const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
        if (!emailRegex.test(email)) {
            return false;
        }
        
        return true;
    }

    validateField(field) {
        const value = field.value.trim();
        const fieldType = field.type;
        
        // Remove existing error state
        field.classList.remove('error');
        
        // Check if required field is empty
        if (field.required && value === '') {
            field.classList.add('error');
            return false;
        }
        
        // Email validation
        if (fieldType === 'email' && value !== '') {
            const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
            if (!emailRegex.test(value)) {
                field.classList.add('error');
                return false;
            }
        }
        
        return true;
    }

    setFormLoading(isLoading) {
        try {
            const submitBtn = document.getElementById('submitBtn');
            const btnText = submitBtn.querySelector('.btn-text');
            const btnLoading = submitBtn.querySelector('.btn-loading');
            
            if (isLoading) {
                submitBtn.disabled = true;
                submitBtn.classList.add('loading');
                btnText.style.display = 'none';
                btnLoading.style.display = 'inline';
            } else {
                submitBtn.disabled = false;
                submitBtn.classList.remove('loading');
                btnText.style.display = 'inline';
                btnLoading.style.display = 'none';
            }
        } catch (error) {
            console.error('Set form loading error:', error);
        }
    }

    showFormMessage(message, type) {
        try {
            const formMessage = document.getElementById('formMessage');
            if (!formMessage) return;
            
            formMessage.textContent = message;
            formMessage.className = `form-message ${type}`;
            formMessage.style.display = 'block';
            
            // Auto-hide success messages after 5 seconds
            if (type === 'success') {
                setTimeout(() => {
                    this.hideFormMessage();
                }, 5000);
            }
        } catch (error) {
            console.error('Show form message error:', error);
        }
    }

    hideFormMessage() {
        try {
            const formMessage = document.getElementById('formMessage');
            if (formMessage) {
                formMessage.style.display = 'none';
            }
        } catch (error) {
            console.error('Hide form message error:', error);
        }
    }

    // Mobile Menu
    setupMobileMenu() {
        try {
            const navToggle = document.getElementById('navToggle');
            const navMenu = document.getElementById('navMenu');
            
            if (!navToggle || !navMenu) return;
            
            navToggle.addEventListener('click', () => {
                navMenu.classList.toggle('active');
                navToggle.classList.toggle('active');
            });
            
            // Close menu when clicking outside
            document.addEventListener('click', (e) => {
                if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
                    navMenu.classList.remove('active');
                    navToggle.classList.remove('active');
                }
            });
        } catch (error) {
            console.error('Mobile menu setup error:', error);
        }
    }

    // Initial Animations
    startInitialAnimations() {
        try {
            // Add initial animation classes
            setTimeout(() => {
                const heroContent = document.querySelector('.hero-content');
                if (heroContent) {
                    heroContent.classList.add('animate-in');
                }
            }, 300);
        } catch (error) {
            console.error('Initial animations error:', error);
        }
    }

    // Utility Functions
    throttle(func, limit) {
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
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    try {
        new AerospacePortfolio();
        console.log('🚀 Aerospace Portfolio initialized successfully');
    } catch (error) {
        console.error('Failed to initialize aerospace portfolio:', error);
    }
});

// Add error handling for uncaught errors
window.addEventListener('error', (e) => {
    console.error('Uncaught error:', e.error);
});

window.addEventListener('unhandledrejection', (e) => {
    console.error('Unhandled promise rejection:', e.reason);
});"""

# Save updated JavaScript file
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ Updated app.js with enhanced Formspree form handling!")
