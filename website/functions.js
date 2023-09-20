function registrar() {
    var resultadoElement = document.getElementById("mensagemSucesso");
    
    resultadoElement.textContent = "Ponto cadastrado com sucesso!";
    resultadoElement.style.display = "block";
    resultadoElement.classList.remove("fadeOut");
    resultadoElement.classList.add("fadeIn");
    
    setTimeout(function () {
        resultadoElement.classList.remove("fadeIn");
        resultadoElement.classList.add("fadeOut");
        setTimeout(function () {
            resultadoElement.style.display = "none";
        }, 1000);
    }, 3000);
}

function horaAtual() {
    var contadorElement = document.getElementById("contador");
    var agora = new Date();
    var hora = agora.getHours().toString().padStart(2, '0');
    var minutos = agora.getMinutes().toString().padStart(2, '0');
    var segundos = agora.getSeconds().toString().padStart(2, '0');

    contadorElement.textContent = hora + ":" + minutos + ":" + segundos;
}

setInterval(horaAtual, 1000);

const serverURL = 'http://127.0.0.1:5001';
document.getElementById('valorInteiro').addEventListener('submit', function (e) {
    e.preventDefault();
    const matricula = document.getElementById('valorInteiro').value;
    fetch('${serverURL}/ponto-adicao', {
        method: 'POST',
        body: JSON.stringify({ usuario: matricula })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').textContent = data.message;
    });
});