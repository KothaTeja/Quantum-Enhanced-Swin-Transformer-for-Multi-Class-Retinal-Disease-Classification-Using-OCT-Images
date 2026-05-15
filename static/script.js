function uploadImage() {
    const input = document.getElementById('imageInput');
    const file = input.files[0];

    if (!file) {
        alert("Select an image");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const reader = new FileReader();

    reader.onload = function(e) {
        const imageURL = e.target.result;

        // Send to backend
        fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {

            if (data.error) {
                document.getElementById("result").innerHTML =
                    `<p style="color:red;">${data.error}</p>`;
            } else {
                document.getElementById("result").innerHTML =
                    `
                    <div style="text-align:center;">
                        <img src="${imageURL}" width="300" style="border-radius:10px; margin-bottom:15px;">

                        <h2>Prediction: ${data.class}</h2>
                        <h3>Confidence: ${data.confidence}%</h3>
                    </div>
                    `;
            }
        })
        .catch(err => {
            console.error(err);
            alert("Backend connection error");
        });
    };

    reader.readAsDataURL(file);
}