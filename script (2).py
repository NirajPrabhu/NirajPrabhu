# Enhanced CSS with form validation styling and improved visual feedback
css_content = """/* Professional Aerospace Portfolio Styles - Enhanced with Form Validation */

/* Root Variables */
:root {
    /* Primary Colors */
    --primary-navy: #1a237e;
    --primary-blue: #3f51b5;
    --secondary-gray: #37474f;
    --light-gray: #546e7a;
    --background-white: #fafafa;
    --pure-white: #ffffff;
    --text-dark: #212121;
    --text-light: #757575;
    
    /* Accent Colors */
    --accent-blue: #2196f3;
    --success-green: #4caf50;
    --warning-orange: #ff9800;
    --error-red: #f44336;
    
    /* Shadows */
    --shadow-light: 0 2px 4px rgba(0,0,0,0.1);
    --shadow-medium: 0 4px 8px rgba(0,0,0,0.15);
    --shadow-heavy: 0 8px 24px rgba(0,0,0,0.2);
    
    /* Transitions */
    --transition-fast: 0.2s ease;
    --transition-medium: 0.3s ease;
    --transition-slow: 0.5s ease;
}

/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: var(--text-dark);
    background-color: var(--background-white);
    scroll-behavior: smooth;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navigation */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    box-shadow: var(--shadow-light);
    z-index: 1000;
    transition: transform var(--transition-medium);
}

.navbar.hidden {
    transform: translateY(-100%);
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 20px;
}

.nav-brand {
    display: flex;
    flex-direction: column;
}

.brand-text {
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--primary-navy);
}

.brand-title {
    font-size: 0.9rem;
    color: var(--text-light);
    font-weight: 400;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-link {
    text-decoration: none;
    color: var(--text-dark);
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    transition: var(--transition-fast);
    position: relative;
}

.nav-link:hover,
.nav-link.active {
    color: var(--primary-blue);
    background-color: rgba(63, 81, 181, 0.1);
}

.nav-toggle {
    display: none;
    flex-direction: column;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
}

.nav-toggle span {
    width: 25px;
    height: 3px;
    background: var(--text-dark);
    margin: 3px 0;
    transition: var(--transition-fast);
}

/* Scroll Progress */
.scroll-progress {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: var(--primary-blue);
    z-index: 1001;
    transition: width var(--transition-fast);
}

/* Hero Section */
.hero-section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    background: linear-gradient(135deg, var(--background-white) 0%, #e8eaf6 100%);
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="%23e0e7ff" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
    opacity: 0.5;
}

.hero-content {
    position: relative;
    z-index: 2;
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.8s ease;
}

.hero-content.animate-in {
    opacity: 1;
    transform: translateY(0);
}

.hero-title {
    font-size: clamp(3rem, 8vw, 5rem);
    font-weight: 700;
    color: var(--primary-navy);
    margin-bottom: 1rem;
    letter-spacing: -0.02em;
}

.hero-subtitle {
    font-size: clamp(1.5rem, 4vw, 2.5rem);
    margin-bottom: 1.5rem;
    color: var(--primary-blue);
}

.typing-text {
    display: inline-block;
    min-width: 200px;
}

.cursor {
    font-weight: 100;
    animation: blink 1s infinite;
}

@keyframes blink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
}

.hero-description {
    font-size: 1.2rem;
    color: var(--text-light);
    margin-bottom: 2.5rem;
    max-width: 600px;
}

.hero-buttons {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.btn {
    padding: 1rem 2rem;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 600;
    transition: var(--transition-medium);
    border: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1rem;
}

.btn-primary {
    background: var(--primary-blue);
    color: white;
}

.btn-primary:hover {
    background: var(--primary-navy);
    transform: translateY(-2px);
    box-shadow: var(--shadow-medium);
}

.btn-secondary {
    background: transparent;
    color: var(--primary-blue);
    border: 2px solid var(--primary-blue);
}

.btn-secondary:hover {
    background: var(--primary-blue);
    color: white;
    transform: translateY(-2px);
}

/* Section Styles */
section {
    padding: 5rem 0;
}

.section-header {
    text-align: center;
    margin-bottom: 4rem;
}

.section-title {
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    font-weight: 700;
    color: var(--primary-navy);
    margin-bottom: 1rem;
}

.section-line {
    width: 80px;
    height: 4px;
    background: var(--primary-blue);
    margin: 0 auto;
    border-radius: 2px;
}

/* About Section */
.about-section {
    background: white;
}

.about-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.about-summary {
    font-size: 1.3rem;
    color: var(--primary-blue);
    margin-bottom: 2rem;
    font-weight: 500;
}

.about-content p {
    font-size: 1.1rem;
    line-height: 1.8;
    margin-bottom: 2rem;
    color: var(--text-light);
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}

.stat-item {
    padding: 2rem 1rem;
    background: var(--background-white);
    border-radius: 12px;
    box-shadow: var(--shadow-light);
    transition: var(--transition-medium);
}

.stat-item:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-medium);
}

.stat-number {
    font-size: 3rem;
    font-weight: 700;
    color: var(--primary-blue);
    margin-bottom: 0.5rem;
    display: block;
}

.stat-label {
    font-size: 1rem;
    color: var(--text-light);
    font-weight: 500;
}

/* Experience Section */
.experience-section {
    background: var(--background-white);
}

.timeline {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--primary-blue);
    transform: translateX(-50%);
}

.timeline-item {
    position: relative;
    margin: 3rem 0;
    display: flex;
    align-items: center;
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.6s ease;
}

.timeline-item.animate-in {
    opacity: 1;
    transform: translateY(0);
}

.timeline-item:nth-child(even) {
    flex-direction: row-reverse;
}

.timeline-marker {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 60px;
    background: white;
    border: 3px solid var(--primary-blue);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    z-index: 2;
    box-shadow: var(--shadow-light);
}

.timeline-content {
    width: 45%;
    padding: 2rem;
    background: white;
    border-radius: 12px;
    box-shadow: var(--shadow-light);
    transition: var(--transition-medium);
}

.timeline-content:hover {
    box-shadow: var(--shadow-medium);
    transform: translateY(-3px);
}

.timeline-date {
    font-size: 0.9rem;
    color: var(--primary-blue);
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.timeline-content h3 {
    font-size: 1.4rem;
    color: var(--primary-navy);
    margin-bottom: 0.5rem;
}

.timeline-content h4 {
    font-size: 1.1rem;
    color: var(--text-light);
    margin-bottom: 1rem;
}

.timeline-content p {
    line-height: 1.7;
    color: var(--text-dark);
}

.skills-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1rem;
}

.skill-tag {
    background: var(--primary-blue);
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 500;
}

/* Skills Section */
.skills-section {
    background: white;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 4rem;
}

.skills-category h3 {
    font-size: 1.8rem;
    color: var(--primary-navy);
    margin-bottom: 2rem;
    text-align: center;
}

.skill-item {
    margin-bottom: 2.5rem;
    opacity: 0;
    transform: translateX(-30px);
    transition: all 0.6s ease;
}

.skill-item.animate-in {
    opacity: 1;
    transform: translateX(0);
}

.skill-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.8rem;
}

.skill-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-dark);
}

.skill-percentage {
    font-size: 1rem;
    font-weight: 600;
    color: var(--primary-blue);
}

.skill-bar {
    height: 8px;
    background: #e0e7ff;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 0.8rem;
}

.skill-progress {
    height: 100%;
    background: linear-gradient(90deg, var(--primary-blue), var(--accent-blue));
    border-radius: 4px;
    width: 0%;
    transition: width 2s ease;
}

.skill-description {
    font-size: 0.9rem;
    color: var(--text-light);
    font-style: italic;
}

/* Projects Section */
.projects-section {
    background: var(--background-white);
}

.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2.5rem;
}

.project-card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: var(--shadow-light);
    transition: var(--transition-medium);
    opacity: 0;
    transform: translateY(30px);
    border: 1px solid #e8eaf6;
}

.project-card.animate-in {
    opacity: 1;
    transform: translateY(0);
}

.project-card:hover {
    box-shadow: var(--shadow-heavy);
    border-color: var(--primary-blue);
}

.project-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.project-icon {
    font-size: 2.5rem;
}

.project-status {
    background: var(--success-green);
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
}

.project-content h3 {
    font-size: 1.4rem;
    color: var(--primary-navy);
    margin-bottom: 0.5rem;
}

.project-period {
    color: var(--primary-blue);
    font-weight: 600;
    margin-bottom: 1rem;
}

.project-description {
    line-height: 1.7;
    color: var(--text-dark);
    margin-bottom: 1.5rem;
}

.project-highlights {
    list-style: none;
    margin-bottom: 1.5rem;
}

.project-highlights li {
    padding: 0.3rem 0;
    color: var(--text-light);
    position: relative;
    padding-left: 1.2rem;
}

.project-highlights li::before {
    content: '✓';
    position: absolute;
    left: 0;
    color: var(--success-green);
    font-weight: bold;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.tech-tag {
    background: #e8eaf6;
    color: var(--primary-navy);
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 500;
}

/* Contact Section */
.contact-section {
    background: white;
}

.contact-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    max-width: 1000px;
    margin: 0 auto;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    padding: 1.5rem;
    background: var(--background-white);
    border-radius: 12px;
    margin-bottom: 1.5rem;
    box-shadow: var(--shadow-light);
    transition: var(--transition-medium);
}

.contact-item:hover {
    transform: translateX(5px);
    box-shadow: var(--shadow-medium);
}

.contact-icon {
    font-size: 1.8rem;
    min-width: 50px;
    text-align: center;
}

.contact-details h4 {
    color: var(--primary-navy);
    margin-bottom: 0.3rem;
    font-size: 1.1rem;
}

.contact-details p {
    color: var(--text-light);
}

.contact-form-container {
    background: var(--background-white);
    padding: 2.5rem;
    border-radius: 16px;
    box-shadow: var(--shadow-light);
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group label {
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: var(--text-dark);
}

.form-group input,
.form-group textarea {
    padding: 1rem;
    border: 2px solid #e0e7ff;
    border-radius: 8px;
    font-size: 1rem;
    font-family: inherit;
    transition: var(--transition-fast);
    background: white;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-blue);
    box-shadow: 0 0 0 3px rgba(63, 81, 181, 0.1);
}

/* Form Validation Styles */
.form-group input.error,
.form-group textarea.error {
    border-color: var(--error-red);
    box-shadow: 0 0 0 3px rgba(244, 67, 54, 0.1);
}

.form-group input.success,
.form-group textarea.success {
    border-color: var(--success-green);
    box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
}

.submit-btn {
    padding: 1rem 2rem;
    background: var(--primary-blue);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition-medium);
    position: relative;
    overflow: hidden;
}

.submit-btn:hover:not(:disabled) {
    background: var(--primary-navy);
    transform: translateY(-2px);
    box-shadow: var(--shadow-medium);
}

.submit-btn:disabled {
    background: var(--light-gray);
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

.submit-btn.loading {
    background: var(--light-gray);
}

.btn-loading {
    display: none;
}

/* Form Message Styles */
.form-message {
    padding: 1rem;
    border-radius: 8px;
    font-weight: 500;
    margin-top: 1rem;
}

.form-message.success {
    background: rgba(76, 175, 80, 0.1);
    color: var(--success-green);
    border: 1px solid rgba(76, 175, 80, 0.3);
}

.form-message.error {
    background: rgba(244, 67, 54, 0.1);
    color: var(--error-red);
    border: 1px solid rgba(244, 67, 54, 0.3);
}

/* Footer */
.footer {
    background: var(--primary-navy);
    color: white;
    padding: 2rem 0;
}

.footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.footer-text p {
    margin-bottom: 0.3rem;
}

.footer-links {
    display: flex;
    gap: 2rem;
}

.footer-link {
    color: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    transition: var(--transition-fast);
}

.footer-link:hover {
    color: white;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-in {
    animation: fadeInUp 0.6s ease forwards;
}

/* Responsive Design */
@media (max-width: 768px) {
    .navbar .container {
        padding: 1rem 20px;
    }
    
    .nav-menu {
        position: fixed;
        top: 100%;
        left: 0;
        right: 0;
        background: white;
        flex-direction: column;
        padding: 2rem;
        box-shadow: var(--shadow-medium);
        transform: translateY(-100%);
        opacity: 0;
        transition: all var(--transition-medium);
        pointer-events: none;
    }
    
    .nav-menu.active {
        transform: translateY(0);
        opacity: 1;
        pointer-events: all;
    }
    
    .nav-toggle {
        display: flex;
    }
    
    .nav-toggle.active span:nth-child(1) {
        transform: rotate(45deg) translate(5px, 5px);
    }
    
    .nav-toggle.active span:nth-child(2) {
        opacity: 0;
    }
    
    .nav-toggle.active span:nth-child(3) {
        transform: rotate(-45deg) translate(7px, -6px);
    }
    
    .hero-buttons {
        flex-direction: column;
        align-items: center;
    }
    
    .btn {
        width: 100%;
        max-width: 300px;
        justify-content: center;
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    .timeline::before {
        left: 30px;
    }
    
    .timeline-item {
        flex-direction: row !important;
        padding-left: 80px;
    }
    
    .timeline-marker {
        left: 30px;
        transform: translateX(-50%);
    }
    
    .timeline-content {
        width: 100%;
    }
    
    .skills-grid {
        grid-template-columns: 1fr;
    }
    
    .contact-content {
        grid-template-columns: 1fr;
    }
    
    .footer-content {
        flex-direction: column;
        text-align: center;
    }
    
    .footer-links {
        justify-content: center;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 15px;
    }
    
    .projects-grid {
        grid-template-columns: 1fr;
    }
    
    .project-card {
        padding: 1.5rem;
    }
    
    .contact-form-container {
        padding: 1.5rem;
    }
}

/* Performance Optimizations */
* {
    will-change: auto;
}

.timeline-item,
.project-card,
.skill-item {
    will-change: transform, opacity;
}

/* Print Styles */
@media print {
    .navbar,
    .scroll-progress,
    .contact-form-container {
        display: none;
    }
    
    body {
        background: white;
        color: black;
    }
    
    .hero-section {
        background: white;
        min-height: auto;
        padding: 2rem 0;
    }
    
    section {
        padding: 2rem 0;
        break-inside: avoid;
    }
}"""

# Save updated CSS file
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ Updated style.css with enhanced form validation styling!")
print("\n🎯 All files updated with Formspree integration:")
print("   • index.html - Updated contact form with Formspree endpoint")
print("   • app.js - Enhanced form handling with validation and error messages")
print("   • style.css - Added form validation styles and visual feedback")
print("\n📧 Your contact form is now connected to: https://formspree.io/f/xzzjzwda")
print("✨ Features added:")
print("   • Real-time form validation")
print("   • Professional success/error messages")
print("   • Loading states during submission")
print("   • Spam protection with honeypot field")
print("   • Responsive form design")
print("   • Error handling for network issues")
print("\n📝 Messages sent through your portfolio will now go directly to your email!")