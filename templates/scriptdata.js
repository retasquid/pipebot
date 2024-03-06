function afficherDonneesJSON() {
fetch('../donnees_capteurs.json')
.then(response => response.json())
.then(data => {
  // Afficher les données dans un élément <p>
  const dataDate1 = data['date 1'];
  if (dataDate1) {
      // Lire la valeur de la propriété "distance" dans l'objet "date 1"
      const distance = dataDate1.distance;
      if (distance !== undefined) {
          // Afficher la valeur de la distance dans un élément <p>
          document.getElementById('distance').textContent = `${distance}`;
        } else {
          console.error("La propriété 'distance' n'est pas définie dans l'objet 'date 1'.");
      }

      const temperature = dataDate1.temperature;
      if (temperature !== undefined) {
          // Afficher la valeur de la temperature dans un élément <p>
          document.getElementById('temperature').textContent = `${temperature}`;
      } else {
          console.error("La propriété 'temperature' n'est pas définie dans l'objet 'date 1'.");
      }
      
      const humidite = dataDate1.humidite;
      if (humidite !== undefined) {
          // Afficher la valeur de la humidité dans un élément <p>
          document.getElementById('humidite').textContent = `${humidite}`;
      } else {
          console.error("La propriété 'humidité' n'est pas définie dans l'objet 'date 1'.");
      }

      const taux_co2 = dataDate1.taux_co2;
      if (taux_co2 !== undefined) {
          // Afficher la valeur du taux_co2 dans un élément <p>
          document.getElementById('taux_co2').textContent = `${taux_co2}`;
      } else {
          console.error("La propriété 'taux_co2' n'est pas définie dans l'objet 'date 1'.");
      }
  } else {
  console.error("La clé 'date 1' n'existe pas dans le JSON.");
  }
})
.catch(error => {
  console.error('Erreur lors de la récupération des données:', error);
});
}
window.onload = afficherDonneesJSON;