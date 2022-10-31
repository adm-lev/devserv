import React from "react";

const FooterBlock = (({footer}) => {
    return (
        <div class="footer container">
            {footer.map((string_) => <p>{string_}</p>)}
        </div>
    )
});

export default FooterBlock;