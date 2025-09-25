// Professional Aerospace Portfolio JavaScript - Fixed Version

class AerospacePortfolio {
    constructor() {
        this.currentTypeIndex = 0;
        this.isTyping = false;
        this.typingPhrases = [
            "Aeronautical Engineer",
            "Flight Control Specialist",
            "Aerospace Systems Expert",
            "CFD Analysis Specialist",
            "Research & Development Engineer",
            "MATLAB/Simulink Expert"
        ];
        
        this.initializeApp();
    }

    initializeApp() {
        try {
            // Wait for DOM to be fully loaded
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

    // Fixed Navigation Setup
    setupNavigation() {
        try {
            this.navbar = document.getElementById('navbar');
            this.navLinks = document.querySelectorAll('.nav-link');
            this.lastScrollY = window.scrollY;
            
            if (!this.navbar || this.navLinks.length === 0) {
                console.warn('Navigation elements not found');
                return;
            }
            
            // Setup navigation click handlers with error handling
            this.navLinks.forEach(link => {
                link.addEventListener('click', (e) => {
                    try {
                        e.preventDefault();
                        const href = link.getAttribute('href');
                        
                        if (!href || !href.startsWith('#')) {
                            console.warn('Invalid navigation link:', href);
                            return;
                        }
                        
                        const targetId = href.substring(1);
                        const targetElement = document.getElementById(targetId);
                        
                        if (targetElement) {
                            this.scrollToSection(targetId);
                            this.updateActiveNavLink(targetId);
                        } else {
                            console.warn('Target section not found:', targetId);
                        }
                    } catch (error) {
                        console.error('Navigation click error:', error);
                    }
                });
            });

            // Setup scroll handlers with throttling
            const throttledScrollHandler = this.throttle(() => {
                try {
                    this.handleNavbarScroll();
                    this.updateScrollProgress();
                    this.updateActiveNavLink();
                } catch (error) {
                    console.error('Scroll handler error:', error);
                }
            }, 16);
            
            window.addEventListener('scroll', throttledScrollHandler, { passive: true });
            
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

    updateScrollProgress() {
        const scrollProgress = document.getElementById('scrollProgress');
        if (!scrollProgress) return;
        
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
        
        scrollProgress.style.width = Math.min(100, Math.max(0, scrolled)) + '%';
    }

    updateActiveNavLink(targetSection = null) {
        try {
            if (targetSection) {
                this.navLinks.forEach(link => {
                    const linkTarget = link.getAttribute('href')?.substring(1);
                    if (linkTarget) {
                        link.classList.toggle('active', linkTarget === targetSection);
                    }
                });
                return;
            }

            const sections = document.querySelectorAll('section[id]');
            let currentSection = '';

            sections.forEach(section => {
                const rect = section.getBoundingClientRect();
                if (rect.top <= 100 && rect.bottom >= 100) {
                    currentSection = section.id;
                }
            });

            this.navLinks.forEach(link => {
                const linkTarget = link.getAttribute('href')?.substring(1);
                if (linkTarget) {
                    link.classList.toggle('active', linkTarget === currentSection);
                }
            });
        } catch (error) {
            console.error('Active nav link update error:', error);
        }
    }

    scrollToSection(targetId) {
        try {
            const target = document.getElementById(targetId);
            if (!target) {
                console.warn('Target section not found:', targetId);
                return;
            }

            const navbarHeight = this.navbar ? this.navbar.offsetHeight : 80;
            const targetOffset = target.offsetTop - navbarHeight;
            
            window.scrollTo({
                top: Math.max(0, targetOffset),
                behavior: 'smooth'
            });
        } catch (error) {
            console.error('Scroll to section error:', error);
        }
    }

    // Scroll Effects
    setupScrollEffects() {
        try {
            const sections = document.querySelectorAll('section');
            sections.forEach(section => {
                section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            });
        } catch (error) {
            console.error('Scroll effects setup error:', error);
        }
    }

    // Typing Animation
    setupTypingAnimation() {
        try {
            this.typingElement = document.getElementById('typingText');
            if (this.typingElement) {
                setTimeout(() => {
                    this.startTypingAnimation();
                }, 1000);
            }
        } catch (error) {
            console.error('Typing animation setup error:', error);
        }
    }

    async startTypingAnimation() {
        if (this.isTyping || !this.typingElement) return;
        
        try {
            await this.typePhrase(this.typingPhrases[this.currentTypeIndex]);
        } catch (error) {
            console.error('Typing animation error:', error);
        }
    }

    async typePhrase(phrase) {
        this.isTyping = true;
        
        try {
            // Type out the phrase
            for (let i = 0; i <= phrase.length; i++) {
                if (this.typingElement) {
                    this.typingElement.textContent = phrase.substring(0, i);
                }
                await this.delay(100);
            }
            
            // Wait before erasing
            await this.delay(3000);
            
            // Erase the phrase
            for (let i = phrase.length; i >= 0; i--) {
                if (this.typingElement) {
                    this.typingElement.textContent = phrase.substring(0, i);
                }
                await this.delay(50);
            }
            
            // Move to next phrase
            this.currentTypeIndex = (this.currentTypeIndex + 1) % this.typingPhrases.length;
            this.isTyping = false;
            
            // Wait before next phrase
            await this.delay(500);
            this.startTypingAnimation();
        } catch (error) {
            console.error('Type phrase error:', error);
            this.isTyping = false;
        }
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // Animation Observers
    setupAnimationObservers() {
        try {
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };

            this.observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        this.animateElement(entry.target);
                    }
                });
            }, observerOptions);

            // Observe sections and animated elements
            const elementsToAnimate = document.querySelectorAll(`
                .section-header,
                .about-text,
                .education-section,
                .timeline-item,
                .skills-category,
                .project-card,
                .contact-info,
                .contact-form-container
            `);

            elementsToAnimate.forEach(element => {
                this.observer.observe(element);
            });
        } catch (error) {
            console.error('Animation observer setup error:', error);
        }
    }

    animateElement(element) {
        try {
            element.classList.add('animate');
            
            // Special handling for timeline items
            if (element.classList.contains('timeline-item')) {
                const siblings = Array.from(element.parentElement.children);
                const delay = siblings.indexOf(element) * 200;
                setTimeout(() => {
                    element.classList.add('animate');
                }, delay);
            }
        } catch (error) {
            console.error('Element animation error:', error);
        }
    }

    // Skills Animation
    setupSkillsAnimation() {
        try {
            const skillsSection = document.getElementById('skills');
            if (!skillsSection) return;
            
            let skillsAnimated = false;

            const skillsObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !skillsAnimated) {
                        this.animateSkills();
                        skillsAnimated = true;
                    }
                });
            }, { threshold: 0.3 });

            skillsObserver.observe(skillsSection);
        } catch (error) {
            console.error('Skills animation setup error:', error);
        }
    }

    animateSkills() {
        try {
            const skillItems = document.querySelectorAll('.skill-item');
            
            skillItems.forEach((item, index) => {
                setTimeout(() => {
                    const progressBar = item.querySelector('.skill-progress');
                    if (progressBar) {
                        const level = progressBar.dataset.level;
                        progressBar.style.width = level + '%';
                        
                        // Add hover effects
                        item.addEventListener('mouseenter', () => {
                            progressBar.style.filter = 'brightness(1.1)';
                        });
                        
                        item.addEventListener('mouseleave', () => {
                            progressBar.style.filter = 'brightness(1)';
                        });
                    }
                }, index * 100);
            });
        } catch (error) {
            console.error('Skills animation error:', error);
        }
    }

    // Project Cards
    setupProjectCards() {
        try {
            const projectCards = document.querySelectorAll('.project-card');
            
            projectCards.forEach(card => {
                const toggleBtn = card.querySelector('.project-toggle');
                if (toggleBtn) {
                    toggleBtn.addEventListener('click', (e) => {
                        e.preventDefault();
                        this.toggleProjectCard(card);
                    });
                }
                
                // Add hover effects
                card.addEventListener('mouseenter', () => {
                    card.style.transform = 'translateY(-6px)';
                });
                
                card.addEventListener('mouseleave', () => {
                    if (!card.classList.contains('expanded')) {
                        card.style.transform = 'translateY(0)';
                    }
                });
            });
        } catch (error) {
            console.error('Project cards setup error:', error);
        }
    }

    toggleProjectCard(card) {
        try {
            const toggleBtn = card.querySelector('.project-toggle');
            if (!toggleBtn) return;
            
            // Close other expanded cards
            document.querySelectorAll('.project-card.expanded').forEach(otherCard => {
                if (otherCard !== card) {
                    otherCard.classList.remove('expanded');
                    const otherBtn = otherCard.querySelector('.project-toggle');
                    if (otherBtn) {
                        otherBtn.textContent = 'View Details';
                        otherBtn.setAttribute('aria-expanded', 'false');
                    }
                }
            });
            
            // Toggle current card
            const isExpanded = card.classList.contains('expanded');
            card.classList.toggle('expanded');
            
            if (card.classList.contains('expanded')) {
                toggleBtn.textContent = 'Hide Details';
                toggleBtn.setAttribute('aria-expanded', 'true');
                card.style.transform = 'translateY(-6px)';
            } else {
                toggleBtn.textContent = 'View Details';
                toggleBtn.setAttribute('aria-expanded', 'false');
                card.style.transform = 'translateY(0)';
            }
        } catch (error) {
            console.error('Project card toggle error:', error);
        }
    }

    // Contact Form
    setupContactForm() {
        try {
            const contactForm = document.getElementById('contactForm');
            if (!contactForm) return;
            
            contactForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.handleFormSubmission(contactForm);
            });
            
            // Add input focus effects
            const inputs = contactForm.querySelectorAll('.form-control');
            inputs.forEach(input => {
                input.addEventListener('focus', () => {
                    if (input.parentElement) {
                        input.parentElement.style.transform = 'scale(1.02)';
                    }
                });
                
                input.addEventListener('blur', () => {
                    if (input.parentElement) {
                        input.parentElement.style.transform = 'scale(1)';
                    }
                });
            });
        } catch (error) {
            console.error('Contact form setup error:', error);
        }
    }

    async handleFormSubmission(form) {
        try {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (!submitBtn) return;
            
            const originalText = submitBtn.textContent;
            
            // Show loading state
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.7';
            
            // Simulate form submission
            await this.delay(2000);
            
            // Show success message
            this.showNotification('Message sent successfully!', 'success');
            form.reset();
            
            // Reset button
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
        } catch (error) {
            console.error('Form submission error:', error);
            this.showNotification('Failed to send message. Please try again.', 'error');
        }
    }

    showNotification(message, type = 'success') {
        try {
            const notification = document.createElement('div');
            notification.className = `notification notification--${type}`;
            notification.textContent = message;
            
            const bgColor = type === 'success' ? '#28a745' : '#dc3545';
            
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 1rem 1.5rem;
                border-radius: 8px;
                color: white;
                font-weight: 500;
                z-index: 10000;
                transform: translateX(100%);
                transition: transform 0.3s ease;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                background: ${bgColor};
            `;
            
            document.body.appendChild(notification);
            
            // Animate in
            setTimeout(() => {
                notification.style.transform = 'translateX(0)';
            }, 100);
            
            // Animate out
            setTimeout(() => {
                notification.style.transform = 'translateX(100%)';
                setTimeout(() => {
                    if (notification.parentElement) {
                        notification.parentElement.removeChild(notification);
                    }
                }, 300);
            }, 3000);
        } catch (error) {
            console.error('Notification error:', error);
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
            
            // Close menu when clicking nav links
            this.navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    navMenu.classList.remove('active');
                    navToggle.classList.remove('active');
                });
            });
        } catch (error) {
            console.error('Mobile menu setup error:', error);
        }
    }

    // Start initial animations
    startInitialAnimations() {
        try {
            setTimeout(() => {
                const sections = document.querySelectorAll('section');
                sections.forEach(section => {
                    section.style.opacity = '1';
                    section.style.transform = 'translateY(0)';
                });
            }, 500);
        } catch (error) {
            console.error('Initial animations error:', error);
        }
    }

    // Utility function for throttling
    throttle(func, delay) {
        let timeoutId;
        let lastExecTime = 0;
        
        return function (...args) {
            const currentTime = Date.now();
            
            if (currentTime - lastExecTime > delay) {
                func.apply(this, args);
                lastExecTime = currentTime;
            } else {
                clearTimeout(timeoutId);
                timeoutId = setTimeout(() => {
                    func.apply(this, args);
                    lastExecTime = Date.now();
                }, delay - (currentTime - lastExecTime));
            }
        };
    }
}

// Initialize the application
let portfolioApp;

document.addEventListener('DOMContentLoaded', function() {
    try {
        portfolioApp = new AerospacePortfolio();
        
        // Add mobile menu styles
        const style = document.createElement('style');
        style.textContent = `
            @media (max-width: 768px) {
                .nav-menu {
                    position: fixed;
                    top: 100%;
                    left: 0;
                    right: 0;
                    background: var(--color-surface);
                    border-top: 1px solid var(--color-border);
                    flex-direction: column;
                    padding: var(--space-lg);
                    gap: var(--space-md);
                    transform: translateY(-100%);
                    opacity: 0;
                    visibility: hidden;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
                }
                
                .nav-menu.active {
                    transform: translateY(0);
                    opacity: 1;
                    visibility: visible;
                }
                
                .nav-link {
                    padding: var(--space-md);
                    text-align: center;
                    border-radius: var(--radius-base);
                    transition: all 0.15s ease;
                }
                
                .nav-toggle span {
                    transition: all 0.3s ease;
                }
                
                .nav-toggle.active span:nth-child(1) {
                    transform: rotate(45deg) translateY(6px);
                }
                
                .nav-toggle.active span:nth-child(2) {
                    opacity: 0;
                }
                
                .nav-toggle.active span:nth-child(3) {
                    transform: rotate(-45deg) translateY(-6px);
                }
            }
        `;
        document.head.appendChild(style);
        
    } catch (error) {
        console.error('Application initialization failed:', error);
    }
});

// Global functions
window.scrollToSection = function(sectionId) {
    try {
        if (portfolioApp) {
            portfolioApp.scrollToSection(sectionId);
        }
    } catch (error) {
        console.error('Global scroll function error:', error);
    }
};