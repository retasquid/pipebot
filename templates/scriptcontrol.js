//completez l'ip et le port si necessaire
function encoder(touche){
    let v = {touche};
    const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body:vj=JSON.stringify(v)
    };
    fetch('http://192.168.1.20:1707', options)
    .then(response => response.json())
    .then(vj => {
      console.log('Réponse du serveur:', vj);
    })
    .catch(error => {
      console.error('Erreur lors de l\'envoi de la requête:', error);
    });
}

document.addEventListener("keydown", function(event) {
    if (event.key === 'z') {
        console.log('avance!');
        encoder(event.key);
    }else if (event.key === 's') {
        console.log('recule!');
        encoder(event.key);
    }else if (event.key === 'q') {
        console.log('gauche!');
        encoder(event.key);
    }else if (event.key === 'd') {
        console.log('droite!');
        encoder(event.key);
    }else if (event.key === 'e') {
        console.log('Led allumée!');
        encoder(event.key);
    }else if (event.key === ' ') {
        console.log('changement de mode!');
        encoder("sp");
    }else if (event.key === 'p') {
        console.log('prise de données!');
        encoder(event.key);
    }
});



