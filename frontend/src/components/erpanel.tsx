import React from "react";
import "./jsonpanel.css"; // Usa el mismo estilo base por ahora

const ErPanel = () => {
  return (
    <div className="json-panel">
      <h2 style={{ color: "white", padding: "20px" }}>Panel E/R</h2>
      <p style={{ color: "white", paddingLeft: "20px" }}>
        Aquí puedes mostrar tu diagrama Entidad-Relación o información del modelo de base de datos.
      </p>
    </div>
  );
};

export default ErPanel;
