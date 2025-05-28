document.addEventListener('DOMContentLoaded', function() {
    // Enable tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Enable popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    });

    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Course search functionality (for course listing page)
    const courseSearchInput = document.getElementById('courseSearchInput');
    if (courseSearchInput) {
        courseSearchInput.addEventListener('keyup', function() {
            const searchValue = this.value.toLowerCase();
            const courseCards = document.querySelectorAll('.course-card');
            
            courseCards.forEach(function(card) {
                const title = card.querySelector('.card-title').textContent.toLowerCase();
                const code = card.querySelector('.badge').textContent.toLowerCase();
                const description = card.querySelector('.card-text').textContent.toLowerCase();
                const instructor = card.querySelector('.instructor-name')?.textContent.toLowerCase() || '';
                
                if (title.includes(searchValue) || code.includes(searchValue) || 
                    description.includes(searchValue) || instructor.includes(searchValue)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    // Password strength meter
    const passwordInput = document.getElementById('password');
    const strengthMeter = document.getElementById('password-strength-meter');
    
    if (passwordInput && strengthMeter) {
        passwordInput.addEventListener('input', function() {
            const password = this.value;
            let strength = 0;
            
            // Check length
            if (password.length >= 8) strength += 1;
            
            // Check for lowercase and uppercase letters
            if (/[a-z]/.test(password) && /[A-Z]/.test(password)) strength += 1;
            
            // Check for numbers
            if (/\d/.test(password)) strength += 1;
            
            // Check for special characters
            if (/[^a-zA-Z0-9]/.test(password)) strength += 1;
            
            // Update strength meter
            strengthMeter.value = strength;
            
            // Update strength text
            const strengthText = document.getElementById('password-strength-text');
            if (strengthText) {
                const strengthLabels = ['Weak', 'Fair', 'Good', 'Strong'];
                strengthText.textContent = strength > 0 ? strengthLabels[strength - 1] : '';
                
                // Update color
                strengthText.className = 'text-' + 
                    (strength === 1 ? 'danger' : 
                     strength === 2 ? 'warning' : 
                     strength === 3 ? 'info' : 
                     strength === 4 ? 'success' : '');
            }
        });
    }

    // Course enrollment count progress bars
    const enrollmentBars = document.querySelectorAll('.enrollment-progress');
    enrollmentBars.forEach(function(bar) {
        const current = parseInt(bar.getAttribute('data-current'));
        const max = parseInt(bar.getAttribute('data-max'));
        const percentage = Math.round((current / max) * 100);
        
        // Update width
        bar.style.width = percentage + '%';
        
        // Update color based on capacity
        if (percentage < 50) {
            bar.classList.add('bg-success');
        } else if (percentage < 80) {
            bar.classList.add('bg-warning');
        } else {
            bar.classList.add('bg-danger');
        }
        
        // Update text
        bar.textContent = current + '/' + max;
    });

    // Toggle password visibility
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');
    togglePasswordButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const passwordField = document.getElementById(targetId);
            
            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                this.innerHTML = '<i class="fas fa-eye-slash"></i>';
            } else {
                passwordField.type = 'password';
                this.innerHTML = '<i class="fas fa-eye"></i>';
            }
        });
    });

    // Confirmation for critical actions
    const confirmActionButtons = document.querySelectorAll('.confirm-action');
    confirmActionButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            const message = this.getAttribute('data-confirm-message') || 'Are you sure you want to continue?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });
    
    // Theme toggling functionality
    const themeToggleBtn = document.getElementById('theme-toggle');
    
    if (themeToggleBtn) {
        // Update button state based on current theme
        function updateButtonState() {
            const currentTheme = document.documentElement.getAttribute('data-bs-theme') || 'dark';
            // Update toggle button appearance based on theme
            if (currentTheme === 'dark') {
                themeToggleBtn.setAttribute('title', 'Switch to light mode');
                themeToggleBtn.querySelector('.sun-icon').style.opacity = '1';
                themeToggleBtn.querySelector('.moon-icon').style.opacity = '0';
            } else {
                themeToggleBtn.setAttribute('title', 'Switch to dark mode');
                themeToggleBtn.querySelector('.sun-icon').style.opacity = '0';
                themeToggleBtn.querySelector('.moon-icon').style.opacity = '1';
            }
        }
        
        // Set initial state of toggle button
        updateButtonState();
        
        // Toggle theme when the button is clicked
        themeToggleBtn.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-bs-theme') || 'dark';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            // Use the setTheme function from theme.js if available
            if (typeof window.setTheme === 'function') {
                window.setTheme(newTheme);
            } else {
                document.documentElement.setAttribute('data-bs-theme', newTheme);
            }
            
            // Save the preference
            localStorage.setItem('theme', newTheme);
            
            // Update button state
            updateButtonState();
            
            console.log('Theme switched to:', newTheme); // Debugging
        });
    }
});
