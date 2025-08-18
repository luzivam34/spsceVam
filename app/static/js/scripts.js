const thumbnails = document.querySelectorAll('.display_poke img');
const preview = document.getElementById('preview');

thumbnails.forEach(img => {
    img.addEventListener('mouseenter', () => {
        const full = img.getAttribute('data-full');
        preview.src = full;
    });
});