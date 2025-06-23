import React, { useState } from "react";
import Navbar from "../components/navbar";
import JsonPanel from "../components/jsonpanel";
import Panel from "../components/panel";
// (otros imports si los tienes)

const Home = () => {
  const [content, setContent] = useState("");

  return (
    <div>
      <Navbar />
      <div>
        <JsonPanel onChange={(text) => setContent(text)} />
        <Panel content={content} />
      </div>
    </div>
  );
};

export default Home;
