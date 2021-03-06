oscca-sembei : Segmentation-free version of OSCCA
===================================================

単語分割を経由しない単語埋め込み手法 *segmentation-free word embeddings (sembei)* [1] の Python 実装．
この実装では，行列分解に基づく単語埋め込み手法 eigenwords (OSCCA) [2] をベースにしている．


## Installation

```sh
git clone https://github.com/shimo-lab/sembei
cd sembei
python setup.py build && python setup.py install
```

## How to use

`./sample_code/` のファイルを参照．


## Requirements

* anaconda3 (>=4.2.0)


## References

1. 押切 孝将, 下平 英寿. **単語分割を経由しない単語埋め込み**. 言語処理学会第23回年次大会論文集, pp.258-261. 言語処理学会, 2017年3月.
2. Dhillon, P. S., Foster, D. P., and Ungar, L. H. (2015). **Eigenwords: Spectral word embeddings**. Journal of Machine Learning Research, 16:3035–3078.
