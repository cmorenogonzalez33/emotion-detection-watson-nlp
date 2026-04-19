let RunSentimentAnalysis = ()=>{
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    // Esta línea llama a la ruta que definimos en server.py
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + textToAnalyze, true);
    xhttp.send();
}
