// static/js/script.js

function sharePromise() {
    const promessa = document.getElementById('promise-text').textContent;
    if (navigator.share) {
        navigator.share({
            title: 'Promessa',
            text: promessa,
            url: window.location.href
        }).catch(error => {
            console.error('Erro ao compartilhar:', error);
        });
    } else {
        alert('A funcionalidade de compartilhamento não está disponível neste navegador.');
    }
}

function copyPromise() {
    const promessa = document.getElementById('promise-text').textContent;
    navigator.clipboard.writeText(promessa).then(() => {
        alert('Promessa copiada para a área de transferência!');
    }).catch(error => {
        console.error('Erro ao copiar para a área de transferência:', error);
    });
}
