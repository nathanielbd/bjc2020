# Breakthrough Junior Challenge 2020

Script and Manim code. The inverted pendulum simulation code can be found [here](https://github.com/SASE-Labs-2021/inverted-pendulum).

## Usage

First, [install MiKTeX](https://miktex.org/download)

```
# install dependencies in Ubuntu
sudo apt install pkg-config libcairo2-dev ffmpeg sox texlive

# install required latex packages
sudo apt install texlive-latex-extra    # "standalone"
sudo apt install texlive-fonts-extra    # "dsfont"
sudo apt install texlive-science        # "physics"

# install manim
git clone https://github.com/3b1b/manim.git
cd manim
conda env create -f environment.yml
conda activate manim
python3 -m pip install -r requirements.txt
cd ..
git clone https://github.com/nathanielbd/bjc2020.git
```

Add the folowing lines to the preamble of `manim/manimlib/tex_template.tex`:
```
\usepackage{tikz}
\usetikzlibrary{positioning}
```

Finally, 

```
cd manim
python3 -m manim ../jbc2020/scenes.py <SceneName> -pl
```

`-pl` flag means preview at low quality. For production level quality, use `-p`.
