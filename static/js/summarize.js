document.querySelector(".btn").addEventListener("click", function () {

    let inputText = document.getElementById("inputText").value;
    let model = document.getElementById("modelSelect").value;

    if (inputText.trim() === "") {
        alert("Please enter some text!");
        return;
    }

    const body = "text=" + encodeURIComponent(inputText) + "&model=" + encodeURIComponent(model);

    fetch("/summarize-text", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: body
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("outputSummary").value = data;
    });
});