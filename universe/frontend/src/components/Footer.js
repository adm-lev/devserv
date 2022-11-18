import React from "react";

const FooterBlock = (({footer}) => {
    return (
        <div className="footer container">
            {footer.map((string_) => <p>{string_}</p>)}
        </div>
    )
});

export default FooterBlock;