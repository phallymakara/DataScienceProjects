// This script runs before the page is rendered
(function() {
    // Function to set theme
    function setTheme(theme) {
        document.documentElement.setAttribute('data-bs-theme', theme);
        // Also apply compatible Bootstrap classes for better support
        if (theme === 'dark') {
            document.body.classList.add('bg-dark');
            document.body.classList.add('text-light');
            document.body.classList.remove('bg-light');
            document.body.classList.remove('text-dark');
        } else {
            document.body.classList.add('bg-light');
            document.body.classList.add('text-dark');
            document.body.classList.remove('bg-dark');
            document.body.classList.remove('text-light');
        }
    }

    // Load the saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        setTheme(savedTheme);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
        // If no saved preference, use device preference
        setTheme('light');
    } else {
        // Default to dark mode if no preference detected
        setTheme('dark');
    }

    // Make the function available globally
    window.setTheme = setTheme;
})(); 