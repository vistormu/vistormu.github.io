document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.querySelectorAll('.copy-btn');

    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Use DOM traversal to get the preceding <pre> element
            let code = this.previousElementSibling.innerText;

            // Copy code to clipboard
            copyToClipboard(code);

            // Change button text and revert after 2 seconds
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

