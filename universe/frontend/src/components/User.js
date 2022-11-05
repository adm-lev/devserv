import React from "react";


const UserItem = ({user}) => {
    return (
        <ul class="user-item">
            <li>{user.firstName}</li>
            <li>{user.lastName}</li>
            <li>{user.userName}</li>
            <li>{user.email}</li>
        </ul>
    )
};

const UserList = ({users}) => {
    const clear_users = []
    for (const i in users.results){
        clear_users.push(users.results[i])
    }
    
    return (
        <div class="user-div">
            <ul class="user-list">
                <li>First name</li>
                <li>Last name</li>
                <li>Username</li>
                <li>Email</li>               
            </ul>            
            {clear_users.map((user_) => <UserItem user={user_}/>)}
            
        </div>    
    )
    
};

export default UserList;