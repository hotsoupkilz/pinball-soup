# pinball_soup

- install pyenv & activate virtualenv plugin
- install python versions
- $ env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install --verbose 3.12.3
- $ env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install --verbose 3.9.12
- $ pyenv virtualenv 3.9.12 mpf3912
- $ pyenv virtualenv 3.12.3 mpf3123
- $ pyenv activate mpf3912

