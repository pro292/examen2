import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [expresion, setExpresion] = useState("");
  const [resultado, setResultado] = useState("");
  const [concatenacion, setConcatenacion] = useState("");

  const handleCalcular = async () => {
    try {
      const res = await axios.post("http://localhost:5000/api/pila/calcular", {
        expresion,
      });
      // Guardar resultado
      setResultado(res.data.resultado);
      // Extraer solo los valores del atributo "dato"
      const pilaConcat = res.data.pila_concatenacion || [];
      // Se invierte el orden para que los signos aparezcan primero
      const datosConcatenados = pilaConcat
        .map((nodo) => nodo.dato)
        .reverse() // 👈 invierte el orden del array
        .join(" ");
      // Guardar en el estado
      setConcatenacion(datosConcatenados);
    } catch (err) {
      console.error(err);
      setResultado("Error");
      setConcatenacion("");
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: "sans-serif" }}>
      <h2>Calculadora con Pila</h2>
      <div style={{ marginBottom: 10 }}>
        <label>Expresión:&nbsp;</label>
        <input
          type="text"
          value={expresion}
          onChange={(e) => setExpresion(e.target.value)}
          placeholder="Ej: 12+3-4"
        />
      </div>
      <div style={{ marginBottom: 10 }}>
        <button onClick={handleCalcular}>Calcular</button>
      </div>
      <div style={{ marginBottom: 10 }}>
        <label>Resultado:&nbsp;</label>
        <input type="text" value={resultado} readOnly />
      </div>
      <div style={{ marginBottom: 10 }}>
        <label>Concatenación:&nbsp;</label>
        <input type="text" value={concatenacion} readOnly />
      </div>
    </div>
  );
}

export default App;
