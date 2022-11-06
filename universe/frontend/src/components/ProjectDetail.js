import React from "react";
import { useParams } from "react-router-dom";


const ProjectDetail = ({projects}) => {
    // const clear_projects = []
    // for (const i in projects.results){
    //     clear_projects.push(projects.results[i])
    // }
    const clear_projects = projects.results
    const {projectId} = useParams(); 
    const project = clear_projects.filter((item) => parseInt(item.id) === parseInt(projectId))[0];    
    return (
        <ul className="project-item">
            <li>{project.id}</li>
            <li>{project.name}</li>
            <li>{project.users}</li>
            <li>{project.projectUrl}</li>              
        </ul>
    )
};

export default ProjectDetail;