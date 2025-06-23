import React from "react";

interface JsonPanelProps {
  onChange: (text: string) => void;
}

const JsonPanel: React.FC<JsonPanelProps> = ({ onChange }) => {
  return (
    <div className="json-panel">
      <h4 style={{ color: "deeppink" }}>JSON</h4>
      <textarea
        onChange={(e) => onChange(e.target.value)}
        placeholder="Escribe algo aquí..."
        style={{
          width: "100%",
          height: "400px",
          padding: "10px",
          fontFamily: "monospace",
        }}
      ></textarea>
    </div>
  );
};

export default JsonPanel;
