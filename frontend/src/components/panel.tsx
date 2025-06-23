import React, { useEffect, useState } from "react";

interface PanelProps {
  content: string;
}

const Panel: React.FC<PanelProps> = ({ content }) => {
  const [imageUrl, setImageUrl] = useState("");

  useEffect(() => {
    if (!content.trim()) return;

    const fetchImage = async () => {
      try {
        const res = await fetch("http://localhost:8000/generate-image", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text: content }),
        });

        const data = await res.json();
        setImageUrl(data.image_url);
      } catch (err) {
        console.error("Error al obtener la imagen:", err);
      }
    };

    fetchImage();
  }, [content]);

  return (
    <div className="panel">
      <h4>Contenido recibido:</h4>
      <pre>{content}</pre>

      {imageUrl && (
        <img
          src={imageUrl}
          alt="Generado por backend"
          style={{ maxWidth: "100%", marginTop: "10px" }}
        />
      )}
    </div>
  );
};

export default Panel;
