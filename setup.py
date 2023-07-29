import setuptools

if __name__ == "__main__":
    setuptools.setup(package_data={'urdf_files': ['urdf/*.urdf'], 'meshes': ['meshes/*.STL']},include_package_data=True)