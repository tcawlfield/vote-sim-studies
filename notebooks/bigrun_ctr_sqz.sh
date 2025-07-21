#!/bin/bash

set -ex

export RUST_LOG=warn

./voting -c ctr_sqz.toml -t 2000000 -v 100000 -C 2 -o ctr_sqz_1d_2c.parquet
./voting -c ctr_sqz.toml -t 2000000 -v 100000 -C 3 -o ctr_sqz_1d_3c.parquet
./voting -c ctr_sqz.toml -t 2000000 -v 100000 -C 5 -o ctr_sqz_1d_5c.parquet
./voting -c ctr_sqz.toml -t 2000000 -v 100000 -C 8 -o ctr_sqz_1d_8c.parquet
