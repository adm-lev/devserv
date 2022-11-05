import React from "react";
import { useParams } from "react-router-dom";


const ProjectItem = ({project}) => {
    return (
        <ul className="project-item">
            <li>{project.name}</li>
            <li>{project.users}</li>
            <li>{project.projectUrl}</li>  
            {/* <li><button>Delete</button></li>   */}
        </ul>
    )
};

const ProjectUser = ({projects}) => {
    const clear_projects = []
    const {userId} = useParams()    
    for (const i in projects.results){
        clear_projects.push(projects.results[i])
    }
    const filter_projects = clear_projects.filter((project) => project.users.includes(parseInt(userId)))
    return (
        <div className="project-div">
            <ul className="project-list">
                <li>Project name</li>
                <li>User name</li>
                <li>Project URL</li>                               
            </ul>
            {filter_projects.map((project_) => <ProjectItem project={project_}/>)}
        </div>    
    )
    
};

export default ProjectUser;