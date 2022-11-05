import React from "react";

const MenuBlock = (({menu}) => {
    return (
        <div className="menu container">
            <ul>
            {menu.map((tile_) => <li className="menu-item">{tile_}</li>)}
            </ul>
        </div>
    )
});

export default MenuBlock;