import React from "react";


const UserItem = ({user}) => {
    return (
        <ul class="user-item">
            <li>{user.first_name}</li>
            <li>{user.last_name}</li>
            <li>{user.user_name}</li>
            <li>{user.email}</li>
        </ul>
    )
};

const UserList = ({users}) => {
    return (
        <div class="user-div">
            <ul class="user-list">
                <li>First name</li>
                <li>Last name</li>
                <li>Username</li>
                <li>Email</li>               
            </ul>
            {users.map((user_) => <UserItem user={user_}/>)}
        </div>    
    )
    
};

export default UserList;