document.addEventListener('DOMContentLoaded', (event) => {
    const savedTheme = localStorage.getItem('theme');
    const modeToggleElement = document.getElementById('themeIcon');

    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        modeToggleElement.src = 'assets/off.svg';
    } else {
        document.body.classList.remove('dark-mode');
        modeToggleElement.src = 'assets/on.svg';
    }
});
document.getElementById('modeToggle').addEventListener('click', function() {
    const modeToggleElement = document.getElementById('themeIcon');
    document.body.classList.toggle('dark-mode');

    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
        modeToggleElement.src = 'assets/off.svg';
    } else {
        localStorage.setItem('theme', 'light');
        modeToggleElement.src = 'assets/on.svg';
    }
});

