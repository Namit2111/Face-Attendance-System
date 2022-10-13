import React, { useState } from "react";
import DataBase from "./DataBase";
import Card from "./Card";
import Left_items from "./Left_container_item";
import LeftPaneIcons from "./LeftPaneIcons";
import LeftPaneLogo from "./LeftPaneLogo";
import './Home.css'

const Home = () => {
    const [active, setActive] = useState(0);

  const handleClick = (e) => {
    setActive(e);
  };

  let arr = [];

  if (DataBase.length) {
    arr = DataBase.map((e) => {
      if (e.Name == "Unknown") return;
      return <Card Name={e.Name} RollNO={e.RollNO}></Card>;
    });
  }

  let i = 0;
  const left_items = Left_items.map((e) => {
    return (
      <LeftPaneIcons
        PlaceHolder={e}
        id={i++}
        active={active}
        handleClick={handleClick}
      ></LeftPaneIcons>
    );
  });

  let j = 0;
  const logo_design = LeftPaneLogo.map((e) => {
    return (
      <div
        className={`container_logo${active == j ? " active" : ""}`}
        onClick={(event) => {
          handleClick(event.target.id);
        }}
      >
        <i className={e} id={j++}></i>
      </div>
    );
  });


  return (
    <div className="container">
      <div className="left">
        <div className="upper">
          <div className="upper-left">
            <i class="fa fa-graduation-cap" aria-hidden="true"></i>
          </div>
          <div className="upper-right">
            <p>ATTENDANCE</p>
          </div>
        </div>
        <div className="lower">
          <div className="logo">{logo_design}</div>
          <div className="menu">
            <ul>{left_items}</ul>
          </div>
        </div>
      </div>
      <div className="right">
        <div className="right_items">{DataBase.length ? arr : "MASS BUNK"}</div>
      </div>
    </div>
  );
};

export default Home;
