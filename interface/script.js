document.getElementById("predictionForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const sepalWidth = document.getElementById("sepalWidth").value;
    
    if (!sepalWidth) {
        alert("Veuillez entrer la largeur du sépale.");
        return;
    }
    
    try {
        const response = await fetch("http://localhost:8000/predict", { // Remplacez par l'URL de votre API
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ sepal_width: parseFloat(sepalWidth) }),
        });

        const data = await response.json();
        
        if (response.ok) {
            document.getElementById("predictionResult").innerText = `Longueur estimée : ${data.predicted_length} cm`;
        } else {
            document.getElementById("predictionResult").innerText = "Erreur de prédiction. Essayez à nouveau";
        }
    } catch (error) {
        document.getElementById("predictionResult").innerText = "Une erreur s'est produite. Veuillez réessayer plus tard.";
    }
});
