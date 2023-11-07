document.addEventListener('DOMContentLoaded', (event) => {
    const savedTheme = localStorage.getItem('theme');
    const modeToggleElement = document.getElementById('themeIcon');
    const highlightStyle = document.getElementById('highlight-style');

    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        modeToggleElement.src = 'assets/off.svg';
        highlightStyle.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-dark.min.css';
    } else {
        document.body.classList.remove('dark-mode');
        modeToggleElement.src = 'assets/on.svg';
        highlightStyle.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-light.min.css';
    }
});
document.getElementById('modeToggle').addEventListener('click', function() {
    const modeToggleElement = document.getElementById('themeIcon');
    document.body.classList.toggle('dark-mode');
    const highlightStyle = document.getElementById('highlight-style');

    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
        modeToggleElement.src = 'assets/off.svg';
        highlightStyle.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-dark.min.css';
    } else {
        localStorage.setItem('theme', 'light');
        modeToggleElement.src = 'assets/on.svg';
        highlightStyle.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-light.min.css';
    }
});

