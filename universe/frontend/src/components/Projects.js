import React from "react";
import { Link } from "react-router-dom";


const ProjectItem = ({project}) => {
    return (
        <ul className="project-item">
            <li>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </li>                        
        </ul>
    )
};

const ProjectList = ({projects}) => {
    const clear_projects = []
    for (const i in projects.results){
        clear_projects.push(projects.results[i])
    }
    return (
        <div className="project-div">
            <ul className="project-list">
                <li>Project name</li>
                {/* <li>User name</li>
                <li>Project URL</li>                                */}
            </ul>
            {clear_projects.map((project_) => <ProjectItem project={project_}/>)}
        </div>    
    )
    
};

export default ProjectList;