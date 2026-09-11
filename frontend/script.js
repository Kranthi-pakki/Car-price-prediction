const form = document.getElementById("predictionForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const data = {
        Car_Name: document.getElementById("carName").value,
        Year: Number(document.getElementById("year").value),
        Present_Price: Number(document.getElementById("presentPrice").value),
        Kms_Driven: Number(document.getElementById("kmsDriven").value),
        Fuel_Type: document.getElementById("fuelType").value,
        Seller_Type: document.getElementById("sellerType").value,
        Transmission: document.getElementById("transmission").value,
        Owner: document.getElementById("owner").value
    };

    result.textContent = "Predicting...";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const prediction = await response.json();

        if (!response.ok) {
            throw new Error(prediction.error || "Prediction failed");
        }

        result.textContent =
            `Predicted Price: ₹${prediction.predicted_price} Lakhs`;

    } catch (error) {
        result.textContent =
            "Unable to connect to the prediction server.";
        console.error(error);
    }
});