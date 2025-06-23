import React from "react";
import "./jsonpanel.css"; // Puedes usar el mismo estilo del panel JSON

const AwsPanel = () => {
  return (
    <div className="json-panel">
      <h2 style={{ color: "white", padding: "20px" }}>Panel de AWS</h2>
      <p style={{ color: "white", paddingLeft: "20px" }}>
        Aquí puedes mostrar información relacionada con tu arquitectura en la nube, servicios de AWS o visualizaciones de infraestructura.
      </p>
    </div>
  );
};

export default AwsPanel;
