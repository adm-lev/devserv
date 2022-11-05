import React from "react";

const MenuBlock = (({menu}) => {
    return (
        <div class="menu container">
            <ul>
            {menu.map((tile_) => <li class="menu-item">{tile_}</li>)}
            </ul>
        </div>
    )
});

export default MenuBlock;