# Copyright (c) Anurag Dhadse.
# Distributed under the terms of the Modified BSD License.
# Adapted from https://github.com/jupyter-lsp/jupyterlab-lsp/blob/master/scripts/publish_pypi.sh

rm dist/*
python3 setup.py sdist
twine upload dist/* -r testpypi
echo "Published to testpypi"
while true; do
    read -p "Do you wish to publish to pypi?" yn
    case $yn in
        [Yy]* ) twine upload dist/*; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done