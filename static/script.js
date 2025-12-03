// static/script.js
document.getElementById("converter-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const valor = parseFloat(document.getElementById("valor").value);
  const moeda_origem = document.getElementById("moeda_origem").value;
  const moeda_destino = document.getElementById("moeda_destino").value;
  const resultadoDiv = document.getElementById("resultado");

  if (!valor || valor <= 0) {
    resultadoDiv.textContent = "Informe um valor maior que zero.";
    return;
  }

  resultadoDiv.textContent = "Convertendo...";

  try {
    const res = await fetch("/converter", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ valor, moeda_origem, moeda_destino })
    });

    const data = await res.json();

    if (!res.ok) {
      resultadoDiv.textContent = data.error || "Erro desconhecido.";
      return;
    }

    // Mostra resultado e taxa (se disponível)
    const rateText = data.rate ? ` (Taxa: ${Number(data.rate).toFixed(6)})` : "";
    resultadoDiv.textContent = data.resultado + rateText;
  } catch (err) {
    console.error(err);
    resultadoDiv.textContent = "Erro na conexão. Tente novamente.";
  }
});
