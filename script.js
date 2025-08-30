document.getElementById('searchButton').addEventListener('click', function() {
    const input = document.getElementById('searchInput').value;
    const content = document.getElementById('content');
    const text = content.innerHTML;

    // Eliminar resaltes anteriores
    content.innerHTML = text.replace(/<mark>(.*?)<\/mark>/g, '$1');

    if (input) {
        const regex = new RegExp(`(${input})`, 'gi');
        const highlighted = text.replace(regex, '<mark>$1</mark>');
        content.innerHTML = highlighted;
    }
});
