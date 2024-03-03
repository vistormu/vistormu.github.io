window.addEventListener('scroll', function() {
    headers = document.querySelectorAll('.header');

    headers.forEach(function(header) {
        if (window.scrollY > 0) {
            header.classList.add('shrink');
        } else {
            header.classList.remove('shrink');
        }
    });

    var navs = document.querySelectorAll('.nav-link');
    navs.forEach(function(nav) {
        if (window.scrollY > 0) {
            nav.style.display = 'none';
        } else {
            nav.style.display = 'inline-block';
        }
    });
});

