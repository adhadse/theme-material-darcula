"""
theme-material-darcula setup
"""
import json
from pathlib import Path
# import conda_build.bdist_conda


from jupyter_packaging import (
    create_cmdclass, 
    install_npm, 
    ensure_targets,
    combine_commands,
    skip_if_exists
)
import setuptools

HERE = Path(__file__).parent.resolve()

# The name of the project
name = "theme-material-darcula"

# Get our version
with (HERE / "package.json").open() as f:
    version = json.load(f)['version']

lab_path = HERE / name / "labextension"

# Representative files that should exist after a successful build
jstargets = [
    str(HERE / "lib" / "index.js"),
    str(lab_path / "package.json"),
]

package_data_spec = {
    name: [
        "*"
    ]
}

labext_name = "@adhadse/theme-material-darcula"

data_files_spec = [
    ("share/jupyter/labextensions/%s" % labext_name, str(lab_path), "**"),
    ("share/jupyter/labextensions/%s" % labext_name, str(HERE), "install.json"),
]

cmdclass = create_cmdclass(
    "jsdeps",
    package_data_spec=package_data_spec,
    data_files_spec=data_files_spec
)

js_command = combine_commands(
    install_npm(HERE, build_cmd="build:prod", npm=["jlpm"]),
    ensure_targets(jstargets),
)

is_repo = (HERE / ".git").exists()
if is_repo:
    cmdclass["jsdeps"] = js_command
else:
    cmdclass["jsdeps"] = skip_if_exists(jstargets, js_command)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name=name,
    version=version,
    url="https://github.com/adhadse/theme-material-darcula",
    author="Anurag Dhadse",
    description="A Jupyterlab theme inspired from JetBrains IDE's Darcula scheme and Material Design.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    cmdclass=cmdclass,
    zip_safe=False,
    # distclass=conda_build.bdist_conda.CondaDistribution,
    packages=setuptools.find_packages(),
    install_requires=[
        "jupyterlab>=3.0.0"
    ],
    include_package_data=True,
    python_requires=">=3.6",
    license="BSD-3-Clause",
    platforms="Linux, Mac OS X, Windows",
    keywords=["Jupyter", "JupyterLab"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Jupyter",
    ],
)


if __name__ == "__main__":
    setuptools.setup(**setup_args)
