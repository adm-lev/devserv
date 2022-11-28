import {useLocation} from 'react-router-dom';
import React from 'react';

const NotFound404 = () => {
    const {pathname} = useLocation()

    return(
        <div>
            <h1>THis page is not found: {pathname}</h1>
        </div>
    )
};

export default NotFound404;