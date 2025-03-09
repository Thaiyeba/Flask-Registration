function submitForm() {
    let sname = document.getElementById("sname").value;
    let place = document.getElementById("place").value;
    let salary = document.getElementById("salary").value;

    if (sname === "" || place === "" || salary === "") {
        alert("Please fill all fields.");
        return;
    }

    let formData = { sname, place, salary };

    fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "success.html";  // Redirect to success page
        } else {
            console.log("Error:", data.message);
        }
    })
    .catch(error => {
        console.error("Connection error. The server might be down.");
    });
}
