import subprocess

async def vue_install_package(path: str, package_name: str):
    """
    This function is used to install a package in the Vue project.
    Parameters: 
        package_name : The name of the package.
        path : The path of the project.
    """
    try:
        subprocess.run(["npm", "install", package_name], cwd=path)
        return {
            "status": "true",
            "description": "Package installed successfully.",
        }
    except Exception as e:
        return {"status": "false", "description": str(e)}

async def vue_create_directory(path: str, directory_name: str):
    """
    This function is used to create a directory in the Vue project.
    Parameters: 
        path : The path of the project.
        directory_name : The name of the directory.
    """
    
    try:
        cmd = "mkdir " + directory_name
        print(cmd)
        completed_process = subprocess.run(cmd, shell=True, cwd=path)
        print(completed_process)
        description = ""
        status = "false"
        if completed_process.returncode == 0:
            description = "File created successfully."
            status = "true"
        else:
            description = "File creation failed."
        return {
            "status": status,
            "description": description,
        }
    except Exception as e:
        return {"status": "false", "description": str(e)}
    
async def vue_create_file(path: str, file_name: str):
    """
    This function is used to create a file in the Vue project.
    Parameters: 
        path : The path of the project.
        file_name : The name of the file.
    """
    try:
        cmd = "touch " + file_name
        print(cmd)
        completed_process = subprocess.run(cmd, shell=True, cwd=path)
        print(completed_process)
        description = ""
        status = "false"
        if completed_process.returncode == 0:
            description = "File created successfully."
            status = "true"
        else:
            description = "File creation failed."
        return {
            "status": status,
            "discription": description,
        }
    except Exception as e:
        return {"status": "false", "description": str(e)}
    
async def vue_get_project_file_list(path: str):
    """
    This function is used to get the file list of the Vue project.
    Parameters: 
        project_name : The name of the project.
        path : The path of the project.
    """
    # 使用ls命令获取文件列表
    try:
        cmd = "ls -a " + path
        print(cmd)
        tree = subprocess.run(cmd, shell=True, capture_output=True)
        return {
            "status": "true",
            "description": tree.stdout.decode(),
        }
    except Exception as e:
        return {"status": "false", "description": str(e)}
    
    
async def get_vue_project_file_content(path: str, file_name: str):
    """
    This function is used to get the content of a file in the Vue project.
    Parameters: 
        path : The path of the file you want to write to.
        file_name : The name of the file.
    """
    try:
        with open(f"{path}/{file_name}", "r") as f:
            content = f.read()
        return {
            "status": "true",
            "description": content,
        }
    except Exception as e:
        return {"status": "false", "description": str(e)}
      
async def write_vue_project_file_content(path: str, file_name: str, content: str):
    """
    This function is used to write content to a file in the Vue project.
    Parameters: 
        path : The path of the file you want to write to.
        file_name : The name of the file.
        content : The content to write.
    """
    try:
        with open(f"{path}/{file_name}", "w") as f:
            f.write(content)
        return {
            "status": "true",
            "description": "File content written successfully.",
        }
    except Exception as e:
        return {"status": "false", "description": str(e)}
    
