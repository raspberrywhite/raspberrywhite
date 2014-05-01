export PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
export PYENV_HOME=$WORKSPACE/.pyenv/

if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

wget https://dl.dropboxusercontent.com/u/35837126/assets.zip
unzip assets.zip -d tests/

virtualenv --no-site-packages $PYENV_HOME
. $PYENV_HOME/bin/activate
pip install -r requirements.txt
nosetests tests/