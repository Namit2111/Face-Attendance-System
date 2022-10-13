
// Required to display information on the card

import React from "react";
import './Card.css'

function Str({ Name, RollNO }) {
  return (
    <div className="card">
      <div className="image">
        <img src={require(`../EncodedImages/${Name}.jpeg`)}/>
        <h1>{Name}</h1>
        <p>Roll NO = {RollNO}</p>
      </div>
      <div className="circle">
        <div className="present">P</div>
        <div className="ab">A</div>
        <div className="ab">L</div>
      </div>
    </div>
  );
}

export default Str;
