// script.js
window.addEventListener('scroll', function() {
    var headers = document.querySelectorAll('.header');
    headers.forEach(function(header) {
        if (window.pageYOffset > 0) {
            header.classList.add('shrink');
        } else {
            header.classList.remove('shrink');
        }
    });

    var navs = document.querySelectorAll('.nav-link');
    navs.forEach(function(nav) {
        if (window.pageYOffset > 0) {
            nav.style.display = 'none';
        } else {
            nav.style.display = 'inline-block';
        }
    });
});

