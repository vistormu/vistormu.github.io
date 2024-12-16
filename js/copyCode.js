document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.querySelectorAll('.copy-btn');

    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            let code = this.previousElementSibling.innerText;
            code = code.replace(/\u00A0/g, ' ');

            copyToClipboard(code);

            this.innerText = 'copied!';
            setTimeout(() => {
                this.innerText = 'copy';
            }, 2000);
        });
    });
});

function copyToClipboard(text) {
    let textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
}
