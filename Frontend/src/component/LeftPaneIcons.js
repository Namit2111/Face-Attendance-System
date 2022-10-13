// For desiging the left pane icons

import React from "react";
import "./LeftPaneIcons.css";

function Design({ PlaceHolder, id, active, handleClick }) {
  const name = PlaceHolder.toLowerCase();
  return (
    <div
      className={`list_design${active == id ? " active" : ""}`}
      id={id}
      onClick={() => {
        handleClick(id);
      }}
    >
      <li>{PlaceHolder}</li>
    </div>
  );
}

export default Design;
