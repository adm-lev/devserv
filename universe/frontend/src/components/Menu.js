import React from "react";

const MenuBlock = (({menu}) => {
    return (
        <div class="menu container">
            <ul>
            {menu.map((tile_) => <li class="menu-item"><a href="#">{tile_}</a></li>)}
            </ul>
        </div>
    )
});

export default MenuBlock;