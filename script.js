async function loadPrompts() {
  let res = await fetch("http://127.0.0.1:8000/prompts");
  let data = await res.json();
  document.getElementById("output").innerText = JSON.stringify(data, null, 2);
}

async function loadGita() {
  let res = await fetch("http://127.0.0.1:8000/gita");
  let data = await res.json();
  document.getElementById("output").innerText = JSON.stringify(data, null, 2);
}
