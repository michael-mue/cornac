# Copyright 2018 The Cornac Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Example for RecVAE"""

import cornac
from cornac.datasets import movielens
from cornac.eval_methods import RatioSplit

# Load MovieLens 1M ratings
ml_1m = movielens.load_feedback(variant="1M")

# Define an evaluation method to split feedback into train and test sets
ratio_split = RatioSplit(
    data=ml_1m, test_size=0.2, exclude_unknowns=False, verbose=True
)

# Instantiate the global average baseline and MF model
global_avg = cornac.models.GlobalAvg()
recvae = cornac.models.RecVAE(verbose=True)

# Instantiate MAE and RMSE for evaluation
mae = cornac.metrics.MAE()
rmse = cornac.metrics.RMSE()
ndcg = cornac.metrics.NDCG(k=100)
recall = cornac.metrics.Recall(k=100)

# Put everything together into an experiment and run it
cornac.Experiment(
    eval_method=ratio_split,
    models=[
        global_avg,
        recvae,
    ],
    metrics=[mae, rmse, ndcg, recall],
    user_based=True,
).run()